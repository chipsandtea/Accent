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
                Field('firstname'),
                Field('lastname'),
                Field('password'),
                Field('email'))

#db.define_table('pet',
 #               Field('ownedby', db.person),
  #              Field('name'),
   #             Field('info'))

# I don't want to display the user email by default in all forms.

# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
