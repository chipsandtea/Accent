# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
import ginger2

#@auth.requires_login()
def index():
    posts = ['temp index']
    return dict(posts=posts)


@request.restful()
def api():
    response.view = 'generic.json'

    def GET(*args, **vars):
	status = None
	error = None
	#pattern matching for login and getting sentences
	patterns = [
	   "/login/{acc.email}/{acc.password}",
	   "/{sentence.email}/get"
	]
	#maps request args from URL to a db query    	
	parser = db.parse_as_rest(patterns, args, vars)
	#successfully parsed the request
        if parser.status == 200:
	    #returns rows from db query
	    resp = parser.response
	    print resp
	    #no rows returned, email and pw did not match
	    if len(resp) == 0:
		status = 'failure'
		if args[0] == 'login':
	 	    error = 'Email and password did not match'
		return response.json(dict(status = status, error = error))	
	    #return a response with the queried content
	    else:
		status = 'success'	
	    return response.json(dict(status = status, content = resp))	
	#raises 400 if no matching pattern 
	elif parser.status == 404:
	    return response.json(dict(status = 'failure', error = parser.error))
	else:
	    raise HTTP(400) 
    
    def POST(tablename, **fields):
	#========creating account================
        if tablename == 'acc':
            #check if acc exists? look up validate_and_insert return value
	    existing = db(db.acc.email == request.post_vars.email).select().first()
	    print tablename
            if existing is None:
		resp = dict(status = 'success',acc = db.acc.validate_and_insert(**fields))
	    else: 
            	resp = dict(status = 'failure', error = 'email already exists')

            return response.json(resp)

        #========corecting input ======================
	elif tablename == 'sentence':
	    fields['corrected'] = ginger2.main(fields['speech'])
	    #return row after inserting
	    row = db.sentence.validate_and_insert(**fields)
	    rid = row.id
	    resp = dict(status = 'success', content = db.sentence[rid])
	    return response.json(resp)
	#========invalid request===============
	else:
	    raise HTTP(400)
   	#locals() returns a dict including all vars in the local func 
    return locals()      

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


