#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import listRepoPackages
import sys

server = "localhost"
user = "root"
passwd = ""
db = "test"

try:
    # get pisi index file full path
    index_file = sys.argv[1]
except:
    print """
Usage: python main.py <full_path_of_pisi_index_file>
"""
    sys.exit(0)

# Connect DB
print "---connecting DB"
db = MySQLdb.connect(server, user, passwd, db)

# Get package names and maintainer addresses
print "---parse index file"
packDict = listRepoPackages.getFullList(index_file)

# Execute a query to insert/update components infos
# packDict = {"package_name":"maintainer@foo.bar"}
# profiles = {"maintainer@foo.bar":id}

errors = {'db':[], 'mail':[]}
procs = {'update':0, 'insert':0}

for pack in packDict.iterkeys():
    cPackage = db.cursor()

    # pack = package name
    # packDict[pack] = email
    
    try:
       email = str(packDict[pack])

       numRows = cPackage.execute("SELECT owner FROM component WHERE name = '%s'" % pack)

       if not numRows == 0:
           print "---updating %s package, package owner is %s" % (str(pack), email)
           cPackage.execute("UPDATE component SET owner = '%s' WHERE name = '%s'" % (email, str(pack)))
           procs['update'] += 1
       else:
           print "---inserting %s package, package owner is %s" % (str(pack), email)
           cPackage.execute("INSERT INTO component(name, owner) VALUES (%s, %s)",(str(pack), email))
           procs['insert'] += 1

       db.commit()

    except MySQLdb.Error, e:
        errors['db'].append(e.__str__())
    except KeyError, e:
        errors['mail'].append(str(e))

print "\nThere are %s packages in repo" % packDict.keys().__len__()
print "%s packages inserted, %s packages updated\n" % (procs["insert"], procs["update"])

print "---DB Errors (%s)" % errors['db'].__len__()
print "\n".join(errors['db'])

print "---Unknown Mail Addresses (%s)" % errors['mail'].__len__()
print "\n".join(list(set(errors['mail'])))
