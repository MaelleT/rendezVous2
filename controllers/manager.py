# -*- coding: utf-8 -*-
def charger_jardin():
    if request.vars.csvfile != None:

        table = db[request.vars.table]
        file = request.vars.csvfile.file

        table.import_from_csv_file(file)

        response.flash = 'Data uploaded'
    return dict()

def nouveauRDV():
    form=SQLFORM(db.rendezVous)
    if form.process():
        response.flash='Nouveau Rendez-vous ajouté'
    elif form.errors :
        reponse.flash='erreur dans saisie Rendez-vous'
        
    return locals()
