# dict.py - using DictCUrsor/DictRow
#
# Copyright (C) 2005 Federico Di Gregorio  <fog@debian.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.

## put in DSN your DSN string

DSN = 'dbname=test'

## don't modify anything below this line (except for experimenting)

import sys
import psycopg
import psycopg.extras

if len(sys.argv) > 1:
    DSN = sys.argv[1]

print "Opening connection using dsn:", DSN
conn = psycopg.connect(DSN)
print "Encoding for this connection is", conn.encoding

    
curs = conn.cursor(cursor_factory=psycopg.extras.DictCursor)
curs.execute("SELECT 1 AS foo, 'cip' AS bar, date(now()) as zot")

data = curs.fetchone()
print "Some data accessed both as tuple and dict:"
print " ", data['foo'], data['bar'], data['zot']
print " ", data[0], data[1], data[2]

# execute another query and demostrate we can still access the row
curs.execute("SELECT 2 AS foo")
print "Some more data accessed both as tuple and dict:"
print " ", data['foo'], data['bar'], data['zot']
print " ", data[0], data[1], data[2]