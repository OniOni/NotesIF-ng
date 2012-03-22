# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Log'
        db.create_table(u'LOG', (
            ('auteur', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='Auteur')),
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True, db_column='Date')),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=45, primary_key=True, db_column='IP')),
            ('action', self.gf('django.db.models.fields.TextField')(db_column='Action')),
        ))
        db.send_create_signal('studentapp', ['Log'])

        # Adding model 'LogEleve'
        db.create_table(u'LOG_eleve', (
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.User'], max_length=60, primary_key=True, db_column='uid')),
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True, db_column='Date')),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='IP')),
        ))
        db.send_create_signal('studentapp', ['LogEleve'])

        # Adding model 'Absence'
        db.create_table(u'absence', (
            ('ideleve', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Eleve'], primary_key=True, db_column='idEleve')),
            ('date', self.gf('django.db.models.fields.DateField')(primary_key=True, db_column='Date')),
            ('idactivite', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Activite'], max_length=24, primary_key=True, db_column='idActivite')),
        ))
        db.send_create_signal('studentapp', ['Absence'])

        # Adding model 'Activite'
        db.create_table(u'activite', (
            ('idactivite', self.gf('django.db.models.fields.CharField')(unique=True, max_length=24, db_column='idActivite')),
            ('idmatiere', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Matiere'], max_length=18, db_column='idMatiere')),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Typeactivite'], max_length=3, db_column='Type')),
            ('coefficient', self.gf('django.db.models.fields.FloatField')(db_column='Coefficient')),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=768, db_column='Nom')),
            ('nbhprevu', self.gf('django.db.models.fields.IntegerField')(db_column='NbHPrevu')),
            ('annee', self.gf('django.db.models.fields.CharField')(max_length=3, db_column='Annee')),
            ('sansnote', self.gf('django.db.models.fields.IntegerField')(db_column='SansNote')),
            ('notevisible', self.gf('django.db.models.fields.CharField')(max_length=1, db_column='NoteVisible')),
            ('semestre', self.gf('django.db.models.fields.IntegerField')(db_column='Semestre')),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='ID')),
        ))
        db.send_create_signal('studentapp', ['Activite'])

        # Adding model 'Admins'
        db.create_table(u'admins', (
            ('login', self.gf('django.db.models.fields.CharField')(max_length=60, primary_key=True)),
        ))
        db.send_create_signal('studentapp', ['Admins'])

        # Adding model 'Anneeuniversitaire'
        db.create_table(u'anneeuniversitaire', (
            ('idanneeuniversitaire', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='idAnneeUniversitaire')),
            ('datedebut', self.gf('django.db.models.fields.DateField')(db_column='DateDebut')),
            ('datefin', self.gf('django.db.models.fields.DateField')(db_column='DateFin')),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=60, db_column='Nom')),
        ))
        db.send_create_signal('studentapp', ['Anneeuniversitaire'])

        # Adding model 'BilanActivite'
        db.create_table(u'bilan_activite', (
            ('idanneeuniversitaire', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Anneeuniversitaire'], primary_key=True, db_column='idAnneeUniversitaire')),
            ('idactivite', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Activite'], max_length=24, primary_key=True, db_column='idActivite')),
            ('min', self.gf('django.db.models.fields.FloatField')()),
            ('max', self.gf('django.db.models.fields.FloatField')()),
            ('moyenne', self.gf('django.db.models.fields.FloatField')()),
            ('ecart_type', self.gf('django.db.models.fields.FloatField')()),
            ('pourcent_saisie', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('studentapp', ['BilanActivite'])

        # Adding model 'BilanEleve'
        db.create_table(u'bilan_eleve', (
            ('idbilaneleve', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='idBilanEleve')),
            ('ideleve', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Eleve'], db_column='idEleve')),
            ('idcontratpedagogique', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Contratpedagogique'], db_column='idContratPedagogique')),
            ('moyenne', self.gf('django.db.models.fields.FloatField')()),
            ('moyenneds', self.gf('django.db.models.fields.FloatField')(db_column='moyenneDS')),
            ('coefficientds', self.gf('django.db.models.fields.FloatField')(db_column='coefficientDS')),
            ('moyennetp', self.gf('django.db.models.fields.FloatField')(db_column='moyenneTP')),
            ('coefficienttp', self.gf('django.db.models.fields.FloatField')(db_column='coefficientTP')),
            ('classement', self.gf('django.db.models.fields.IntegerField')()),
            ('nbeleves', self.gf('django.db.models.fields.IntegerField')(db_column='nbEleves')),
            ('redoublement', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exclusion', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('absences', self.gf('django.db.models.fields.IntegerField')()),
            ('coefficients', self.gf('django.db.models.fields.FloatField')()),
            ('coefficientdispenses', self.gf('django.db.models.fields.FloatField')(db_column='coefficientDispenses')),
            ('decisionjury', self.gf('django.db.models.fields.TextField')(db_column='decisionJury')),
            ('moyennesem1', self.gf('django.db.models.fields.FloatField')(db_column='moyenneSEM1')),
            ('moyennesem2', self.gf('django.db.models.fields.FloatField')(db_column='moyenneSEM2')),
            ('moyennenorm', self.gf('django.db.models.fields.FloatField')(db_column='moyenneNorm')),
            ('moyennenormds', self.gf('django.db.models.fields.FloatField')(db_column='moyenneNormDS')),
            ('moyennenormtp', self.gf('django.db.models.fields.FloatField')(db_column='moyenneNormTP')),
            ('ectsvalides', self.gf('django.db.models.fields.IntegerField')(db_column='ectsValides')),
        ))
        db.send_create_signal('studentapp', ['BilanEleve'])

        # Adding model 'BilanLaniere'
        db.create_table(u'bilan_laniere', (
            ('idbilanlaniere', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='idBilanLaniere')),
            ('ideleve', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Eleve'], db_column='idEleve')),
            ('moyenne', self.gf('django.db.models.fields.FloatField')()),
            ('moyenneds', self.gf('django.db.models.fields.FloatField')(db_column='moyenneDS')),
            ('coefficientds', self.gf('django.db.models.fields.FloatField')(db_column='coefficientDS')),
            ('moyennetp', self.gf('django.db.models.fields.FloatField')(db_column='moyenneTP')),
            ('coefficienttp', self.gf('django.db.models.fields.FloatField')(db_column='coefficientTP')),
            ('classement', self.gf('django.db.models.fields.IntegerField')()),
            ('nbeleves', self.gf('django.db.models.fields.IntegerField')(db_column='nbEleves')),
            ('idlaniere', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Laniere'], max_length=9, db_column='idLaniere')),
            ('qualification', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('rattrapage', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('ectsvalides', self.gf('django.db.models.fields.IntegerField')(db_column='ectsValides')),
        ))
        db.send_create_signal('studentapp', ['BilanLaniere'])

        # Adding model 'BilanMatiere'
        db.create_table(u'bilan_matiere', (
            ('idbilanmatiere', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='idBilanMatiere')),
            ('ideleve', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Eleve'], db_column='idEleve')),
            ('moyenne', self.gf('django.db.models.fields.FloatField')()),
            ('moyenneds', self.gf('django.db.models.fields.FloatField')(db_column='moyenneDS')),
            ('coefficientds', self.gf('django.db.models.fields.FloatField')(db_column='coefficientDS')),
            ('moyennetp', self.gf('django.db.models.fields.FloatField')(db_column='moyenneTP')),
            ('coefficienttp', self.gf('django.db.models.fields.FloatField')(db_column='coefficientTP')),
            ('classement', self.gf('django.db.models.fields.IntegerField')()),
            ('nbeleves', self.gf('django.db.models.fields.IntegerField')(db_column='nbEleves')),
            ('idmatiere', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Matiere'], max_length=18, db_column='idMatiere')),
            ('qualification', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('studentapp', ['BilanMatiere'])

        # Adding model 'Contenucontratpedagogique'
        db.create_table(u'contenucontratpedagogique', (
            ('idcontratpedagogique', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Contratpedagogique'], primary_key=True, db_column='idContratPedagogique')),
            ('idmatiereyoratooid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Matiere'], max_length=30, primary_key=True, db_column='idMatiereYoratooID')),
            ('coefficient', self.gf('django.db.models.fields.FloatField')(db_column='Coefficient')),
        ))
        db.send_create_signal('studentapp', ['Contenucontratpedagogique'])

        # Adding model 'Contratpedagogique'
        db.create_table(u'contratpedagogique', (
            ('idcontratpedagogique', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='idContratPedagogique')),
            ('idanneeuniversitaire', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Anneeuniversitaire'], db_column='idAnneeUniversitaire')),
            ('idepoque', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Epoque'], db_column='idEpoque')),
            ('credits', self.gf('django.db.models.fields.FloatField')(db_column='Credits')),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=60, db_column='Nom')),
        ))
        db.send_create_signal('studentapp', ['Contratpedagogique'])

        # Adding model 'CoursEleve'
        db.create_table(u'cours_eleve', (
            ('ideleve', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Eleve'], primary_key=True, db_column='idEleve')),
            ('idactivite', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Activite'], max_length=24, primary_key=True, db_column='idActivite')),
        ))
        db.send_create_signal('studentapp', ['CoursEleve'])

        # Adding model 'CreditsEtranger'
        db.create_table(u'credits_etranger', (
            ('idcreditsetranger', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='idCreditsEtranger')),
            ('ideleve', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Eleve'], db_column='idEleve')),
            ('credits', self.gf('django.db.models.fields.IntegerField')()),
            ('etablissement', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('auteur', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='Auteur')),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='Date')),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='IP')),
        ))
        db.send_create_signal('studentapp', ['CreditsEtranger'])

        # Adding model 'Dispense'
        db.create_table(u'dispense', (
            ('ideleve', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Eleve'], primary_key=True, db_column='idEleve')),
            ('auteur', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='Auteur')),
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True, db_column='Date')),
            ('raison', self.gf('django.db.models.fields.CharField')(max_length=120, db_column='Raison')),
            ('idactivite', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Activite'], max_length=24, primary_key=True, db_column='idActivite')),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='IP')),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=3, db_column='Type')),
        ))
        db.send_create_signal('studentapp', ['Dispense'])

        # Adding model 'Eleve'
        db.create_table(u'eleve', (
            ('ideleve', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='idEleve')),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=120, db_column='Nom')),
            ('nomreseau', self.gf('django.db.models.fields.CharField')(max_length=90, db_column='NomReseau')),
            ('binomes1', self.gf('django.db.models.fields.IntegerField')(db_column='Binomes1')),
            ('binomes2', self.gf('django.db.models.fields.IntegerField')(db_column='Binomes2')),
            ('binomes3', self.gf('django.db.models.fields.IntegerField')(db_column='Binomes3')),
            ('annee', self.gf('django.db.models.fields.IntegerField')(db_column='Annee')),
            ('groupe', self.gf('django.db.models.fields.IntegerField')(db_column='Groupe')),
            ('echange', self.gf('django.db.models.fields.CharField')(max_length=3, db_column='Echange')),
            ('datenaissance', self.gf('django.db.models.fields.DateField')(db_column='DateNaissance')),
            ('origine', self.gf('django.db.models.fields.CharField')(max_length=3, db_column='Origine')),
            ('mail', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Eleve'], max_length=3, db_column='Type')),
            ('tuteur', self.gf('django.db.models.fields.CharField')(max_length=6, db_column='Tuteur')),
        ))
        db.send_create_signal('studentapp', ['Eleve'])

        # Adding model 'Epoque'
        db.create_table(u'epoque', (
            ('idepoque', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='idEpoque')),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=60, db_column='Nom')),
            ('annee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Anneeuniversitaire'], db_column='Annee')),
            ('semestre', self.gf('django.db.models.fields.IntegerField')(db_column='Semestre')),
        ))
        db.send_create_signal('studentapp', ['Epoque'])

        # Adding model 'EtudiantContratpedagogique'
        db.create_table(u'etudiant_contratpedagogique', (
            ('ideleve', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Eleve'], primary_key=True, db_column='idEleve')),
            ('idcontratpedagogique', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Contratpedagogique'], primary_key=True, db_column='idContratPedagogique')),
            ('valide', self.gf('django.db.models.fields.CharField')(max_length=1, db_column='Valide')),
            ('classementvisible', self.gf('django.db.models.fields.IntegerField')(db_column='ClassementVisible')),
        ))
        db.send_create_signal('studentapp', ['EtudiantContratpedagogique'])

        # Adding model 'Laniere'
        db.create_table(u'laniere', (
            ('idlaniere', self.gf('django.db.models.fields.CharField')(max_length=9, primary_key=True, db_column='idLaniere')),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=78, db_column='Nom')),
            ('barreds', self.gf('django.db.models.fields.FloatField')(db_column='BarreDS')),
            ('barretp', self.gf('django.db.models.fields.FloatField')(db_column='BarreTP')),
            ('barregenerale', self.gf('django.db.models.fields.FloatField')(db_column='BarreGenerale')),
            ('nomreseau', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='NomReseau')),
            ('nomen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Profs'], max_length=150, db_column='NomEn')),
        ))
        db.send_create_signal('studentapp', ['Laniere'])

        # Adding model 'Matiere'
        db.create_table(u'matiere', (
            ('idmatiere', self.gf('django.db.models.fields.CharField')(max_length=18, primary_key=True, db_column='idMatiere')),
            ('idlaniere', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Laniere'], max_length=9, db_column='idLaniere')),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=210, db_column='Nom')),
            ('annee', self.gf('django.db.models.fields.IntegerField')(db_column='Annee')),
            ('credits', self.gf('django.db.models.fields.FloatField')(db_column='Credits')),
            ('idmatiereyoratooid', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='idMatiereYoratooID')),
            ('nomen', self.gf('django.db.models.fields.CharField')(max_length=150, db_column='NomEn')),
        ))
        db.send_create_signal('studentapp', ['Matiere'])

        # Adding model 'MessagesEleve'
        db.create_table(u'messages_eleve', (
            ('idmessage', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='IDMessage')),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=765, db_column='Message')),
            ('date', self.gf('django.db.models.fields.DateField')(db_column='Date')),
            ('annee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Anneeuniversitaire'], max_length=3, db_column='Annee')),
        ))
        db.send_create_signal('studentapp', ['MessagesEleve'])

        # Adding model 'News'
        db.create_table(u'news', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='idNews')),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('annee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Anneeuniversitaire'], db_column='Anne')),
        ))
        db.send_create_signal('studentapp', ['News'])

        # Adding model 'Note'
        db.create_table(u'note', (
            ('ideleve', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Eleve'], primary_key=True, db_column='idEleve')),
            ('idactivite', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Activite'], to_field='idactivite', max_length=24, db_column='idActivite')),
            ('auteur', self.gf('django.db.models.fields.CharField')(max_length=30, db_column='Auteur')),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_column='Date')),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='IP')),
            ('note', self.gf('django.db.models.fields.FloatField')(db_column='Note')),
            ('notenorm', self.gf('django.db.models.fields.FloatField')(db_column='NoteNorm')),
            ('visible', self.gf('django.db.models.fields.CharField')(max_length=1, db_column='Visible')),
            ('processed', self.gf('django.db.models.fields.IntegerField')(db_column='Processed')),
        ))
        db.send_create_signal('studentapp', ['Note'])

        # Adding model 'Plage'
        db.create_table(u'plage', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='idPlage')),
            ('idplage', self.gf('django.db.models.fields.CharField')(max_length=24, primary_key=True, db_column='idPlage')),
            ('annee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Anneeuniversitaire'], max_length=3, db_column='Annee')),
            ('idactivite', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Activite'], max_length=24, db_column='idActivite')),
            ('semaine', self.gf('django.db.models.fields.IntegerField')(db_column='Semaine')),
            ('jour', self.gf('django.db.models.fields.IntegerField')(db_column='Jour')),
        ))
        db.send_create_signal('studentapp', ['Plage'])

        # Adding model 'Profactivite'
        db.create_table(u'profactivite', (
            ('idprof', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Profs'], max_length=24, primary_key=True, db_column='idProf')),
            ('idactivite', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Activite'], max_length=24, primary_key=True, db_column='idActivite')),
        ))
        db.send_create_signal('studentapp', ['Profactivite'])

        # Adding model 'Profs'
        db.create_table(u'profs', (
            ('idprof', self.gf('django.db.models.fields.IntegerField')(max_length=6, primary_key=True, db_column='idProf')),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=60, db_column='Nom')),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='Prenom')),
            ('nomreseau', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='NomReseau')),
            ('mail', self.gf('django.db.models.fields.CharField')(max_length=765)),
        ))
        db.send_create_signal('studentapp', ['Profs'])

        # Adding model 'ResponsableLaniere'
        db.create_table(u'responsable_laniere', (
            ('nomreseau', self.gf('django.db.models.fields.CharField')(max_length=45, db_column='NomReseau')),
            ('idprof', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Profs'], primary_key=True, db_column='idProf')),
            ('idlaniere', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentapp.Laniere'], max_length=6, primary_key=True, db_column='idLaniere')),
            ('annee', self.gf('django.db.models.fields.IntegerField')(db_column='Annee')),
        ))
        db.send_create_signal('studentapp', ['ResponsableLaniere'])

        # Adding model 'TypeEleve'
        db.create_table(u'type_eleve', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='idTypeEleve')),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=3, db_column='Type')),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=90, db_column='Description')),
        ))
        db.send_create_signal('studentapp', ['TypeEleve'])

        # Adding model 'Typeactivite'
        db.create_table(u'typeactivite', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='idTypeActivite')),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=3, primary_key=True, db_column='Type')),
            ('nomactivite', self.gf('django.db.models.fields.CharField')(max_length=60, db_column='NomActivite')),
        ))
        db.send_create_signal('studentapp', ['Typeactivite'])

        # Adding model 'User'
        db.create_table(u'user', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='idUser')),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('upass', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('utype', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('sno', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal('studentapp', ['User'])

        # Adding model 'UserProfile'
        db.create_table('studentapp_userprofile', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['studentapp.User'], unique=True)),
            ('id_from_ldap', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='idUserProfile')),
        ))
        db.send_create_signal('studentapp', ['UserProfile'])


    def backwards(self, orm):
        
        # Deleting model 'Log'
        db.delete_table(u'LOG')

        # Deleting model 'LogEleve'
        db.delete_table(u'LOG_eleve')

        # Deleting model 'Absence'
        db.delete_table(u'absence')

        # Deleting model 'Activite'
        db.delete_table(u'activite')

        # Deleting model 'Admins'
        db.delete_table(u'admins')

        # Deleting model 'Anneeuniversitaire'
        db.delete_table(u'anneeuniversitaire')

        # Deleting model 'BilanActivite'
        db.delete_table(u'bilan_activite')

        # Deleting model 'BilanEleve'
        db.delete_table(u'bilan_eleve')

        # Deleting model 'BilanLaniere'
        db.delete_table(u'bilan_laniere')

        # Deleting model 'BilanMatiere'
        db.delete_table(u'bilan_matiere')

        # Deleting model 'Contenucontratpedagogique'
        db.delete_table(u'contenucontratpedagogique')

        # Deleting model 'Contratpedagogique'
        db.delete_table(u'contratpedagogique')

        # Deleting model 'CoursEleve'
        db.delete_table(u'cours_eleve')

        # Deleting model 'CreditsEtranger'
        db.delete_table(u'credits_etranger')

        # Deleting model 'Dispense'
        db.delete_table(u'dispense')

        # Deleting model 'Eleve'
        db.delete_table(u'eleve')

        # Deleting model 'Epoque'
        db.delete_table(u'epoque')

        # Deleting model 'EtudiantContratpedagogique'
        db.delete_table(u'etudiant_contratpedagogique')

        # Deleting model 'Laniere'
        db.delete_table(u'laniere')

        # Deleting model 'Matiere'
        db.delete_table(u'matiere')

        # Deleting model 'MessagesEleve'
        db.delete_table(u'messages_eleve')

        # Deleting model 'News'
        db.delete_table(u'news')

        # Deleting model 'Note'
        db.delete_table(u'note')

        # Deleting model 'Plage'
        db.delete_table(u'plage')

        # Deleting model 'Profactivite'
        db.delete_table(u'profactivite')

        # Deleting model 'Profs'
        db.delete_table(u'profs')

        # Deleting model 'ResponsableLaniere'
        db.delete_table(u'responsable_laniere')

        # Deleting model 'TypeEleve'
        db.delete_table(u'type_eleve')

        # Deleting model 'Typeactivite'
        db.delete_table(u'typeactivite')

        # Deleting model 'User'
        db.delete_table(u'user')

        # Deleting model 'UserProfile'
        db.delete_table('studentapp_userprofile')


    models = {
        'studentapp.absence': {
            'Meta': {'object_name': 'Absence', 'db_table': "u'absence'"},
            'date': ('django.db.models.fields.DateField', [], {'primary_key': 'True', 'db_column': "'Date'"}),
            'idactivite': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Activite']", 'max_length': '24', 'primary_key': 'True', 'db_column': "'idActivite'"}),
            'ideleve': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Eleve']", 'primary_key': 'True', 'db_column': "'idEleve'"})
        },
        'studentapp.activite': {
            'Meta': {'object_name': 'Activite', 'db_table': "u'activite'"},
            'annee': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "'Annee'"}),
            'coefficient': ('django.db.models.fields.FloatField', [], {'db_column': "'Coefficient'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'ID'"}),
            'idactivite': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '24', 'db_column': "'idActivite'"}),
            'idmatiere': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Matiere']", 'max_length': '18', 'db_column': "'idMatiere'"}),
            'nbhprevu': ('django.db.models.fields.IntegerField', [], {'db_column': "'NbHPrevu'"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '768', 'db_column': "'Nom'"}),
            'notevisible': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "'NoteVisible'"}),
            'sansnote': ('django.db.models.fields.IntegerField', [], {'db_column': "'SansNote'"}),
            'semestre': ('django.db.models.fields.IntegerField', [], {'db_column': "'Semestre'"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Typeactivite']", 'max_length': '3', 'db_column': "'Type'"})
        },
        'studentapp.admins': {
            'Meta': {'object_name': 'Admins', 'db_table': "u'admins'"},
            'login': ('django.db.models.fields.CharField', [], {'max_length': '60', 'primary_key': 'True'})
        },
        'studentapp.anneeuniversitaire': {
            'Meta': {'object_name': 'Anneeuniversitaire', 'db_table': "u'anneeuniversitaire'"},
            'datedebut': ('django.db.models.fields.DateField', [], {'db_column': "'DateDebut'"}),
            'datefin': ('django.db.models.fields.DateField', [], {'db_column': "'DateFin'"}),
            'idanneeuniversitaire': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'idAnneeUniversitaire'"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_column': "'Nom'"})
        },
        'studentapp.bilanactivite': {
            'Meta': {'object_name': 'BilanActivite', 'db_table': "u'bilan_activite'"},
            'ecart_type': ('django.db.models.fields.FloatField', [], {}),
            'idactivite': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Activite']", 'max_length': '24', 'primary_key': 'True', 'db_column': "'idActivite'"}),
            'idanneeuniversitaire': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Anneeuniversitaire']", 'primary_key': 'True', 'db_column': "'idAnneeUniversitaire'"}),
            'max': ('django.db.models.fields.FloatField', [], {}),
            'min': ('django.db.models.fields.FloatField', [], {}),
            'moyenne': ('django.db.models.fields.FloatField', [], {}),
            'pourcent_saisie': ('django.db.models.fields.FloatField', [], {})
        },
        'studentapp.bilaneleve': {
            'Meta': {'object_name': 'BilanEleve', 'db_table': "u'bilan_eleve'"},
            'absences': ('django.db.models.fields.IntegerField', [], {}),
            'classement': ('django.db.models.fields.IntegerField', [], {}),
            'coefficientdispenses': ('django.db.models.fields.FloatField', [], {'db_column': "'coefficientDispenses'"}),
            'coefficientds': ('django.db.models.fields.FloatField', [], {'db_column': "'coefficientDS'"}),
            'coefficients': ('django.db.models.fields.FloatField', [], {}),
            'coefficienttp': ('django.db.models.fields.FloatField', [], {'db_column': "'coefficientTP'"}),
            'decisionjury': ('django.db.models.fields.TextField', [], {'db_column': "'decisionJury'"}),
            'ectsvalides': ('django.db.models.fields.IntegerField', [], {'db_column': "'ectsValides'"}),
            'exclusion': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'idbilaneleve': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'idBilanEleve'"}),
            'idcontratpedagogique': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Contratpedagogique']", 'db_column': "'idContratPedagogique'"}),
            'ideleve': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Eleve']", 'db_column': "'idEleve'"}),
            'moyenne': ('django.db.models.fields.FloatField', [], {}),
            'moyenneds': ('django.db.models.fields.FloatField', [], {'db_column': "'moyenneDS'"}),
            'moyennenorm': ('django.db.models.fields.FloatField', [], {'db_column': "'moyenneNorm'"}),
            'moyennenormds': ('django.db.models.fields.FloatField', [], {'db_column': "'moyenneNormDS'"}),
            'moyennenormtp': ('django.db.models.fields.FloatField', [], {'db_column': "'moyenneNormTP'"}),
            'moyennesem1': ('django.db.models.fields.FloatField', [], {'db_column': "'moyenneSEM1'"}),
            'moyennesem2': ('django.db.models.fields.FloatField', [], {'db_column': "'moyenneSEM2'"}),
            'moyennetp': ('django.db.models.fields.FloatField', [], {'db_column': "'moyenneTP'"}),
            'nbeleves': ('django.db.models.fields.IntegerField', [], {'db_column': "'nbEleves'"}),
            'redoublement': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'studentapp.bilanlaniere': {
            'Meta': {'object_name': 'BilanLaniere', 'db_table': "u'bilan_laniere'"},
            'classement': ('django.db.models.fields.IntegerField', [], {}),
            'coefficientds': ('django.db.models.fields.FloatField', [], {'db_column': "'coefficientDS'"}),
            'coefficienttp': ('django.db.models.fields.FloatField', [], {'db_column': "'coefficientTP'"}),
            'ectsvalides': ('django.db.models.fields.IntegerField', [], {'db_column': "'ectsValides'"}),
            'idbilanlaniere': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'idBilanLaniere'"}),
            'ideleve': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Eleve']", 'db_column': "'idEleve'"}),
            'idlaniere': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Laniere']", 'max_length': '9', 'db_column': "'idLaniere'"}),
            'moyenne': ('django.db.models.fields.FloatField', [], {}),
            'moyenneds': ('django.db.models.fields.FloatField', [], {'db_column': "'moyenneDS'"}),
            'moyennetp': ('django.db.models.fields.FloatField', [], {'db_column': "'moyenneTP'"}),
            'nbeleves': ('django.db.models.fields.IntegerField', [], {'db_column': "'nbEleves'"}),
            'qualification': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'rattrapage': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'studentapp.bilanmatiere': {
            'Meta': {'object_name': 'BilanMatiere', 'db_table': "u'bilan_matiere'"},
            'classement': ('django.db.models.fields.IntegerField', [], {}),
            'coefficientds': ('django.db.models.fields.FloatField', [], {'db_column': "'coefficientDS'"}),
            'coefficienttp': ('django.db.models.fields.FloatField', [], {'db_column': "'coefficientTP'"}),
            'idbilanmatiere': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'idBilanMatiere'"}),
            'ideleve': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Eleve']", 'db_column': "'idEleve'"}),
            'idmatiere': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Matiere']", 'max_length': '18', 'db_column': "'idMatiere'"}),
            'moyenne': ('django.db.models.fields.FloatField', [], {}),
            'moyenneds': ('django.db.models.fields.FloatField', [], {'db_column': "'moyenneDS'"}),
            'moyennetp': ('django.db.models.fields.FloatField', [], {'db_column': "'moyenneTP'"}),
            'nbeleves': ('django.db.models.fields.IntegerField', [], {'db_column': "'nbEleves'"}),
            'qualification': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'studentapp.contenucontratpedagogique': {
            'Meta': {'object_name': 'Contenucontratpedagogique', 'db_table': "u'contenucontratpedagogique'"},
            'coefficient': ('django.db.models.fields.FloatField', [], {'db_column': "'Coefficient'"}),
            'idcontratpedagogique': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Contratpedagogique']", 'primary_key': 'True', 'db_column': "'idContratPedagogique'"}),
            'idmatiereyoratooid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Matiere']", 'max_length': '30', 'primary_key': 'True', 'db_column': "'idMatiereYoratooID'"})
        },
        'studentapp.contratpedagogique': {
            'Meta': {'object_name': 'Contratpedagogique', 'db_table': "u'contratpedagogique'"},
            'credits': ('django.db.models.fields.FloatField', [], {'db_column': "'Credits'"}),
            'idanneeuniversitaire': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Anneeuniversitaire']", 'db_column': "'idAnneeUniversitaire'"}),
            'idcontratpedagogique': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'idContratPedagogique'"}),
            'idepoque': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Epoque']", 'db_column': "'idEpoque'"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_column': "'Nom'"})
        },
        'studentapp.courseleve': {
            'Meta': {'object_name': 'CoursEleve', 'db_table': "u'cours_eleve'"},
            'idactivite': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Activite']", 'max_length': '24', 'primary_key': 'True', 'db_column': "'idActivite'"}),
            'ideleve': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Eleve']", 'primary_key': 'True', 'db_column': "'idEleve'"})
        },
        'studentapp.creditsetranger': {
            'Meta': {'object_name': 'CreditsEtranger', 'db_table': "u'credits_etranger'"},
            'auteur': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'Auteur'"}),
            'credits': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'Date'"}),
            'etablissement': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'idcreditsetranger': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'idCreditsEtranger'"}),
            'ideleve': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Eleve']", 'db_column': "'idEleve'"}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'IP'"})
        },
        'studentapp.dispense': {
            'Meta': {'object_name': 'Dispense', 'db_table': "u'dispense'"},
            'auteur': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'Auteur'"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True', 'db_column': "'Date'"}),
            'idactivite': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Activite']", 'max_length': '24', 'primary_key': 'True', 'db_column': "'idActivite'"}),
            'ideleve': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Eleve']", 'primary_key': 'True', 'db_column': "'idEleve'"}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'IP'"}),
            'raison': ('django.db.models.fields.CharField', [], {'max_length': '120', 'db_column': "'Raison'"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "'Type'"})
        },
        'studentapp.eleve': {
            'Meta': {'object_name': 'Eleve', 'db_table': "u'eleve'"},
            'annee': ('django.db.models.fields.IntegerField', [], {'db_column': "'Annee'"}),
            'binomes1': ('django.db.models.fields.IntegerField', [], {'db_column': "'Binomes1'"}),
            'binomes2': ('django.db.models.fields.IntegerField', [], {'db_column': "'Binomes2'"}),
            'binomes3': ('django.db.models.fields.IntegerField', [], {'db_column': "'Binomes3'"}),
            'datenaissance': ('django.db.models.fields.DateField', [], {'db_column': "'DateNaissance'"}),
            'echange': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "'Echange'"}),
            'groupe': ('django.db.models.fields.IntegerField', [], {'db_column': "'Groupe'"}),
            'ideleve': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'idEleve'"}),
            'mail': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '120', 'db_column': "'Nom'"}),
            'nomreseau': ('django.db.models.fields.CharField', [], {'max_length': '90', 'db_column': "'NomReseau'"}),
            'origine': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "'Origine'"}),
            'tuteur': ('django.db.models.fields.CharField', [], {'max_length': '6', 'db_column': "'Tuteur'"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Eleve']", 'max_length': '3', 'db_column': "'Type'"})
        },
        'studentapp.epoque': {
            'Meta': {'object_name': 'Epoque', 'db_table': "u'epoque'"},
            'annee': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Anneeuniversitaire']", 'db_column': "'Annee'"}),
            'idepoque': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'idEpoque'"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_column': "'Nom'"}),
            'semestre': ('django.db.models.fields.IntegerField', [], {'db_column': "'Semestre'"})
        },
        'studentapp.etudiantcontratpedagogique': {
            'Meta': {'object_name': 'EtudiantContratpedagogique', 'db_table': "u'etudiant_contratpedagogique'"},
            'classementvisible': ('django.db.models.fields.IntegerField', [], {'db_column': "'ClassementVisible'"}),
            'idcontratpedagogique': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Contratpedagogique']", 'primary_key': 'True', 'db_column': "'idContratPedagogique'"}),
            'ideleve': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Eleve']", 'primary_key': 'True', 'db_column': "'idEleve'"}),
            'valide': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "'Valide'"})
        },
        'studentapp.laniere': {
            'Meta': {'object_name': 'Laniere', 'db_table': "u'laniere'"},
            'barreds': ('django.db.models.fields.FloatField', [], {'db_column': "'BarreDS'"}),
            'barregenerale': ('django.db.models.fields.FloatField', [], {'db_column': "'BarreGenerale'"}),
            'barretp': ('django.db.models.fields.FloatField', [], {'db_column': "'BarreTP'"}),
            'idlaniere': ('django.db.models.fields.CharField', [], {'max_length': '9', 'primary_key': 'True', 'db_column': "'idLaniere'"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '78', 'db_column': "'Nom'"}),
            'nomen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Profs']", 'max_length': '150', 'db_column': "'NomEn'"}),
            'nomreseau': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'NomReseau'"})
        },
        'studentapp.log': {
            'Meta': {'object_name': 'Log', 'db_table': "u'LOG'"},
            'action': ('django.db.models.fields.TextField', [], {'db_column': "'Action'"}),
            'auteur': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'Auteur'"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True', 'db_column': "'Date'"}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '45', 'primary_key': 'True', 'db_column': "'IP'"})
        },
        'studentapp.logeleve': {
            'Meta': {'object_name': 'LogEleve', 'db_table': "u'LOG_eleve'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True', 'db_column': "'Date'"}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'IP'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.User']", 'max_length': '60', 'primary_key': 'True', 'db_column': "'uid'"})
        },
        'studentapp.matiere': {
            'Meta': {'object_name': 'Matiere', 'db_table': "u'matiere'"},
            'annee': ('django.db.models.fields.IntegerField', [], {'db_column': "'Annee'"}),
            'credits': ('django.db.models.fields.FloatField', [], {'db_column': "'Credits'"}),
            'idlaniere': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Laniere']", 'max_length': '9', 'db_column': "'idLaniere'"}),
            'idmatiere': ('django.db.models.fields.CharField', [], {'max_length': '18', 'primary_key': 'True', 'db_column': "'idMatiere'"}),
            'idmatiereyoratooid': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'idMatiereYoratooID'"}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '210', 'db_column': "'Nom'"}),
            'nomen': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_column': "'NomEn'"})
        },
        'studentapp.messageseleve': {
            'Meta': {'object_name': 'MessagesEleve', 'db_table': "u'messages_eleve'"},
            'annee': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Anneeuniversitaire']", 'max_length': '3', 'db_column': "'Annee'"}),
            'date': ('django.db.models.fields.DateField', [], {'db_column': "'Date'"}),
            'idmessage': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'IDMessage'"}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Message'"})
        },
        'studentapp.news': {
            'Meta': {'object_name': 'News', 'db_table': "u'news'"},
            'annee': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Anneeuniversitaire']", 'db_column': "'Anne'"}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'idNews'"}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '765'})
        },
        'studentapp.note': {
            'Meta': {'object_name': 'Note', 'db_table': "u'note'"},
            'auteur': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'Auteur'"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'db_column': "'Date'"}),
            'idactivite': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Activite']", 'to_field': "'idactivite'", 'max_length': '24', 'db_column': "'idActivite'"}),
            'ideleve': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Eleve']", 'primary_key': 'True', 'db_column': "'idEleve'"}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'IP'"}),
            'note': ('django.db.models.fields.FloatField', [], {'db_column': "'Note'"}),
            'notenorm': ('django.db.models.fields.FloatField', [], {'db_column': "'NoteNorm'"}),
            'processed': ('django.db.models.fields.IntegerField', [], {'db_column': "'Processed'"}),
            'visible': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "'Visible'"})
        },
        'studentapp.plage': {
            'Meta': {'object_name': 'Plage', 'db_table': "u'plage'"},
            'annee': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Anneeuniversitaire']", 'max_length': '3', 'db_column': "'Annee'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'idPlage'"}),
            'idactivite': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Activite']", 'max_length': '24', 'db_column': "'idActivite'"}),
            'idplage': ('django.db.models.fields.CharField', [], {'max_length': '24', 'primary_key': True, 'db_column': "'idPlage'"}),
            'jour': ('django.db.models.fields.IntegerField', [], {'db_column': "'Jour'"}),
            'semaine': ('django.db.models.fields.IntegerField', [], {'db_column': "'Semaine'"})
        },
        'studentapp.profactivite': {
            'Meta': {'object_name': 'Profactivite', 'db_table': "u'profactivite'"},
            'idactivite': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Activite']", 'max_length': '24', 'primary_key': 'True', 'db_column': "'idActivite'"}),
            'idprof': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Profs']", 'max_length': '24', 'primary_key': 'True', 'db_column': "'idProf'"})
        },
        'studentapp.profs': {
            'Meta': {'object_name': 'Profs', 'db_table': "u'profs'"},
            'idprof': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'primary_key': 'True', 'db_column': "'idProf'"}),
            'mail': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_column': "'Nom'"}),
            'nomreseau': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'NomReseau'"}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'Prenom'"})
        },
        'studentapp.responsablelaniere': {
            'Meta': {'object_name': 'ResponsableLaniere', 'db_table': "u'responsable_laniere'"},
            'annee': ('django.db.models.fields.IntegerField', [], {'db_column': "'Annee'"}),
            'idlaniere': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Laniere']", 'max_length': '6', 'primary_key': 'True', 'db_column': "'idLaniere'"}),
            'idprof': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentapp.Profs']", 'primary_key': 'True', 'db_column': "'idProf'"}),
            'nomreseau': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "'NomReseau'"})
        },
        'studentapp.typeactivite': {
            'Meta': {'object_name': 'Typeactivite', 'db_table': "u'typeactivite'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'idTypeActivite'"}),
            'nomactivite': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_column': "'NomActivite'"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True', 'db_column': "'Type'"})
        },
        'studentapp.typeeleve': {
            'Meta': {'object_name': 'TypeEleve', 'db_table': "u'type_eleve'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '90', 'db_column': "'Description'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'idTypeEleve'"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "'Type'"})
        },
        'studentapp.user': {
            'Meta': {'object_name': 'User', 'db_table': "u'user'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'idUser'"}),
            'sno': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'upass': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'utype': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'})
        },
        'studentapp.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id_from_ldap': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'idUserProfile'"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['studentapp.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['studentapp']
