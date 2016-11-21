# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.

import datetime

db.define_table('acc',
                Field('firstname', writable=True),
                Field('lastname', writable=True),
                Field('password', writable=True),
                Field('email', writable=True))

db.define_table('sentence',
		Field('email', writable=True),
		Field('speech', writable=True),
		Field('corrected', writable=True))
