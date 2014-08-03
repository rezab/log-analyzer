<html>
<title></title>
<body>

<h2>About</h2>
<p>
Log Analyzer is an opensource project, aims at Monitoring and Analyzing log files of different services.
</p>

<h2>Basic Usage</h2>
<code>
PYTHONPATH=. DJANGO_SETTINGS_MODULE=LogAnalyzer.settings servicelog/logtail.py
</code>

<h2>Requirements</h2>
<p>
Django and Tornado.
</p>
<p>For Ubuntu, you need to install:
<p><code>apt-get install python-django</code></p>
<p><code>apt-get install python-tornado</code></p>
</p>

<h2>How to use this:</h2>
<p>
Config the database:
</p>
<p><code>python manage.py syncdb</code></p>
<p>
Run server:
</p>
<p><code>python manage.py runserver 0:8000</code></p>
<p>
Visit admin page:
</p>
<p><code>http://localhost:8000/admin</code></p>


</body>
</html>
