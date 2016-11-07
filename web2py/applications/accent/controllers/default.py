# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
from test_script import demoCall

#@auth.requires_login()
def index():
    """
    This is your main controller.
    """
    # I am creating a bogus list here, just to have some divs appear in the
    # view.  You need to read at most 20 posts from the database, in order of
    # most recent first, and you need to return that list here.
    # Note that posts is NOT a list of strings in your actual code; it is
    # what you get from a db(...).select(...).
    posts = ['banana', 'pear', 'eggplant']
    return dict(posts=posts)


@request.restful()
def api():
    response.view = 'generic.json'

    def GET(tablename, id):
        if not tablename == 'acc':
            raise HTTP(400)
        return dict(acc = db.acc(id))

    #temp returning status success until we have validation in place
    def POST(tablename, **fields):
        status = None
        if tablename == 'acc':
            #TODO: check if acc exists? look up validate_and_insert return val
            status = 'success'
            resp = dict(status = status,acc = db.acc.validate_and_insert(**fields))
            return response.json(resp)
        elif tablename == 'test':
	    status = 'success'
	    resp = dict(status = status, test = demoCall())
	    return response.json(resp)
	else:
	    raise HTTP(400);
      #  if table_name == 'person':
       #     return dict(db.person.validate_and_insert(**vars))
       # elif table_name == 'pet':
       #     return dict(db.pet.validate_and_insert(**vars))
       # else:
       #     raise HTTP(400)  
    #locals() returns a dictionary including all the variables in the local function         
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


