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
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    action = models.TextField(db_column='Action') # Field name made lowercase.
    class Meta:
        db_table = u'LOG'

class LogEleve(models.Model):
    user = models.CharField(max_length=60)
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    class Meta:
        db_table = u'LOG_eleve'

class Absence(models.Model):
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    date = models.DateField(db_column='Date') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    class Meta:
        db_table = u'absence'

class Absence20082009(models.Model):
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    date = models.DateField(db_column='Date') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    class Meta:
        db_table = u'absence_2008_2009'

class Absence20092010(models.Model):
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    date = models.DateField(db_column='Date') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    class Meta:
        db_table = u'absence_2009_2010'

class Absence20102011(models.Model):
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    date = models.DateField(db_column='Date') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    class Meta:
        db_table = u'absence_2010_2011'

class Activite(models.Model):
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    idmatiere = models.CharField(max_length=18, db_column='idMatiere') # Field name made lowercase.
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    coefficient = models.FloatField(db_column='Coefficient') # Field name made lowercase.
    nom = models.CharField(max_length=768, db_column='Nom') # Field name made lowercase.
    nbhprevu = models.IntegerField(db_column='NbHPrevu') # Field name made lowercase.
    annee = models.CharField(max_length=3, db_column='Annee') # Field name made lowercase.
    sansnote = models.IntegerField(db_column='SansNote') # Field name made lowercase.
    notevisible = models.CharField(max_length=1, db_column='NoteVisible') # Field name made lowercase.
    semestre = models.IntegerField(db_column='Semestre') # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'activite'

class Activite20062007(models.Model):
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    idmatiere = models.CharField(max_length=18, db_column='idMatiere') # Field name made lowercase.
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    coefficient = models.FloatField(db_column='Coefficient') # Field name made lowercase.
    nom = models.CharField(max_length=120, db_column='Nom') # Field name made lowercase.
    nbhprevu = models.IntegerField(db_column='NbHPrevu') # Field name made lowercase.
    annee = models.CharField(max_length=3, db_column='Annee') # Field name made lowercase.
    sansnote = models.IntegerField(db_column='SansNote') # Field name made lowercase.
    notevisible = models.CharField(max_length=1, db_column='NoteVisible') # Field name made lowercase.
    semestre = models.IntegerField(db_column='Semestre') # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'activite_2006_2007'

class Activite20072008(models.Model):
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    idmatiere = models.CharField(max_length=18, db_column='idMatiere') # Field name made lowercase.
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    coefficient = models.FloatField(db_column='Coefficient') # Field name made lowercase.
    nom = models.CharField(max_length=120, db_column='Nom') # Field name made lowercase.
    nbhprevu = models.IntegerField(db_column='NbHPrevu') # Field name made lowercase.
    annee = models.CharField(max_length=3, db_column='Annee') # Field name made lowercase.
    sansnote = models.IntegerField(db_column='SansNote') # Field name made lowercase.
    notevisible = models.CharField(max_length=1, db_column='NoteVisible') # Field name made lowercase.
    semestre = models.IntegerField(db_column='Semestre') # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'activite_2007_2008'

class Activite20082009(models.Model):
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    idmatiere = models.CharField(max_length=18, db_column='idMatiere') # Field name made lowercase.
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    coefficient = models.FloatField(db_column='Coefficient') # Field name made lowercase.
    nom = models.CharField(max_length=120, db_column='Nom') # Field name made lowercase.
    nbhprevu = models.IntegerField(db_column='NbHPrevu') # Field name made lowercase.
    annee = models.CharField(max_length=3, db_column='Annee') # Field name made lowercase.
    sansnote = models.IntegerField(db_column='SansNote') # Field name made lowercase.
    notevisible = models.CharField(max_length=1, db_column='NoteVisible') # Field name made lowercase.
    semestre = models.IntegerField(db_column='Semestre') # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'activite_2008_2009'

class Activite20092010(models.Model):
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    idmatiere = models.CharField(max_length=18, db_column='idMatiere') # Field name made lowercase.
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    coefficient = models.FloatField(db_column='Coefficient') # Field name made lowercase.
    nom = models.CharField(max_length=120, db_column='Nom') # Field name made lowercase.
    nbhprevu = models.IntegerField(db_column='NbHPrevu') # Field name made lowercase.
    annee = models.CharField(max_length=3, db_column='Annee') # Field name made lowercase.
    sansnote = models.IntegerField(db_column='SansNote') # Field name made lowercase.
    notevisible = models.CharField(max_length=1, db_column='NoteVisible') # Field name made lowercase.
    semestre = models.IntegerField(db_column='Semestre') # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'activite_2009_2010'

class Activite20102011(models.Model):
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    idmatiere = models.CharField(max_length=18, db_column='idMatiere') # Field name made lowercase.
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    coefficient = models.FloatField(db_column='Coefficient') # Field name made lowercase.
    nom = models.CharField(max_length=120, db_column='Nom') # Field name made lowercase.
    nbhprevu = models.IntegerField(db_column='NbHPrevu') # Field name made lowercase.
    annee = models.CharField(max_length=3, db_column='Annee') # Field name made lowercase.
    sansnote = models.IntegerField(db_column='SansNote') # Field name made lowercase.
    notevisible = models.CharField(max_length=1, db_column='NoteVisible') # Field name made lowercase.
    semestre = models.IntegerField(db_column='Semestre') # Field name made lowercase.
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'activite_2010_2011'

class Admins(models.Model):
    login = models.CharField(max_length=60)
    class Meta:
        db_table = u'admins'

class Anneeuniversitaire(models.Model):
    idanneeuniversitaire = models.IntegerField(primary_key=True, db_column='idAnneeUniversitaire') # Field name made lowercase.
    datedebut = models.DateField(db_column='DateDebut') # Field name made lowercase.
    datefin = models.DateField(db_column='DateFin') # Field name made lowercase.
    nom = models.CharField(max_length=60, db_column='Nom') # Field name made lowercase.
    class Meta:
        db_table = u'anneeuniversitaire'

class BilanActivite(models.Model):
    idanneeuniversitaire = models.IntegerField(db_column='idAnneeUniversitaire') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    min = models.FloatField()
    max = models.FloatField()
    moyenne = models.FloatField()
    ecart_type = models.FloatField()
    pourcent_saisie = models.FloatField()
    class Meta:
        db_table = u'bilan_activite'

class BilanActivite20062007(models.Model):
    idanneeuniversitaire = models.IntegerField(db_column='idAnneeUniversitaire') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    min = models.FloatField()
    max = models.FloatField()
    moyenne = models.FloatField()
    ecart_type = models.FloatField()
    pourcent_saisie = models.FloatField()
    class Meta:
        db_table = u'bilan_activite_2006_2007'

class BilanActivite20072008(models.Model):
    idanneeuniversitaire = models.IntegerField(db_column='idAnneeUniversitaire') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    min = models.FloatField()
    max = models.FloatField()
    moyenne = models.FloatField()
    ecart_type = models.FloatField()
    pourcent_saisie = models.FloatField()
    class Meta:
        db_table = u'bilan_activite_2007_2008'

class BilanActivite20082009(models.Model):
    idanneeuniversitaire = models.IntegerField(db_column='idAnneeUniversitaire') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    min = models.FloatField()
    max = models.FloatField()
    moyenne = models.FloatField()
    ecart_type = models.FloatField()
    pourcent_saisie = models.FloatField()
    class Meta:
        db_table = u'bilan_activite_2008_2009'

class BilanActivite20092010(models.Model):
    idanneeuniversitaire = models.IntegerField(db_column='idAnneeUniversitaire') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    min = models.FloatField()
    max = models.FloatField()
    moyenne = models.FloatField()
    ecart_type = models.FloatField()
    pourcent_saisie = models.FloatField()
    class Meta:
        db_table = u'bilan_activite_2009_2010'

class BilanActivite20102011(models.Model):
    idanneeuniversitaire = models.IntegerField(db_column='idAnneeUniversitaire') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    min = models.FloatField()
    max = models.FloatField()
    moyenne = models.FloatField()
    ecart_type = models.FloatField()
    pourcent_saisie = models.FloatField()
    class Meta:
        db_table = u'bilan_activite_2010_2011'

class BilanEleve(models.Model):
    idbilaneleve = models.IntegerField(primary_key=True, db_column='idBilanEleve') # Field name made lowercase.
    ideleve = models.IntegerField(db_column='idEleve') # Field name made lowercase.
    idcontratpedagogique = models.IntegerField(db_column='idContratPedagogique') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenneds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficientds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyennetp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficienttp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    redoublement = models.CharField(max_length=1)
    exclusion = models.CharField(max_length=1)
    absences = models.IntegerField()
    coefficients = models.FloatField()
    coefficientdispenses = models.FloatField(db_column='coefficientDispenses') # Field name made lowercase.
    decisionjury = models.TextField(db_column='decisionJury') # Field name made lowercase.
    moyennesem1 = models.FloatField(db_column='moyenneSEM1') # Field name made lowercase.
    moyennesem2 = models.FloatField(db_column='moyenneSEM2') # Field name made lowercase.
    moyennenorm = models.FloatField(db_column='moyenneNorm') # Field name made lowercase.
    moyennenormds = models.FloatField(db_column='moyenneNormDS') # Field name made lowercase.
    moyennenormtp = models.FloatField(db_column='moyenneNormTP') # Field name made lowercase.
    ectsvalides = models.IntegerField(db_column='ectsValides') # Field name made lowercase.
    class Meta:
        db_table = u'bilan_eleve'

class BilanEleve20062007(models.Model):
    idbilaneleve = models.IntegerField(primary_key=True, db_column='idBilanEleve') # Field name made lowercase.
    ideleve = models.IntegerField(db_column='idEleve') # Field name made lowercase.
    idcontratpedagogique = models.IntegerField(db_column='idContratPedagogique') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenneds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficientds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyennetp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficienttp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    redoublement = models.CharField(max_length=1)
    exclusion = models.CharField(max_length=1)
    absences = models.IntegerField()
    coefficients = models.FloatField()
    coefficientdispenses = models.FloatField(db_column='coefficientDispenses') # Field name made lowercase.
    decisionjury = models.CharField(max_length=300, db_column='decisionJury') # Field name made lowercase.
    moyennesem1 = models.FloatField(db_column='moyenneSEM1') # Field name made lowercase.
    moyennesem2 = models.FloatField(db_column='moyenneSEM2') # Field name made lowercase.
    ectsvalides = models.IntegerField(db_column='ectsValides') # Field name made lowercase.
    class Meta:
        db_table = u'bilan_eleve_2006_2007'

class BilanEleve20072008(models.Model):
    idbilaneleve = models.IntegerField(primary_key=True, db_column='idBilanEleve') # Field name made lowercase.
    ideleve = models.IntegerField(db_column='idEleve') # Field name made lowercase.
    idcontratpedagogique = models.IntegerField(db_column='idContratPedagogique') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenneds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficientds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyennetp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficienttp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    redoublement = models.CharField(max_length=1)
    exclusion = models.CharField(max_length=1)
    absences = models.IntegerField()
    coefficients = models.FloatField()
    coefficientdispenses = models.FloatField(db_column='coefficientDispenses') # Field name made lowercase.
    decisionjury = models.TextField(db_column='decisionJury') # Field name made lowercase.
    moyennesem1 = models.FloatField(db_column='moyenneSEM1') # Field name made lowercase.
    moyennesem2 = models.FloatField(db_column='moyenneSEM2') # Field name made lowercase.
    moyennenorm = models.FloatField(db_column='moyenneNorm') # Field name made lowercase.
    moyennenormds = models.FloatField(db_column='moyenneNormDS') # Field name made lowercase.
    moyennenormtp = models.FloatField(db_column='moyenneNormTP') # Field name made lowercase.
    ectsvalides = models.IntegerField(db_column='ectsValides') # Field name made lowercase.
    class Meta:
        db_table = u'bilan_eleve_2007_2008'

class BilanEleve20082009(models.Model):
    idbilaneleve = models.IntegerField(primary_key=True, db_column='idBilanEleve') # Field name made lowercase.
    ideleve = models.IntegerField(db_column='idEleve') # Field name made lowercase.
    idcontratpedagogique = models.IntegerField(db_column='idContratPedagogique') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenneds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficientds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyennetp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficienttp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    redoublement = models.CharField(max_length=1)
    exclusion = models.CharField(max_length=1)
    absences = models.IntegerField()
    coefficients = models.FloatField()
    coefficientdispenses = models.FloatField(db_column='coefficientDispenses') # Field name made lowercase.
    decisionjury = models.TextField(db_column='decisionJury') # Field name made lowercase.
    moyennesem1 = models.FloatField(db_column='moyenneSEM1') # Field name made lowercase.
    moyennesem2 = models.FloatField(db_column='moyenneSEM2') # Field name made lowercase.
    moyennenorm = models.FloatField(db_column='moyenneNorm') # Field name made lowercase.
    moyennenormds = models.FloatField(db_column='moyenneNormDS') # Field name made lowercase.
    moyennenormtp = models.FloatField(db_column='moyenneNormTP') # Field name made lowercase.
    ectsvalides = models.IntegerField(db_column='ectsValides') # Field name made lowercase.
    class Meta:
        db_table = u'bilan_eleve_2008_2009'

class BilanEleve20092010(models.Model):
    idbilaneleve = models.IntegerField(primary_key=True, db_column='idBilanEleve') # Field name made lowercase.
    ideleve = models.IntegerField(db_column='idEleve') # Field name made lowercase.
    idcontratpedagogique = models.IntegerField(db_column='idContratPedagogique') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenneds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficientds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyennetp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficienttp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    redoublement = models.CharField(max_length=1)
    exclusion = models.CharField(max_length=1)
    absences = models.IntegerField()
    coefficients = models.FloatField()
    coefficientdispenses = models.FloatField(db_column='coefficientDispenses') # Field name made lowercase.
    decisionjury = models.TextField(db_column='decisionJury') # Field name made lowercase.
    moyennesem1 = models.FloatField(db_column='moyenneSEM1') # Field name made lowercase.
    moyennesem2 = models.FloatField(db_column='moyenneSEM2') # Field name made lowercase.
    moyennenorm = models.FloatField(db_column='moyenneNorm') # Field name made lowercase.
    moyennenormds = models.FloatField(db_column='moyenneNormDS') # Field name made lowercase.
    moyennenormtp = models.FloatField(db_column='moyenneNormTP') # Field name made lowercase.
    ectsvalides = models.IntegerField(db_column='ectsValides') # Field name made lowercase.
    class Meta:
        db_table = u'bilan_eleve_2009_2010'

class BilanEleve20102011(models.Model):
    idbilaneleve = models.IntegerField(primary_key=True, db_column='idBilanEleve') # Field name made lowercase.
    ideleve = models.IntegerField(db_column='idEleve') # Field name made lowercase.
    idcontratpedagogique = models.IntegerField(db_column='idContratPedagogique') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenneds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficientds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyennetp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficienttp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    redoublement = models.CharField(max_length=1)
    exclusion = models.CharField(max_length=1)
    absences = models.IntegerField()
    coefficients = models.FloatField()
    coefficientdispenses = models.FloatField(db_column='coefficientDispenses') # Field name made lowercase.
    decisionjury = models.TextField(db_column='decisionJury') # Field name made lowercase.
    moyennesem1 = models.FloatField(db_column='moyenneSEM1') # Field name made lowercase.
    moyennesem2 = models.FloatField(db_column='moyenneSEM2') # Field name made lowercase.
    moyennenorm = models.FloatField(db_column='moyenneNorm') # Field name made lowercase.
    moyennenormds = models.FloatField(db_column='moyenneNormDS') # Field name made lowercase.
    moyennenormtp = models.FloatField(db_column='moyenneNormTP') # Field name made lowercase.
    ectsvalides = models.IntegerField(db_column='ectsValides') # Field name made lowercase.
    class Meta:
        db_table = u'bilan_eleve_2010_2011'

class BilanLaniere(models.Model):
    idbilanlaniere = models.IntegerField(primary_key=True, db_column='idBilanLaniere') # Field name made lowercase.
    ideleve = models.IntegerField(db_column='idEleve') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenneds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficientds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyennetp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficienttp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    idlaniere = models.CharField(max_length=9, db_column='idLaniere') # Field name made lowercase.
    qualification = models.CharField(max_length=3)
    rattrapage = models.CharField(max_length=1)
    ectsvalides = models.IntegerField(db_column='ectsValides') # Field name made lowercase.
    class Meta:
        db_table = u'bilan_laniere'

class BilanLaniere20062007(models.Model):
    idbilanlaniere = models.IntegerField(primary_key=True, db_column='idBilanLaniere') # Field name made lowercase.
    ideleve = models.IntegerField(db_column='idEleve') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenneds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficientds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyennetp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficienttp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    idlaniere = models.CharField(max_length=6, db_column='idLaniere') # Field name made lowercase.
    qualification = models.CharField(max_length=3)
    rattrapage = models.CharField(max_length=1)
    class Meta:
        db_table = u'bilan_laniere_2006_2007'

class BilanLaniere20072008(models.Model):
    idbilanlaniere = models.IntegerField(primary_key=True, db_column='idBilanLaniere') # Field name made lowercase.
    ideleve = models.IntegerField(db_column='idEleve') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenneds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficientds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyennetp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficienttp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    idlaniere = models.CharField(max_length=6, db_column='idLaniere') # Field name made lowercase.
    qualification = models.CharField(max_length=3)
    rattrapage = models.CharField(max_length=1)
    ectsvalides = models.IntegerField(db_column='ectsValides') # Field name made lowercase.
    class Meta:
        db_table = u'bilan_laniere_2007_2008'

class BilanLaniere20082009(models.Model):
    idbilanlaniere = models.IntegerField(primary_key=True, db_column='idBilanLaniere') # Field name made lowercase.
    ideleve = models.IntegerField(db_column='idEleve') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenneds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficientds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyennetp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficienttp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    idlaniere = models.CharField(max_length=6, db_column='idLaniere') # Field name made lowercase.
    qualification = models.CharField(max_length=3)
    rattrapage = models.CharField(max_length=1)
    ectsvalides = models.IntegerField(db_column='ectsValides') # Field name made lowercase.
    class Meta:
        db_table = u'bilan_laniere_2008_2009'

class BilanLaniere20092010(models.Model):
    idbilanlaniere = models.IntegerField(primary_key=True, db_column='idBilanLaniere') # Field name made lowercase.
    ideleve = models.IntegerField(db_column='idEleve') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenneds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficientds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyennetp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficienttp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    idlaniere = models.CharField(max_length=6, db_column='idLaniere') # Field name made lowercase.
    qualification = models.CharField(max_length=3)
    rattrapage = models.CharField(max_length=1)
    ectsvalides = models.IntegerField(db_column='ectsValides') # Field name made lowercase.
    class Meta:
        db_table = u'bilan_laniere_2009_2010'

class BilanLaniere20102011(models.Model):
    idbilanlaniere = models.IntegerField(primary_key=True, db_column='idBilanLaniere') # Field name made lowercase.
    ideleve = models.IntegerField(db_column='idEleve') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenneds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficientds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyennetp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficienttp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    idlaniere = models.CharField(max_length=6, db_column='idLaniere') # Field name made lowercase.
    qualification = models.CharField(max_length=3)
    rattrapage = models.CharField(max_length=1)
    ectsvalides = models.IntegerField(db_column='ectsValides') # Field name made lowercase.
    class Meta:
        db_table = u'bilan_laniere_2010_2011'

class BilanMatiere(models.Model):
    idbilanmatiere = models.IntegerField(primary_key=True, db_column='idBilanMatiere') # Field name made lowercase.
    ideleve = models.IntegerField(db_column='idEleve') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenneds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficientds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyennetp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficienttp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    idmatiere = models.CharField(max_length=18, db_column='idMatiere') # Field name made lowercase.
    qualification = models.CharField(max_length=3)
    class Meta:
        db_table = u'bilan_matiere'

class BilanMatiere20072008(models.Model):
    idbilanmatiere = models.IntegerField(primary_key=True, db_column='idBilanMatiere') # Field name made lowercase.
    ideleve = models.IntegerField(db_column='idEleve') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenneds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficientds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyennetp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficienttp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    idmatiere = models.CharField(max_length=18, db_column='idMatiere') # Field name made lowercase.
    qualification = models.CharField(max_length=3)
    class Meta:
        db_table = u'bilan_matiere_2007_2008'

class BilanMatiere20082009(models.Model):
    idbilanmatiere = models.IntegerField(primary_key=True, db_column='idBilanMatiere') # Field name made lowercase.
    ideleve = models.IntegerField(db_column='idEleve') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenneds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficientds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyennetp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficienttp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    idmatiere = models.CharField(max_length=18, db_column='idMatiere') # Field name made lowercase.
    qualification = models.CharField(max_length=3)
    class Meta:
        db_table = u'bilan_matiere_2008_2009'

class BilanMatiere20092010(models.Model):
    idbilanmatiere = models.IntegerField(primary_key=True, db_column='idBilanMatiere') # Field name made lowercase.
    ideleve = models.IntegerField(db_column='idEleve') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenneds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficientds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyennetp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficienttp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    idmatiere = models.CharField(max_length=18, db_column='idMatiere') # Field name made lowercase.
    qualification = models.CharField(max_length=3)
    class Meta:
        db_table = u'bilan_matiere_2009_2010'

class BilanMatiere20102011(models.Model):
    idbilanmatiere = models.IntegerField(primary_key=True, db_column='idBilanMatiere') # Field name made lowercase.
    ideleve = models.IntegerField(db_column='idEleve') # Field name made lowercase.
    moyenne = models.FloatField()
    moyenneds = models.FloatField(db_column='moyenneDS') # Field name made lowercase.
    coefficientds = models.FloatField(db_column='coefficientDS') # Field name made lowercase.
    moyennetp = models.FloatField(db_column='moyenneTP') # Field name made lowercase.
    coefficienttp = models.FloatField(db_column='coefficientTP') # Field name made lowercase.
    classement = models.IntegerField()
    nbeleves = models.IntegerField(db_column='nbEleves') # Field name made lowercase.
    idmatiere = models.CharField(max_length=18, db_column='idMatiere') # Field name made lowercase.
    qualification = models.CharField(max_length=3)
    class Meta:
        db_table = u'bilan_matiere_2010_2011'

class Contenucontratpedagogique(models.Model):
    idcontratpedagogique = models.FloatField(db_column='idContratPedagogique') # Field name made lowercase.
    idmatiereyoratooid = models.CharField(max_length=30, db_column='idMatiereYoratooID') # Field name made lowercase.
    coefficient = models.FloatField(db_column='Coefficient') # Field name made lowercase.
    class Meta:
        db_table = u'contenucontratpedagogique'

class Contenucontratpedagogique20062007(models.Model):
    idcontratpedagogique = models.FloatField(db_column='idContratPedagogique') # Field name made lowercase.
    idmatiereyoratooid = models.CharField(max_length=30, db_column='idMatiereYoratooID') # Field name made lowercase.
    coefficient = models.FloatField(db_column='Coefficient') # Field name made lowercase.
    class Meta:
        db_table = u'contenucontratpedagogique_2006_2007'

class Contenucontratpedagogique20072008(models.Model):
    idcontratpedagogique = models.FloatField(db_column='idContratPedagogique') # Field name made lowercase.
    idmatiereyoratooid = models.CharField(max_length=30, db_column='idMatiereYoratooID') # Field name made lowercase.
    coefficient = models.FloatField(db_column='Coefficient') # Field name made lowercase.
    class Meta:
        db_table = u'contenucontratpedagogique_2007_2008'

class Contenucontratpedagogique20082009(models.Model):
    idcontratpedagogique = models.FloatField(db_column='idContratPedagogique') # Field name made lowercase.
    idmatiereyoratooid = models.CharField(max_length=30, db_column='idMatiereYoratooID') # Field name made lowercase.
    coefficient = models.FloatField(db_column='Coefficient') # Field name made lowercase.
    class Meta:
        db_table = u'contenucontratpedagogique_2008_2009'

class Contenucontratpedagogique20092010(models.Model):
    idcontratpedagogique = models.FloatField(db_column='idContratPedagogique') # Field name made lowercase.
    idmatiereyoratooid = models.CharField(max_length=30, db_column='idMatiereYoratooID') # Field name made lowercase.
    coefficient = models.FloatField(db_column='Coefficient') # Field name made lowercase.
    class Meta:
        db_table = u'contenucontratpedagogique_2009_2010'

class Contenucontratpedagogique20102011(models.Model):
    idcontratpedagogique = models.FloatField(db_column='idContratPedagogique') # Field name made lowercase.
    idmatiereyoratooid = models.CharField(max_length=30, db_column='idMatiereYoratooID') # Field name made lowercase.
    coefficient = models.FloatField(db_column='Coefficient') # Field name made lowercase.
    class Meta:
        db_table = u'contenucontratpedagogique_2010_2011'

class Contratpedagogique(models.Model):
    idcontratpedagogique = models.FloatField(primary_key=True, db_column='idContratPedagogique') # Field name made lowercase.
    idanneeuniversitaire = models.IntegerField(db_column='idAnneeUniversitaire') # Field name made lowercase.
    idepoque = models.IntegerField(db_column='idEpoque') # Field name made lowercase.
    credits = models.FloatField(db_column='Credits') # Field name made lowercase.
    nom = models.CharField(max_length=60, db_column='Nom') # Field name made lowercase.
    class Meta:
        db_table = u'contratpedagogique'

class Contratpedagogique20062007(models.Model):
    idcontratpedagogique = models.FloatField(primary_key=True, db_column='idContratPedagogique') # Field name made lowercase.
    idanneeuniversitaire = models.IntegerField(db_column='idAnneeUniversitaire') # Field name made lowercase.
    idepoque = models.IntegerField(db_column='idEpoque') # Field name made lowercase.
    credits = models.FloatField(db_column='Credits') # Field name made lowercase.
    nom = models.CharField(max_length=60, db_column='Nom') # Field name made lowercase.
    class Meta:
        db_table = u'contratpedagogique_2006_2007'

class Contratpedagogique20072008(models.Model):
    idcontratpedagogique = models.FloatField(primary_key=True, db_column='idContratPedagogique') # Field name made lowercase.
    idanneeuniversitaire = models.IntegerField(db_column='idAnneeUniversitaire') # Field name made lowercase.
    idepoque = models.IntegerField(db_column='idEpoque') # Field name made lowercase.
    credits = models.FloatField(db_column='Credits') # Field name made lowercase.
    nom = models.CharField(max_length=60, db_column='Nom') # Field name made lowercase.
    class Meta:
        db_table = u'contratpedagogique_2007_2008'

class Contratpedagogique20082009(models.Model):
    idcontratpedagogique = models.FloatField(primary_key=True, db_column='idContratPedagogique') # Field name made lowercase.
    idanneeuniversitaire = models.IntegerField(db_column='idAnneeUniversitaire') # Field name made lowercase.
    idepoque = models.IntegerField(db_column='idEpoque') # Field name made lowercase.
    credits = models.FloatField(db_column='Credits') # Field name made lowercase.
    nom = models.CharField(max_length=60, db_column='Nom') # Field name made lowercase.
    class Meta:
        db_table = u'contratpedagogique_2008_2009'

class Contratpedagogique20092010(models.Model):
    idcontratpedagogique = models.FloatField(primary_key=True, db_column='idContratPedagogique') # Field name made lowercase.
    idanneeuniversitaire = models.IntegerField(db_column='idAnneeUniversitaire') # Field name made lowercase.
    idepoque = models.IntegerField(db_column='idEpoque') # Field name made lowercase.
    credits = models.FloatField(db_column='Credits') # Field name made lowercase.
    nom = models.CharField(max_length=60, db_column='Nom') # Field name made lowercase.
    class Meta:
        db_table = u'contratpedagogique_2009_2010'

class Contratpedagogique20102011(models.Model):
    idcontratpedagogique = models.FloatField(primary_key=True, db_column='idContratPedagogique') # Field name made lowercase.
    idanneeuniversitaire = models.IntegerField(db_column='idAnneeUniversitaire') # Field name made lowercase.
    idepoque = models.IntegerField(db_column='idEpoque') # Field name made lowercase.
    credits = models.FloatField(db_column='Credits') # Field name made lowercase.
    nom = models.CharField(max_length=60, db_column='Nom') # Field name made lowercase.
    class Meta:
        db_table = u'contratpedagogique_2010_2011'

class CoursEleve(models.Model):
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    class Meta:
        db_table = u'cours_eleve'

class CoursEleve20082009(models.Model):
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    class Meta:
        db_table = u'cours_eleve_2008_2009'

class CoursEleve20092010(models.Model):
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    class Meta:
        db_table = u'cours_eleve_2009_2010'

class CoursEleve20102011(models.Model):
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    class Meta:
        db_table = u'cours_eleve_2010_2011'

class CreditsEtranger(models.Model):
    ideleve = models.FloatField(primary_key=True, db_column='idEleve') # Field name made lowercase.
    credits = models.IntegerField()
    etablissement = models.CharField(max_length=120)
    auteur = models.CharField(max_length=30, db_column='Auteur') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    class Meta:
        db_table = u'credits_etranger'

class Dispense(models.Model):
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    auteur = models.CharField(max_length=30, db_column='Auteur') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    raison = models.CharField(max_length=120, db_column='Raison') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    class Meta:
        db_table = u'dispense'

class Dispense20062007(models.Model):
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    auteur = models.CharField(max_length=30, db_column='Auteur') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    raison = models.CharField(max_length=120, db_column='Raison') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    class Meta:
        db_table = u'dispense_2006_2007'

class Dispense20072008(models.Model):
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    auteur = models.CharField(max_length=30, db_column='Auteur') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    raison = models.CharField(max_length=120, db_column='Raison') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    class Meta:
        db_table = u'dispense_2007_2008'

class Dispense20082009(models.Model):
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    auteur = models.CharField(max_length=30, db_column='Auteur') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    raison = models.CharField(max_length=120, db_column='Raison') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    class Meta:
        db_table = u'dispense_2008_2009'

class Dispense20092010(models.Model):
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    auteur = models.CharField(max_length=30, db_column='Auteur') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    raison = models.CharField(max_length=120, db_column='Raison') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    class Meta:
        db_table = u'dispense_2009_2010'

class Dispense20102011(models.Model):
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    auteur = models.CharField(max_length=30, db_column='Auteur') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    raison = models.CharField(max_length=120, db_column='Raison') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    class Meta:
        db_table = u'dispense_2010_2011'

class Eleve(models.Model):
    ideleve = models.FloatField(primary_key=True, db_column='idEleve') # Field name made lowercase.
    nom = models.CharField(max_length=120, db_column='Nom') # Field name made lowercase.
    nomreseau = models.CharField(max_length=90, db_column='NomReseau') # Field name made lowercase.
    binomes1 = models.IntegerField(db_column='Binomes1') # Field name made lowercase.
    binomes2 = models.IntegerField(db_column='Binomes2') # Field name made lowercase.
    binomes3 = models.IntegerField(db_column='Binomes3') # Field name made lowercase.
    annee = models.IntegerField(db_column='Annee') # Field name made lowercase.
    groupe = models.IntegerField(db_column='Groupe') # Field name made lowercase.
    echange = models.CharField(max_length=3, db_column='Echange') # Field name made lowercase.
    datenaissance = models.DateField(db_column='DateNaissance') # Field name made lowercase.
    origine = models.CharField(max_length=3, db_column='Origine') # Field name made lowercase.
    mail = models.CharField(max_length=150)
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    tuteur = models.CharField(max_length=6, db_column='Tuteur') # Field name made lowercase.
    class Meta:
        db_table = u'eleve'

class Eleve20062007(models.Model):
    ideleve = models.FloatField(primary_key=True, db_column='idEleve') # Field name made lowercase.
    nom = models.CharField(max_length=120, db_column='Nom') # Field name made lowercase.
    nomreseau = models.CharField(max_length=90, db_column='NomReseau') # Field name made lowercase.
    binomes1 = models.IntegerField(db_column='Binomes1') # Field name made lowercase.
    binomes2 = models.IntegerField(db_column='Binomes2') # Field name made lowercase.
    binomes3 = models.IntegerField(db_column='Binomes3') # Field name made lowercase.
    annee = models.IntegerField(db_column='Annee') # Field name made lowercase.
    groupe = models.IntegerField(db_column='Groupe') # Field name made lowercase.
    echange = models.CharField(max_length=3, db_column='Echange') # Field name made lowercase.
    datenaissance = models.DateField(db_column='DateNaissance') # Field name made lowercase.
    origine = models.CharField(max_length=3, db_column='Origine') # Field name made lowercase.
    mail = models.CharField(max_length=150)
    class Meta:
        db_table = u'eleve_2006_2007'

class Eleve20072008(models.Model):
    ideleve = models.FloatField(primary_key=True, db_column='idEleve') # Field name made lowercase.
    nom = models.CharField(max_length=120, db_column='Nom') # Field name made lowercase.
    nomreseau = models.CharField(max_length=90, db_column='NomReseau') # Field name made lowercase.
    binomes1 = models.IntegerField(db_column='Binomes1') # Field name made lowercase.
    binomes2 = models.IntegerField(db_column='Binomes2') # Field name made lowercase.
    binomes3 = models.IntegerField(db_column='Binomes3') # Field name made lowercase.
    annee = models.IntegerField(db_column='Annee') # Field name made lowercase.
    groupe = models.IntegerField(db_column='Groupe') # Field name made lowercase.
    echange = models.CharField(max_length=3, db_column='Echange') # Field name made lowercase.
    datenaissance = models.DateField(db_column='DateNaissance') # Field name made lowercase.
    origine = models.CharField(max_length=3, db_column='Origine') # Field name made lowercase.
    mail = models.CharField(max_length=150)
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    tuteur = models.CharField(max_length=6, db_column='Tuteur') # Field name made lowercase.
    class Meta:
        db_table = u'eleve_2007_2008'

class Eleve20082009(models.Model):
    ideleve = models.FloatField(primary_key=True, db_column='idEleve') # Field name made lowercase.
    nom = models.CharField(max_length=120, db_column='Nom') # Field name made lowercase.
    nomreseau = models.CharField(max_length=90, db_column='NomReseau') # Field name made lowercase.
    binomes1 = models.IntegerField(db_column='Binomes1') # Field name made lowercase.
    binomes2 = models.IntegerField(db_column='Binomes2') # Field name made lowercase.
    binomes3 = models.IntegerField(db_column='Binomes3') # Field name made lowercase.
    annee = models.IntegerField(db_column='Annee') # Field name made lowercase.
    groupe = models.IntegerField(db_column='Groupe') # Field name made lowercase.
    echange = models.CharField(max_length=3, db_column='Echange') # Field name made lowercase.
    datenaissance = models.DateField(db_column='DateNaissance') # Field name made lowercase.
    origine = models.CharField(max_length=3, db_column='Origine') # Field name made lowercase.
    mail = models.CharField(max_length=150)
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    tuteur = models.CharField(max_length=6, db_column='Tuteur') # Field name made lowercase.
    class Meta:
        db_table = u'eleve_2008_2009'

class Eleve20092010(models.Model):
    ideleve = models.FloatField(primary_key=True, db_column='idEleve') # Field name made lowercase.
    nom = models.CharField(max_length=120, db_column='Nom') # Field name made lowercase.
    nomreseau = models.CharField(max_length=90, db_column='NomReseau') # Field name made lowercase.
    binomes1 = models.IntegerField(db_column='Binomes1') # Field name made lowercase.
    binomes2 = models.IntegerField(db_column='Binomes2') # Field name made lowercase.
    binomes3 = models.IntegerField(db_column='Binomes3') # Field name made lowercase.
    annee = models.IntegerField(db_column='Annee') # Field name made lowercase.
    groupe = models.IntegerField(db_column='Groupe') # Field name made lowercase.
    echange = models.CharField(max_length=3, db_column='Echange') # Field name made lowercase.
    datenaissance = models.DateField(db_column='DateNaissance') # Field name made lowercase.
    origine = models.CharField(max_length=3, db_column='Origine') # Field name made lowercase.
    mail = models.CharField(max_length=150)
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    tuteur = models.CharField(max_length=6, db_column='Tuteur') # Field name made lowercase.
    class Meta:
        db_table = u'eleve_2009_2010'

class Eleve20102011(models.Model):
    ideleve = models.FloatField(primary_key=True, db_column='idEleve') # Field name made lowercase.
    nom = models.CharField(max_length=120, db_column='Nom') # Field name made lowercase.
    nomreseau = models.CharField(max_length=90, db_column='NomReseau') # Field name made lowercase.
    binomes1 = models.IntegerField(db_column='Binomes1') # Field name made lowercase.
    binomes2 = models.IntegerField(db_column='Binomes2') # Field name made lowercase.
    binomes3 = models.IntegerField(db_column='Binomes3') # Field name made lowercase.
    annee = models.IntegerField(db_column='Annee') # Field name made lowercase.
    groupe = models.IntegerField(db_column='Groupe') # Field name made lowercase.
    echange = models.CharField(max_length=3, db_column='Echange') # Field name made lowercase.
    datenaissance = models.DateField(db_column='DateNaissance') # Field name made lowercase.
    origine = models.CharField(max_length=3, db_column='Origine') # Field name made lowercase.
    mail = models.CharField(max_length=150)
    type = models.CharField(max_length=3, db_column='Type') # Field name made lowercase.
    tuteur = models.CharField(max_length=6, db_column='Tuteur') # Field name made lowercase.
    class Meta:
        db_table = u'eleve_2010_2011'

class Epoque(models.Model):
    idepoque = models.IntegerField(primary_key=True, db_column='idEpoque') # Field name made lowercase.
    nom = models.CharField(max_length=60, db_column='Nom') # Field name made lowercase.
    annee = models.IntegerField(db_column='Annee') # Field name made lowercase.
    semestre = models.IntegerField(db_column='Semestre') # Field name made lowercase.
    class Meta:
        db_table = u'epoque'

class EtudiantContratpedagogique(models.Model):
    ideleve = models.FloatField(primary_key=True, db_column='idEleve') # Field name made lowercase.
    idcontratpedagogique = models.FloatField(db_column='idContratPedagogique') # Field name made lowercase.
    valide = models.CharField(max_length=1, db_column='Valide') # Field name made lowercase.
    classementvisible = models.IntegerField(db_column='ClassementVisible') # Field name made lowercase.
    class Meta:
        db_table = u'etudiant_contratpedagogique'

class EtudiantContratpedagogique20062007(models.Model):
    ideleve = models.FloatField(primary_key=True, db_column='idEleve') # Field name made lowercase.
    idcontratpedagogique = models.FloatField(db_column='idContratPedagogique') # Field name made lowercase.
    valide = models.CharField(max_length=1, db_column='Valide') # Field name made lowercase.
    classementvisible = models.IntegerField(db_column='ClassementVisible') # Field name made lowercase.
    class Meta:
        db_table = u'etudiant_contratpedagogique_2006_2007'

class EtudiantContratpedagogique20072008(models.Model):
    ideleve = models.FloatField(primary_key=True, db_column='idEleve') # Field name made lowercase.
    idcontratpedagogique = models.FloatField(db_column='idContratPedagogique') # Field name made lowercase.
    valide = models.CharField(max_length=1, db_column='Valide') # Field name made lowercase.
    classementvisible = models.IntegerField(db_column='ClassementVisible') # Field name made lowercase.
    class Meta:
        db_table = u'etudiant_contratpedagogique_2007_2008'

class EtudiantContratpedagogique20082009(models.Model):
    ideleve = models.FloatField(primary_key=True, db_column='idEleve') # Field name made lowercase.
    idcontratpedagogique = models.FloatField(db_column='idContratPedagogique') # Field name made lowercase.
    valide = models.CharField(max_length=1, db_column='Valide') # Field name made lowercase.
    classementvisible = models.IntegerField(db_column='ClassementVisible') # Field name made lowercase.
    class Meta:
        db_table = u'etudiant_contratpedagogique_2008_2009'

class EtudiantContratpedagogique20092010(models.Model):
    ideleve = models.FloatField(primary_key=True, db_column='idEleve') # Field name made lowercase.
    idcontratpedagogique = models.FloatField(db_column='idContratPedagogique') # Field name made lowercase.
    valide = models.CharField(max_length=1, db_column='Valide') # Field name made lowercase.
    classementvisible = models.IntegerField(db_column='ClassementVisible') # Field name made lowercase.
    class Meta:
        db_table = u'etudiant_contratpedagogique_2009_2010'

class EtudiantContratpedagogique20102011(models.Model):
    ideleve = models.FloatField(primary_key=True, db_column='idEleve') # Field name made lowercase.
    idcontratpedagogique = models.FloatField(db_column='idContratPedagogique') # Field name made lowercase.
    valide = models.CharField(max_length=1, db_column='Valide') # Field name made lowercase.
    classementvisible = models.IntegerField(db_column='ClassementVisible') # Field name made lowercase.
    class Meta:
        db_table = u'etudiant_contratpedagogique_2010_2011'

class Laniere(models.Model):
    idlaniere = models.CharField(max_length=9, db_column='idLaniere') # Field name made lowercase.
    nom = models.CharField(max_length=78, db_column='Nom') # Field name made lowercase.
    barreds = models.FloatField(db_column='BarreDS') # Field name made lowercase.
    barretp = models.FloatField(db_column='BarreTP') # Field name made lowercase.
    barregenerale = models.FloatField(db_column='BarreGenerale') # Field name made lowercase.
    nomreseau = models.CharField(max_length=45, db_column='NomReseau') # Field name made lowercase.
    nomen = models.CharField(max_length=150, db_column='NomEn') # Field name made lowercase.
    class Meta:
        db_table = u'laniere'

class Laniere20072008(models.Model):
    idlaniere = models.CharField(max_length=6, db_column='idLaniere') # Field name made lowercase.
    nom = models.CharField(max_length=78, db_column='Nom') # Field name made lowercase.
    barreds = models.FloatField(db_column='BarreDS') # Field name made lowercase.
    barretp = models.FloatField(db_column='BarreTP') # Field name made lowercase.
    barregenerale = models.FloatField(db_column='BarreGenerale') # Field name made lowercase.
    nomreseau = models.CharField(max_length=45, db_column='NomReseau') # Field name made lowercase.
    nomen = models.CharField(max_length=150, db_column='NomEn') # Field name made lowercase.
    class Meta:
        db_table = u'laniere_2007_2008'

class Laniere20082009(models.Model):
    idlaniere = models.CharField(max_length=6, db_column='idLaniere') # Field name made lowercase.
    nom = models.CharField(max_length=78, db_column='Nom') # Field name made lowercase.
    barreds = models.FloatField(db_column='BarreDS') # Field name made lowercase.
    barretp = models.FloatField(db_column='BarreTP') # Field name made lowercase.
    barregenerale = models.FloatField(db_column='BarreGenerale') # Field name made lowercase.
    nomreseau = models.CharField(max_length=45, db_column='NomReseau') # Field name made lowercase.
    nomen = models.CharField(max_length=150, db_column='NomEn') # Field name made lowercase.
    class Meta:
        db_table = u'laniere_2008_2009'

class Laniere20092010(models.Model):
    idlaniere = models.CharField(max_length=6, db_column='idLaniere') # Field name made lowercase.
    nom = models.CharField(max_length=78, db_column='Nom') # Field name made lowercase.
    barreds = models.FloatField(db_column='BarreDS') # Field name made lowercase.
    barretp = models.FloatField(db_column='BarreTP') # Field name made lowercase.
    barregenerale = models.FloatField(db_column='BarreGenerale') # Field name made lowercase.
    nomreseau = models.CharField(max_length=45, db_column='NomReseau') # Field name made lowercase.
    nomen = models.CharField(max_length=150, db_column='NomEn') # Field name made lowercase.
    class Meta:
        db_table = u'laniere_2009_2010'

class Laniere20102011(models.Model):
    idlaniere = models.CharField(max_length=6, db_column='idLaniere') # Field name made lowercase.
    nom = models.CharField(max_length=120, db_column='Nom') # Field name made lowercase.
    barreds = models.FloatField(db_column='BarreDS') # Field name made lowercase.
    barretp = models.FloatField(db_column='BarreTP') # Field name made lowercase.
    barregenerale = models.FloatField(db_column='BarreGenerale') # Field name made lowercase.
    nomreseau = models.CharField(max_length=45, db_column='NomReseau') # Field name made lowercase.
    nomen = models.CharField(max_length=150, db_column='NomEn') # Field name made lowercase.
    class Meta:
        db_table = u'laniere_2010_2011'

class Matiere(models.Model):
    idmatiere = models.CharField(max_length=18, db_column='idMatiere') # Field name made lowercase.
    idlaniere = models.CharField(max_length=9, db_column='idLaniere') # Field name made lowercase.
    nom = models.CharField(max_length=210, db_column='Nom') # Field name made lowercase.
    annee = models.IntegerField(db_column='Annee') # Field name made lowercase.
    credits = models.FloatField(db_column='Credits') # Field name made lowercase.
    idmatiereyoratooid = models.CharField(max_length=30, db_column='idMatiereYoratooID') # Field name made lowercase.
    nomen = models.CharField(max_length=150, db_column='NomEn') # Field name made lowercase.
    class Meta:
        db_table = u'matiere'

class Matiere20062007(models.Model):
    idmatiere = models.CharField(max_length=18, db_column='idMatiere') # Field name made lowercase.
    idlaniere = models.CharField(max_length=6, db_column='idLaniere') # Field name made lowercase.
    nom = models.CharField(max_length=210, db_column='Nom') # Field name made lowercase.
    annee = models.IntegerField(db_column='Annee') # Field name made lowercase.
    credits = models.FloatField(db_column='Credits') # Field name made lowercase.
    idmatiereyoratooid = models.CharField(max_length=30, db_column='idMatiereYoratooID') # Field name made lowercase.
    class Meta:
        db_table = u'matiere_2006_2007'

class Matiere20072008(models.Model):
    idmatiere = models.CharField(max_length=18, db_column='idMatiere') # Field name made lowercase.
    idlaniere = models.CharField(max_length=6, db_column='idLaniere') # Field name made lowercase.
    nom = models.CharField(max_length=210, db_column='Nom') # Field name made lowercase.
    annee = models.IntegerField(db_column='Annee') # Field name made lowercase.
    credits = models.FloatField(db_column='Credits') # Field name made lowercase.
    idmatiereyoratooid = models.CharField(max_length=30, db_column='idMatiereYoratooID') # Field name made lowercase.
    nomen = models.CharField(max_length=150, db_column='NomEn') # Field name made lowercase.
    class Meta:
        db_table = u'matiere_2007_2008'

class Matiere20082009(models.Model):
    idmatiere = models.CharField(max_length=18, db_column='idMatiere') # Field name made lowercase.
    idlaniere = models.CharField(max_length=6, db_column='idLaniere') # Field name made lowercase.
    nom = models.CharField(max_length=210, db_column='Nom') # Field name made lowercase.
    annee = models.IntegerField(db_column='Annee') # Field name made lowercase.
    credits = models.FloatField(db_column='Credits') # Field name made lowercase.
    idmatiereyoratooid = models.CharField(max_length=30, db_column='idMatiereYoratooID') # Field name made lowercase.
    nomen = models.CharField(max_length=150, db_column='NomEn', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'matiere_2008_2009'

class Matiere20092010(models.Model):
    idmatiere = models.CharField(max_length=18, db_column='idMatiere') # Field name made lowercase.
    idlaniere = models.CharField(max_length=6, db_column='idLaniere') # Field name made lowercase.
    nom = models.CharField(max_length=210, db_column='Nom') # Field name made lowercase.
    annee = models.IntegerField(db_column='Annee') # Field name made lowercase.
    credits = models.FloatField(db_column='Credits') # Field name made lowercase.
    idmatiereyoratooid = models.CharField(max_length=30, db_column='idMatiereYoratooID') # Field name made lowercase.
    nomen = models.CharField(max_length=150, db_column='NomEn', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'matiere_2009_2010'

class Matiere20102011(models.Model):
    idmatiere = models.CharField(max_length=18, db_column='idMatiere') # Field name made lowercase.
    idlaniere = models.CharField(max_length=6, db_column='idLaniere') # Field name made lowercase.
    nom = models.CharField(max_length=210, db_column='Nom') # Field name made lowercase.
    annee = models.IntegerField(db_column='Annee') # Field name made lowercase.
    credits = models.FloatField(db_column='Credits') # Field name made lowercase.
    idmatiereyoratooid = models.CharField(max_length=30, db_column='idMatiereYoratooID') # Field name made lowercase.
    nomen = models.CharField(max_length=150, db_column='NomEn') # Field name made lowercase.
    class Meta:
        db_table = u'matiere_2010_2011'

class MessagesEleve(models.Model):
    idmessage = models.IntegerField(primary_key=True, db_column='IDMessage') # Field name made lowercase.
    message = models.CharField(max_length=765, db_column='Message') # Field name made lowercase.
    date = models.DateField(db_column='Date') # Field name made lowercase.
    annee = models.CharField(max_length=3, db_column='Annee') # Field name made lowercase.
    class Meta:
        db_table = u'messages_eleve'

class News(models.Model):
    date = models.DateTimeField(primary_key=True)
    title = models.CharField(max_length=765)
    link = models.CharField(max_length=765)
    description = models.TextField()
    author = models.CharField(max_length=765)
    annee = models.IntegerField()
    class Meta:
        db_table = u'news'

class Note(models.Model):
    idnote = models.IntegerField(primary_key=True, db_column='idNote') # Field name made lowercase.
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    auteur = models.CharField(max_length=30, db_column='Auteur') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    note = models.FloatField(db_column='Note') # Field name made lowercase.
    notenorm = models.FloatField(db_column='NoteNorm') # Field name made lowercase.
    visible = models.CharField(max_length=1, db_column='Visible') # Field name made lowercase.
    processed = models.IntegerField(db_column='Processed') # Field name made lowercase.
    class Meta:
        db_table = u'note'

class Note20062007(models.Model):
    idnote = models.IntegerField(primary_key=True, db_column='idNote') # Field name made lowercase.
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    auteur = models.CharField(max_length=30, db_column='Auteur') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    note = models.FloatField(db_column='Note') # Field name made lowercase.
    notenorm = models.FloatField(db_column='NoteNorm') # Field name made lowercase.
    visible = models.CharField(max_length=1, db_column='Visible') # Field name made lowercase.
    processed = models.IntegerField(db_column='Processed') # Field name made lowercase.
    class Meta:
        db_table = u'note_2006_2007'

class Note20072008(models.Model):
    idnote = models.IntegerField(primary_key=True, db_column='idNote') # Field name made lowercase.
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    auteur = models.CharField(max_length=30, db_column='Auteur') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    note = models.FloatField(db_column='Note') # Field name made lowercase.
    notenorm = models.FloatField(db_column='NoteNorm') # Field name made lowercase.
    visible = models.CharField(max_length=1, db_column='Visible') # Field name made lowercase.
    processed = models.IntegerField(db_column='Processed') # Field name made lowercase.
    class Meta:
        db_table = u'note_2007_2008'

class Note20082009(models.Model):
    idnote = models.IntegerField(primary_key=True, db_column='idNote') # Field name made lowercase.
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    auteur = models.CharField(max_length=30, db_column='Auteur') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    note = models.FloatField(db_column='Note') # Field name made lowercase.
    notenorm = models.FloatField(db_column='NoteNorm') # Field name made lowercase.
    visible = models.CharField(max_length=1, db_column='Visible') # Field name made lowercase.
    processed = models.IntegerField(db_column='Processed') # Field name made lowercase.
    class Meta:
        db_table = u'note_2008_2009'

class Note20092010(models.Model):
    idnote = models.IntegerField(primary_key=True, db_column='idNote') # Field name made lowercase.
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    auteur = models.CharField(max_length=30, db_column='Auteur') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    note = models.FloatField(db_column='Note') # Field name made lowercase.
    notenorm = models.FloatField(db_column='NoteNorm') # Field name made lowercase.
    visible = models.CharField(max_length=1, db_column='Visible') # Field name made lowercase.
    processed = models.IntegerField(db_column='Processed') # Field name made lowercase.
    class Meta:
        db_table = u'note_2009_2010'

class Note20102011(models.Model):
    idnote = models.IntegerField(primary_key=True, db_column='idNote') # Field name made lowercase.
    ideleve = models.FloatField(db_column='idEleve') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    auteur = models.CharField(max_length=30, db_column='Auteur') # Field name made lowercase.
    date = models.DateTimeField(db_column='Date') # Field name made lowercase.
    ip = models.CharField(max_length=45, db_column='IP') # Field name made lowercase.
    note = models.FloatField(db_column='Note') # Field name made lowercase.
    notenorm = models.FloatField(db_column='NoteNorm') # Field name made lowercase.
    visible = models.CharField(max_length=1, db_column='Visible') # Field name made lowercase.
    processed = models.IntegerField(db_column='Processed') # Field name made lowercase.
    class Meta:
        db_table = u'note_2010_2011'

class Plage(models.Model):
    idplage = models.CharField(max_length=24, db_column='idPlage') # Field name made lowercase.
    annee = models.CharField(max_length=3, db_column='Annee') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    semaine = models.IntegerField(db_column='Semaine') # Field name made lowercase.
    jour = models.IntegerField(db_column='Jour') # Field name made lowercase.
    class Meta:
        db_table = u'plage'

class Plage20072008(models.Model):
    idplage = models.CharField(max_length=24, db_column='idPlage') # Field name made lowercase.
    annee = models.CharField(max_length=3, db_column='Annee') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    semaine = models.IntegerField(db_column='Semaine') # Field name made lowercase.
    jour = models.IntegerField(db_column='Jour') # Field name made lowercase.
    class Meta:
        db_table = u'plage_2007_2008'

class Plage20082009(models.Model):
    idplage = models.CharField(max_length=24, db_column='idPlage') # Field name made lowercase.
    annee = models.CharField(max_length=3, db_column='Annee') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    semaine = models.IntegerField(db_column='Semaine') # Field name made lowercase.
    jour = models.IntegerField(db_column='Jour') # Field name made lowercase.
    class Meta:
        db_table = u'plage_2008_2009'

class Plage20092010(models.Model):
    idplage = models.CharField(max_length=24, db_column='idPlage') # Field name made lowercase.
    annee = models.CharField(max_length=3, db_column='Annee') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    semaine = models.IntegerField(db_column='Semaine') # Field name made lowercase.
    jour = models.IntegerField(db_column='Jour') # Field name made lowercase.
    class Meta:
        db_table = u'plage_2009_2010'

class Plage20102011(models.Model):
    idplage = models.CharField(max_length=24, db_column='idPlage') # Field name made lowercase.
    annee = models.CharField(max_length=3, db_column='Annee') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    semaine = models.IntegerField(db_column='Semaine') # Field name made lowercase.
    jour = models.IntegerField(db_column='Jour') # Field name made lowercase.
    class Meta:
        db_table = u'plage_2010_2011'

class Profactivite(models.Model):
    idprof = models.CharField(max_length=24, db_column='idProf') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    class Meta:
        db_table = u'profactivite'

class Profactivite20072008(models.Model):
    idprof = models.CharField(max_length=24, db_column='idProf') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    class Meta:
        db_table = u'profactivite_2007_2008'

class Profactivite20082009(models.Model):
    idprof = models.CharField(max_length=24, db_column='idProf') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    class Meta:
        db_table = u'profactivite_2008_2009'

class Profactivite20092010(models.Model):
    idprof = models.CharField(max_length=24, db_column='idProf') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    class Meta:
        db_table = u'profactivite_2009_2010'

class Profactivite20102011(models.Model):
    idprof = models.CharField(max_length=24, db_column='idProf') # Field name made lowercase.
    idactivite = models.CharField(max_length=24, db_column='idActivite') # Field name made lowercase.
    class Meta:
        db_table = u'profactivite_2010_2011'

class Profs(models.Model):
    idprof = models.CharField(max_length=6, db_column='idProf') # Field name made lowercase.
    nom = models.CharField(max_length=60, db_column='Nom') # Field name made lowercase.
    prenom = models.CharField(max_length=45, db_column='Prenom') # Field name made lowercase.
    nomreseau = models.CharField(max_length=45, db_column='NomReseau') # Field name made lowercase.
    mail = models.CharField(max_length=765)
    class Meta:
        db_table = u'profs'

class Profs20082009(models.Model):
    idprof = models.CharField(max_length=6, db_column='idProf') # Field name made lowercase.
    nom = models.CharField(max_length=60, db_column='Nom') # Field name made lowercase.
    prenom = models.CharField(max_length=45, db_column='Prenom') # Field name made lowercase.
    nomreseau = models.CharField(max_length=45, db_column='NomReseau') # Field name made lowercase.
    mail = models.CharField(max_length=765)
    class Meta:
        db_table = u'profs_2008_2009'

class Profs20092010(models.Model):
    idprof = models.CharField(max_length=6, db_column='idProf') # Field name made lowercase.
    nom = models.CharField(max_length=60, db_column='Nom') # Field name made lowercase.
    prenom = models.CharField(max_length=45, db_column='Prenom') # Field name made lowercase.
    nomreseau = models.CharField(max_length=45, db_column='NomReseau') # Field name made lowercase.
    mail = models.CharField(max_length=765)
    class Meta:
        db_table = u'profs_2009_2010'

class Profs20102011(models.Model):
    idprof = models.CharField(max_length=6, db_column='idProf') # Field name made lowercase.
    nom = models.CharField(max_length=60, db_column='Nom') # Field name made lowercase.
    prenom = models.CharField(max_length=45, db_column='Prenom') # Field name made lowercase.
    nomreseau = models.CharField(max_length=45, db_column='NomReseau') # Field name made lowercase.
    mail = models.CharField(max_length=765)
    class Meta:
        db_table = u'profs_2010_2011'

class ResponsableLaniere(models.Model):
    nomreseau = models.CharField(max_length=45, db_column='NomReseau') # Field name made lowercase.
    idlaniere = models.CharField(max_length=6, db_column='idLaniere') # Field name made lowercase.
    annee = models.IntegerField(db_column='Annee') # Field name made lowercase.
    class Meta:
        db_table = u'responsable_laniere'

class TypeEleve(models.Model):
    type = models.CharField(max_length=3, primary_key=True, db_column='Type') # Field name made lowercase.
    description = models.CharField(max_length=90, db_column='Description') # Field name made lowercase.
    class Meta:
        db_table = u'type_eleve'

class Typeactivite(models.Model):
    type = models.CharField(max_length=3, primary_key=True, db_column='Type') # Field name made lowercase.
    nomactivite = models.CharField(max_length=60, db_column='NomActivite') # Field name made lowercase.
    class Meta:
        db_table = u'typeactivite'

class User(models.Model):
    uid = models.CharField(max_length=90, primary_key=True)
    upass = models.CharField(max_length=60)
    utype = models.CharField(max_length=6, blank=True)
    sno = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = u'user'

