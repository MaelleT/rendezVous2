# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    Affichage d'une information le Saviez-vous sur un jardin pris au hasard.
    Accès à la liste des jardins
    """
    rows=db(db.jardin.Commentaire!= "").select(db.jardin.Libelle, db.jardin.Commentaire)
    nb=db(db.jardin.Commentaire!="").count()
    import random
    n = random.randint(1,nb-1)
    
    row=rows[n]
    return locals()

def listeJardins():
    """
    Affiche la liste des jardins
    """
    rows=db().select(db.jardin.id,db.jardin.Libelle)
    return locals()

def infosJardin():
    """
    Affiche les informations sur un jardin en particulier
    """
    idJardinChoisi=request.vars.jardins
    row=db(db.jardin.id==idJardinChoisi).select(db.jardin.ALL)
    rowsRDV=db(db.rendezVous.Lieu==idJardinChoisi).select(db.rendezVous.ALL)

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
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
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
