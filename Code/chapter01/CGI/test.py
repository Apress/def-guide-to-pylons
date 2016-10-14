#!/usr/bin/env python

# Get the configuration for the script
import ConfigParser
config = ConfigParser.ConfigParser()
config.read('/path/to/config.ini')

# If debugging is enabled, set up the cgitb module
if config.get('general', 'debug') == 'on':
    import cgitb; cgitb.enable()

# Begin the non-configuration-dependent imports
import cgi
import MySQLdb
import os

# Output the HTTP headers
print "Content-type: text/html\n\n"

# Output the head of the HTML page
print "<html><head><title>Example</title></head>"
print "<body><h1>Example</h1><p>Here are the comments:</p>"

# Get the ID from the URL based on the QUERY_STRING environment
# variable using the cgi module
fields = cgi.FieldStorage()
page = int(fields['page'].value)

# Fetch data from the database
connection = MySQLdb.connect(
    db=config.get('database', 'database'),
    user=config.get('database', 'user'),
    passwd=config.get('database', 'password'),
    host=config.get('database', 'host')
)
cursor = connection.cursor()
cursor.execute("SELECT id, data FROM comment WHERE page=%s", (page,))
results = cursor.fetchall()
cursor.close()
connection.close()

# Output the comments
for id, data in results:
    print "<p>Commment #%s: %s</p>"%(id, cgi.escape(data))

# Output the rest of the HTML page
print "</body></html>"

