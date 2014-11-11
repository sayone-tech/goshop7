# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="devs"
#__date__ ="$Mar 23, 2014 5:31:42 PM$"
#
def runthis():
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    for row in cursor.fetchall():
        cursor.execute("ALTER TABLE %s CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;" % (row[0]))
        print row
def change_db_engine():
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    for row in cursor.fetchall():
        cursor.execute("ALTER TABLE %s ENGINE=MyISAM" % (row[0]))
        print row