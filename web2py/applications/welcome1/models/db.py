# -*- coding: utf-8 -*-

# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations

if request.global_settings.web2py_version < "2.14.1":
    raise HTTP(500, "Requires web2py 2.13.3 or newer")

# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# request.requires_https()

# app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig

# once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # if NOT running on Google App Engine use SQLite or other DB
    db = DAL(myconf.get('db.uri'),
             pool_size=myconf.get('db.pool_size'),
             migrate_enabled=myconf.get('db.migrate'),
             check_reserved=['all'])
    # I like to keep the session in the db.
    session.connect(request, response, db=db)
else:
    # connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    # store sessions and tickets there
    session.connect(request, response, db=db)
    #
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))

# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []

# choose a style for forms
response.formstyle = myconf.get('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.get('forms.separator') or ''

# (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# (optional) static assets folder versioning
# response.static_version = '0.0.0'

# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)

from gluon.tools import Auth, Service, PluginManager

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=myconf.get('host.names'))
service = Service()
plugins = PluginManager()

# create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

#db.define_table(
 #   'auth_group',
  #  Field('first_name', length=128, default=''),
   # Field('last_name', length=128, default=''),
    #Field('email', length=128, default='', unique=False), # required
    #Field('password', 'password', length=512,            # required
    #      readable=False, label='Password'),
    #Field('registration_key', length=512,                # required
    #      writable=False, readable=False, default=''),
    #Field('reset_password_key', length=512,              # required
    #      writable=False, readable=False, default=''),
    #Field('registration_id', length=512,                 # required
    #      writable=False, readable=False, default=''))

## do not forget validators
custom_auth_table = db[auth.settings.table_user_name] # get the custom_auth_table
custom_auth_table.first_name.requires =   IS_NOT_EMPTY(error_message=auth.messages.is_empty)
custom_auth_table.last_name.requires =   IS_NOT_EMPTY(error_message=auth.messages.is_empty)
custom_auth_table.password.requires = [IS_STRONG(), CRYPT()]
custom_auth_table.email.requires = [
  IS_EMAIL(error_message=auth.messages.invalid_email),
  IS_NOT_IN_DB(db, custom_auth_table.email)]

auth.settings.table_user = custom_auth_table # tell auth to use custom_auth_table

## before auth.define_tables()

# configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.get('smtp.server')
mail.settings.sender = myconf.get('smtp.sender')
mail.settings.login = myconf.get('smtp.login')
mail.settings.tls = myconf.get('smtp.tls') or False
mail.settings.ssl = myconf.get('smtp.ssl') or False

# configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield

######################
# Logging
import logging, sys
FORMAT = "%(asctime)s %(levelname)s %(process)s %(thread)s %(funcName)s():%(lineno)d %(message)s"
logging.basicConfig(stream=sys.stderr)
logger = logging.getLogger(request.application)
logger.setLevel(logging.INFO)

# Let's log the request.
logger.info("====> Request: %r %r %r %r" % (request.env.request_method, request.env.path_info, request.args, request.vars))
