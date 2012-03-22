# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Log(models.Model):
    auteur = models.CharField(max_length=30, db_column='Auteur') # Field name made lowercase.
    date = models.DateTimeField(primary_key=True,db_column='Date') # Field name made lowercase.
    ip = models.CharField(primary_key=True,max_length=45, db_column='IP') # Field name made lowercase.
    action = models.TextField(db_column='Action') # Field name made lowercase.
    class Meta:
        db_table = u'LOG'

class LogEleve(models.Model):
    user = models.ForeignKey('User',max_length=60,db_column='uid',primary_key=True)
    date = models.DateTimeField(primary_key=True,db_column='Date') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    class Meta:
        db_table = u'LOG_eleve'

class Absence(models.Model):
    ideleve = models.ForeignKey('Eleve',db_column='idEleve',primary_key=True) # Field name made lowercase.
    date = models.DateField(primary_key=True,db_column='Date') # Field name made lowercase.
    idactivite = models.ForeignKey('Activite',max_length=24, db_column='idActivite',primary_key=True) # Field name made lowercase.
    class Meta:
        db_table = u'absence'

class Activite(models.Model):
    idactivite = models.CharField(max_length=24, db_column='idActivite', unique=True) # Field name made lowercase.
    idmatiere = models.ForeignKey('Matiere',max_length=18, db_column='idMatiere') # Field name made lowercase.
    type = models.ForeignKey('Typeactivite',max_length=3, db_column='Type') # Field name made lowercase.
    coefficient = models.FloatField(db_column='Coefficient') # Field name made lowercase.
    nom = models.CharField(max_length=768, db_column='Nom') # Field name made lowercase.
    nb_h_prevu = models.IntegerField(db_column='NbHPrevu') # Field name made lowercase.
    annee = models.CharField(max_length=3, db_column='Annee') # Field name made lowercase.
    sans_note = models.IntegerField(db_column='SansNote') # Field name made lowercase.
    note_visible = models.CharField(max_length=1, db_column='NoteVisible') # Field name made lowercase.
    semestre = models.IntegerField(db_column='Semestre') # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'activite'

class Admins(models.Model):
    login = models.CharField(primary_key=True,max_length=60)
    class Meta:
        db_table = u'admins'

class Anneeuniversitaire(models.Model):
    idanneeuniversitaire = models.IntegerField(primary_key=True, db_column='idAnneeUniversitaire') # Field name made lowercase.
    date_debut = models.DateField(db_column='DateDebut') # Field name made lowercase.
    date_fin = models.DateField(db_column='DateFin') # Field name made lowercase.
    nom = models.CharField(max_length=60, db_column='Nom') # Field name made lowercase.
    class Meta:
        db_table = u'anneeuniversitaire'

class BilanActivite(models.Model):
    idanneeuniversitaire = models.ForeignKey('Anneeuniversitaire',db_column='idAnneeUniversitaire',primary_key=True) # Field name made lowercase.
    idactivite = models.ForeignKey('Activite',max_length=24, db_column='idActivite',primary_key=True) # Field name made lowercase.
    min = models.FloatField()
    max = models.FloatField()
    moyenne = models.FloatField()
    ecart_type = models.FloatField()
    pourcent_saisie = models.FloatField()
    class Meta:
        db_table = u'bilan_activite'

class BilanEleve(models.Model):
    idbilaneleve = models.IntegerField(primary_key=True, db_column='idBilanEleve') # Field name made lowercase.
    ideleve = models.ForeignKey('Eleve',db_column='idEleve') # Field name made lowercase.
    idcontratpedagogique = models.ForeignKey('Contratpedagogique',db_column='idContratPedagogique') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenne_ds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficient_ds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyenne_tp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficient_tp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nb_eleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    redoublement = models.CharField(max_length=1)
    exclusion = models.CharField(max_length=1)
    absences = models.IntegerField()
    coefficients = models.FloatField()
    coefficient_dispenses = models.FloatField(db_column='coefficientDispenses') # Field name made lowercase.
    decision_jury = models.TextField(db_column='decisionJury') # Field name made lowercase.
    moyenne_sem1 = models.FloatField(db_column='moyenneSEM1') # Field name made lowercase.
    moyenne_sem2 = models.FloatField(db_column='moyenneSEM2') # Field name made lowercase.
    moyenne_norm = models.FloatField(db_column='moyenneNorm') # Field name made lowercase.
    moyenne_norm_ds = models.FloatField(db_column='moyenneNormDS') # Field name made lowercase.
    moyenne_norm_tp = models.FloatField(db_column='moyenneNormTP') # Field name made lowercase.
    ects_valides = models.IntegerField(db_column='ectsValides') # Field name made lowercase.
    class Meta:
        db_table = u'bilan_eleve'

class BilanLaniere(models.Model):
    idbilanlaniere = models.IntegerField(primary_key=True, db_column='idBilanLaniere') # Field name made lowercase.
    ideleve = models.ForeignKey('Eleve',db_column='idEleve') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenne_ds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficient_ds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyenne_tp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficient_tp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    idlaniere = models.ForeignKey('Laniere',max_length=9, db_column='idLaniere') # Field name made lowercase.
    qualification = models.CharField(max_length=3)
    rattrapage = models.CharField(max_length=1)
    ects_valides = models.IntegerField(db_column='ectsValides') # Field name made lowercase.
    class Meta:
        db_table = u'bilan_laniere'

class BilanMatiere(models.Model):
    idbilanmatiere = models.IntegerField(primary_key=True, db_column='idBilanMatiere') # Field name made lowercase.
    ideleve = models.ForeignKey('Eleve',db_column='idEleve') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenne_ds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficient_ds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyenne_tp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficient_tp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nb_eleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    idmatiere = models.ForeignKey('Matiere',max_length=18, db_column='idMatiere') # Field name made lowercase.
    qualification = models.CharField(max_length=3)
    class Meta:
        db_table = u'bilan_matiere'

class Contenucontratpedagogique(models.Model):
    idcontratpedagogique = models.ForeignKey ('Contratpedagogique',db_column='idContratPedagogique',primary_key=True) # Field name made lowercase.
    idmatiereyoratooid = models.ForeignKey('Matiere',max_length=30, db_column='idMatiereYoratooID',primary_key=True) # Field name made lowercase.
    coefficient = models.FloatField(db_column='Coefficient') # Field name made lowercase.
    class Meta:
        db_table = u'contenucontratpedagogique'

class Contratpedagogique(models.Model):
    idcontratpedagogique = models.IntegerField(primary_key=True, db_column='idContratPedagogique') # Field name made lowercase.
    idanneeuniversitaire = models.ForeignKey('Anneeuniversitaire',db_column='idAnneeUniversitaire') # Field name made lowercase.
    idepoque = models.ForeignKey('Epoque',db_column='idEpoque') # Field name made lowercase.
    credits = models.FloatField(db_column='Credits') # Field name made lowercase.
    nom = models.CharField(max_length=60, db_column='Nom') # Field name made lowercase.
    class Meta:
        db_table = u'contratpedagogique'

class CoursEleve(models.Model):
    ideleve = models.ForeignKey('Eleve',db_column='idEleve',primary_key=True) # Field name made lowercase.
    idactivite = models.ForeignKey('Activite',max_length=24, db_column='idActivite',primary_key=True) # Field name made lowercase.
    class Meta:
        db_table = u'cours_eleve'

class CreditsEtranger(models.Model):
    #ideleve = models.FloatField(primary_key=True, db_column='idEleve') # Field name made lowercase.
    idcreditsetranger = models.IntegerField(primary_key=True,db_column='idCreditsEtranger')
    ideleve = models.ForeignKey('Eleve', db_column='idEleve') # Field name made lowercase.
    credits = models.IntegerField()
    etablissement = models.CharField(max_length=120)
    auteur = models.CharField(max_length=30, db_column='Auteur') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    class Meta:
        db_table = u'credits_etranger'

class Dispense(models.Model):
    ideleve = models.ForeignKey('Eleve',db_column='idEleve',primary_key=True) # Field name made lowercase.
    auteur = models.CharField(max_length=30, db_column='Auteur') # Field name made lowercase.
    date = models.DateTimeField(primary_key=True,db_column='Date') # Field name made lowercase.
    raison = models.CharField(max_length=120, db_column='Raison') # Field name made lowercase.
    idactivite = models.ForeignKey('Activite',max_length=24, db_column='idActivite',primary_key=True) # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    class Meta:
        db_table = u'dispense'

class Eleve(models.Model):
    ideleve = models.IntegerField(primary_key=True, db_column='idEleve') # Field name made lowercase.
    nom = models.CharField(max_length=120, db_column='Nom') # Field name made lowercase.
    nom_reseau = models.CharField(max_length=90, db_column='NomReseau') # Field name made lowercase.
    binomes1 = models.IntegerField(db_column='Binomes1') # Field name made lowercase.
    binomes2 = models.IntegerField(db_column='Binomes2') # Field name made lowercase.
    binomes3 = models.IntegerField(db_column='Binomes3') # Field name made lowercase.
    annee = models.IntegerField('Anneeuniversitaire',db_column='Annee') # Field name made lowercase.
    groupe = models.IntegerField(db_column='Groupe') # Field name made lowercase.
    echange = models.CharField(max_length=3, db_column='Echange') # Field name made lowercase.
    date_naissance = models.DateField(db_column='DateNaissance') # Field name made lowercase.
    origine = models.CharField(max_length=3, db_column='Origine') # Field name made lowercase.
    mail = models.CharField(max_length=150)
    type = models.ForeignKey('Eleve',max_length=3, db_column='Type') # Field name made lowercase.
    tuteur = models.CharField(max_length=6, db_column='Tuteur') # Field name made lowercase.
    class Meta:
        db_table = u'eleve'

class Epoque(models.Model):
    idepoque = models.IntegerField(primary_key=True, db_column='idEpoque') # Field name made lowercase.
    nom = models.CharField(max_length=60, db_column='Nom') # Field name made lowercase.
    annee = models.ForeignKey('Anneeuniversitaire',db_column='Annee') # Field name made lowercase.
    semestre = models.IntegerField(db_column='Semestre') # Field name made lowercase.
    class Meta:
        db_table = u'epoque'

class EtudiantContratpedagogique(models.Model):
   # ideleve = models.FloatField(primary_key=True, db_column='idEleve') # Field name made lowercase.
    ideleve = models.ForeignKey('Eleve', db_column='idEleve',primary_key=True) # Field name made lowercase.
    idcontratpedagogique = models.ForeignKey('Contratpedagogique',db_column='idContratPedagogique',primary_key=True) # Field name made lowercase.
    valide = models.CharField(max_length=1, db_column='Valide') # Field name made lowercase.
    classement_visible = models.IntegerField(db_column='ClassementVisible') # Field name made lowercase.
    class Meta:
        db_table = u'etudiant_contratpedagogique'

class Laniere(models.Model):
    idlaniere = models.CharField(primary_key=True,max_length=9, db_column='idLaniere') # Field name made lowercase.
    nom = models.CharField(max_length=78, db_column='Nom') # Field name made lowercase.
    barre_ds = models.FloatField(db_column='BarreDS') # Field name made lowercase.
    barre_tp = models.FloatField(db_column='BarreTP') # Field name made lowercase.
    barre_generale = models.FloatField(db_column='BarreGenerale') # Field name made lowercase.
    nom_reseau = models.CharField(max_length=45, db_column='NomReseau') # Field name made lowercase.
    nom_en = models.ForeignKey('Profs',max_length=150, db_column='NomEn') # Field name made lowercase.
    class Meta:
        db_table = u'laniere'

class Matiere(models.Model):
    idmatiere = models.CharField(primary_key=True,max_length=18, db_column='idMatiere') # Field name made lowercase.
    idlaniere = models.ForeignKey('Laniere',max_length=9, db_column='idLaniere') # Field name made lowercase.
    nom = models.CharField(max_length=210, db_column='Nom') # Field name made lowercase.
    annee = models.IntegerField(db_column='Annee') # Field name made lowercase.
    credits = models.FloatField(db_column='Credits') # Field name made lowercase.
    idmatiereyoratooid = models.CharField(max_length=30, db_column='idMatiereYoratooID') # Field name made lowercase.
    nomen = models.CharField(max_length=150, db_column='NomEn') # Field name made lowercase.
    class Meta:
        db_table = u'matiere'

class MessagesEleve(models.Model):
    idmessage = models.IntegerField(primary_key=True, db_column='IDMessage') # Field name made lowercase.
    message = models.CharField(max_length=765, db_column='Message') # Field name made lowercase.
    date = models.DateField(db_column='Date') # Field name made lowercase.
    annee = models.ForeignKey('Anneeuniversitaire',max_length=3, db_column='Annee') # Field name made lowercase.
    class Meta:
        db_table = u'messages_eleve'

class News(models.Model):
    id = models.IntegerField(primary_key=True,db_column='idNews')
    date = models.DateTimeField()
    title = models.CharField(max_length=765)
    link = models.CharField(max_length=765)
    description = models.TextField()
    author = models.CharField(max_length=765)
    annee = models.ForeignKey('Anneeuniversitaire',db_column='Anne')
    class Meta:
        db_table = u'news'

class Note(models.Model):
    #idnote = models.IntegerField(primary_key=True, db_column='idNote') # Field name made lowercase.
    ideleve = models.ForeignKey('Eleve',db_column='idEleve',primary_key=True) # Field name made lowercase.
    idactivite = models.ForeignKey('Activite',max_length=24, db_column='idActivite', to_field='idactivite') # Field name made lowercase.
    auteur = models.CharField(max_length=30, db_column='Auteur') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    note = models.FloatField(db_column='Note') # Field name made lowercase.
    note_norm = models.FloatField(db_column='NoteNorm') # Field name made lowercase.
    visible = models.CharField(max_length=1, db_column='Visible') # Field name made lowercase.
    processed = models.IntegerField(db_column='Processed') # Field name made lowercase.
    class Meta:
        db_table = u'note'

class Plage(models.Model):
    id = models.IntegerField(primary_key=True,db_column='idPlage')
    idplage = models.CharField(max_length=24, db_column='idPlage') # Field name made lowercase.
    annee = models.ForeignKey('Anneeuniversitaire',max_length=3, db_column='Annee') # Field name made lowercase.
    idactivite = models.ForeignKey('Activite',max_length=24, db_column='idActivite') # Field name made lowercase.
    semaine = models.IntegerField(db_column='Semaine') # Field name made lowercase.
    jour = models.IntegerField(db_column='Jour') # Field name made lowercase.
    class Meta:
        db_table = u'plage'

class Profactivite(models.Model):
    idprof = models.ForeignKey('Profs',max_length=24, db_column='idProf',primary_key=True) # Field name made lowercase.
    idactivite = models.ForeignKey('Activite',max_length=24, db_column='idActivite',primary_key=True) # Field name made lowercase.
    class Meta:
        db_table = u'profactivite'

class Profs(models.Model):
    idprof = models.IntegerField(primary_key=True,max_length=6, db_column='idProf') # Field name made lowercase.
    nom = models.CharField(max_length=60, db_column='Nom') # Field name made lowercase.
    prenom = models.CharField(max_length=45, db_column='Prenom') # Field name made lowercase.
    nom_reseau = models.CharField(max_length=45, db_column='NomReseau') # Field name made lowercase.
    mail = models.CharField(max_length=765)
    class Meta:
        db_table = u'profs'

class ResponsableLaniere(models.Model):
    nomreseau = models.CharField(max_length=45, db_column='NomReseau') # Field name made lowercase.
    idprof = models.ForeignKey('Profs',db_column='idProf',primary_key=True);
    idlaniere = models.ForeignKey('Laniere',max_length=6, db_column='idLaniere',primary_key=True) # Field name made lowercase.
    annee = models.IntegerField(db_column='Annee') # Field name made lowercase.
    class Meta:
        db_table = u'responsable_laniere'

class TypeEleve(models.Model):
    id = models.IntegerField(primary_key=True,db_column='idTypeEleve')
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    description = models.CharField(max_length=90, db_column='Description') # Field name made lowercase.
    class Meta:
        db_table = u'type_eleve'

class Typeactivite(models.Model):
    id = models.IntegerField(primary_key=True,db_column='idTypeActivite')
    type = models.CharField(max_length=3, primary_key=True, db_column='Type') # Field name made lowercase.
    nomactivite = models.CharField(max_length=60, db_column='NomActivite') # Field name made lowercase.
    class Meta:
        db_table = u'typeactivite'

class User(models.Model):
    id = models.IntegerField(primary_key=True,db_column='idUser')
    uid = models.CharField(max_length=90)
    upass = models.CharField(max_length=60)
    utype = models.CharField(max_length=6, blank=True)
    sno = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = u'user'
