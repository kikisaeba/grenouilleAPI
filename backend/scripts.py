import logging
import json
import os
from datetime import datetime
import hashlib

from flask_script import Manager

from app import create_app
from models import db, APIKey, APIKeyScope, User, UserScope, Scope, Game, GameStatus, GameVIP, GameVIPType, DotaHero, DotaItem

app = create_app()
manager = Manager(app)


###########
# Scripts #
###########

@manager.command
def hello_world():
    """Simple script example."""
    print('Hello World')

@manager.option('--key', dest='key', default=None)
@manager.option('--description', dest='description', default=None)
def add_api_key(key, description):
    """Add a new API Key to the system.

    Args:
        key: key value string to add.
        description: key description as a reminder.
    """
    if key is None:
        print('No API key specified')
        return
    if description is None:
        print('No description specified')
        return

    salt = app.config['API_KEY_SALT']
    hash_object = hashlib.sha1((key + salt).encode('utf-8'))
    hash_key = hash_object.hexdigest()
    api_key = db.session().query(APIKey).filter(APIKey.key_hash == hash_key).one_or_none()

    if api_key is not None:
        print('Key already in the system')
    else:
        key = APIKey(hash_key, description)
        db.session().add(key)
        db.session().commit()
        print('Key added')

@manager.option('--key', dest='key', default=None)
@manager.option('--scope', dest='scope', default=None)
def add_scope_api_key(key, scope):
    """Add a scope to target APIKey

    Args:
        key: key value.
        scope: scope to add.
    """
    if key is None:
        print('No API key specified')
        return
    if scope is None:
        print('No scope specified')
        return
    if scope not in [x.value for x in list(Scope)]:
        print('Invalid scope')
        return

    salt = app.config['API_KEY_SALT']
    hash_object = hashlib.sha1((key + salt).encode('utf-8'))
    hash_key = hash_object.hexdigest()
    api_key = db.session().query(APIKey).filter(APIKey.key_hash == hash_key).one_or_none()

    if api_key is None:
        print('Key not present!')
    else:
        APIKeyScope.upsert(api_key.key_hash, scope)
        print('Scope added')

@manager.option('--id', dest='id', default=None)
@manager.option('--scope', dest='scope', default=None)
@manager.option('--force', dest='force', default=False)
def add_scope_user(id, scope, force):
    """Add a scope to a steam ID.

    Args:
        id: user steam ID value.
        scope: scope to add.
        force: force adding user to database.
    """
    if id is None:
        print('No user steamId')
        return
    if scope is None:
        print('No scope specified')
        return
    if scope not in [x.value for x in list(Scope)]:
        print('Invalid scope')
        return
    user = db.session().query(User).filter(User.id == id).one_or_none()

    if user is None:
        if force is False:
            print('User not present!')
            return
        else:
            user = User(id)
            db.session.add(user)
            db.session.commit()

    UserScope.upsert(user.id, scope)
    print('Scope added')

@manager.command
def clean_rogue_scopes():
    """Clean rogue scopes from database."""
    all_scopes = [x.value for x in list(Scope)]
    for user_scope in db.session.query(UserScope).all():
        if user_scope.scope not in all_scopes:
            db.session.delete(user_scope)
    for key_scope in db.session.query(APIKeyScope).all():
        if key_scope.scope not in all_scopes:
            db.session.delete(key_scope)
    db.session.commit()

@manager.command
def init_database():
    """Initialize database with dota value."""

    # Insert Heroes
    hero_json_path = os.path.join(os.path.dirname(__file__), 'ressources', 'json', 'dota_heroes.json')
    if os.path.isfile(hero_json_path):
        with open(hero_json_path, 'r') as hero_json_file:
            hero_json = json.loads(hero_json_file.read())
        for hero in hero_json['heroes']:
            DotaHero.upsert(hero['id'], hero['name'], hero['short_name'], hero['localized_name'])

    # Insert Items
    item_json_path = os.path.join(os.path.dirname(__file__), 'ressources', 'json', 'dota_items.json')
    if os.path.isfile(item_json_path):
        with open(item_json_path, 'r') as item_json_file:
            item_json = json.loads(item_json_file.read())
        for item in item_json['items']:
            DotaItem.upsert(item['id'], item['name'], item['short_name'], item['localized_name'])

#######################
# Setup Manage Script #
#######################
if __name__ == '__main__':
    manager.run()
