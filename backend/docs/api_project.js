define({
  "name": "GrenouilleAPI",
  "version": "1.0.4",
  "description": "API used with multiple FroggedTV services.",
  "header": {
    "title": "Presentation",
    "content": "<h2>Endpoints access</h2>\n<p>Endpoints are protected with 2 possible ways, specified in endpoint headers. API calls are limited to 50 per minutes per ip.</p>\n<p>First you can use an APIKey if the &lt;API_KEY&gt; header is present. If you have a logged user, you can use a auth token in the <Authorization> header. In this case, the user needs to have the appropriate user rights to use the endpoint.</p>\n<h2>Authentication</h2>\n<p>User authentication module. User logs with steam, and is redirected to the website with a refresh token valid for 60 days. The refresh token is then used to get a auth token, valid for 1 hour. The token is used to access multiple endpoints.</p>\n<h2>DotaBots</h2>\n<p>Bots used to host inhouse leagues.</p>\n<h2>User</h2>\n<p>User management endpoints.</p>\n<h2>Community</h2>\n<p>Community endpoints for news, calendar, comments.</p>\n<h2>StreamSystem</h2>\n<p>Endpoints used for the automatic streaming system, managing VODs and the forever running OBS.</p>\n"
  },
  "sampleUrl": false,
  "defaultVersion": "0.0.0",
  "apidoc": "0.3.0",
  "generator": {
    "name": "apidoc",
    "time": "2018-06-20T19:10:48.344Z",
    "url": "http://apidocjs.com",
    "version": "0.17.6"
  }
});
