# -*- coding: utf-8 -*-
db.define_table('theme',
                Field('Libelle','string', requires=IS_NOT_EMPTY()))

db.define_table('jardin',
               Field('Libelle','string',requires=IS_NOT_EMPTY()),
               Field('adresse_postale','string',requires=IS_NOT_EMPTY()),
               Field('Jeux','string',requires=IS_IN_SET("OUI","NON")),
               Field('Mobilier_pique_nique','string',requires=IS_IN_SET("OUI","NON")),
               Field('Pataugeoire','string',requires=IS_IN_SET("OUI","NON")),
               Field('Point_d_eau','string',requires=IS_IN_SET("OUI","NON")),
               Field('Commentaire','text'),
               )

db.define_table('rendezVous',
                Field('DateRDV','datetime',requires=IS_DATETIME(format=T('%d-%m-%Y %H:%M')),label='Date'),
                Field('Lieu','reference jardin',requires=IS_IN_DB(db,db.jardin.id,'%(Libelle)s')),
                Field('Commentaire','text',requires=IS_NOT_EMPTY()),
                Field('Theme','reference theme',requires=IS_IN_DB(db,db.theme.id,'%(Libelle)s')),
               )
