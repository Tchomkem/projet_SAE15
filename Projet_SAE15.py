import os
import csv
#import matplotlib.pyplot as plt

def lecture_fichier(chemin: str):
    """
    Lecture d'un fichier.

    :param chemin: le chemin du fichier
    :return: la chaine de caractère contenant tout le fichier ou None si le fichier n'a pu être lu
    """

    try:
        with open(chemin, encoding="utf8") as fh:
            return fh.read()
    except:
        print("Le fichier n'existe pas %s", os.path.abspath(chemin))
        return None
tab=[]
tab1=([],[],[],[],[])    
f = lecture_fichier('SAE15.txt')
#print(f)
d = f.splitlines()
with open('SAE15.csv', 'w', newline='') as csvfile:
    fieldnames = ['IP_destination', 'IP_source','Flags','length']
    writer=csv.writer(csvfile)
    writer.writerow(['IP_destination;IP_source;Flags;length'])
#print(d)
    for e in d: 
        if e.startswith('\t')==False:
            tab=e.split(' ')
            tab1[0].append(tab[2])
            tab1[1].append(tab[4])
            tab1[2].append(tab[6])
            tab1[3].append(tab[20:21])
            for p in tab:
                if tab[5] == "Flags":
                    tab1[2].append(tab[5+1])
                if tab[3].startswith('HTTP'):
                    tab1[3].append(tab[-1])
            texte=''
            for i in range(4):
                texte=texte+str(tab1[i])+';'
            #print(texte)    
        writer.writerow([texte])
                
#with open('sae15.csv', 'w', newline='') as csvfile:
    #fieldnames = ['IP_destination', 'IP_source','Flags','length']
    #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer.writeheader()
    #writer.writerow({'IP_destination': tab1[0], 'IP_source': tab1[1], 'Flags':tab1[2], 'length':tab1[3]})
    
    
   
#print(tab1[0])
#print(tab1[1])
#print(tab1[2])
#print(tab1[3])



        
     #print(e)        

        

    