import models 


def tab(eleve = models.Eleve.objects.get(pk=4382217)):

    i = 0

    tab = {}

#print 'num|laniere|activite|annee|matiere|note'
    for note in eleve.note_set.all():
        i += 1
        try:
            matiere = models.Matiere.objects.filter(idmatiere__iexact=note.idactivite.idmatiere).get(annee__iexact=eleve.annee)
            #print str(i)+'|'+matiere.idlaniere.nom +'|'+ note.idactivite.nom.rstrip()+'|'+str(matiere.annee)+'|'+note.idactivite.type.nomactivite+'|'+ str(note.note)
            #print len(note.idactivite.bilanactivite_set.all())

            if matiere.idlaniere.nom in tab:
                if note.idactivite.type.nomactivite in tab[matiere.idlaniere.nom]["categories"][note.idactivite.type.nomactivite]:
                    tab[matiere.idlaniere.nom]["categories"][note.idactivite.type.nomactivite]["note_list"] += [{"nom" : note.idactivite.nom.rstrip(), "value": note.note}]
                else:
                    tab[matiere.idlaniere.nom]["categories"][note.idactivite.type.nomactivite]["note_list"] += [{"nom" :note.idactivite.nom.rstrip(), "value": note.note}]
            else:
                tab[matiere.idlaniere.nom] = {"categories":{note.idactivite.type.nomactivite: {"note_list" : [{"nom": note.idactivite.nom.rstrip(), "value": note.note}]}}}
                
        except Exception as e:
            print 'error -> '+ str(e)

    return tab


def pprint_tab(tab):
    i=0
    for laniere in tab:
        print laniere
        for type in tab[laniere]:
            print '\t'+type
            try:
                for matiere in tab[laniere][type]:
                    i+=1
                    print '\t\t'+ str(i) +'|'+ matiere +'|'+ str(tab[laniere][type][matiere])
            except TypeError as e:
                print str(e)

        
