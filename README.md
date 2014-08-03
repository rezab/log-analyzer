<html>
<title></title>
<body>

<h2>About</h2>
<p>
Log Analyzer is an opensource project, aims at Monitoring and Analyzing log files of different services.
</p>


<h1>Requirements</h1>
<p>
Django and Tornado.
</p>
<p>For Ubuntu, you need to install:
<p><code>apt-get install python-django</code></p>
<p><code>apt-get install python-tornado</code></p>
</p>

<hr/>

<h1>Installation</h1>

<p>
Config the database:
</p>
<p><code>python manage.py syncdb</code></p>
While populating database, the user and password would be asked. use them to enter admin page.
<p>

TODO: config the static address path in servicelog/logtail.py
<p>

Make this file executable:

<code>
chmod +x servicelog/logtail.py
</code>
<p>

Run Log Server:
<p>
<code>
PYTHONPATH=. DJANGO_SETTINGS_MODULE=LogAnalyzer.settings servicelog/logtail.py
</code>

<hr/>

<h1>Basic Usage</h1>

Visit admin page:
</p>
<p><code>http://localhost:8001/admin</code></p>

Add log files in admin page.

<p>
Visit User Page:
</p>
<p><code>http://localhost:8001/servicelog/instance/</code></p>

Enjoy it !

</body>
</html>
