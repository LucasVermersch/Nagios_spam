#!/usr/bin/python
# coding: utf8

# ----------------------------------------------------
#
# Créé par Lucas Vermersch (lucas.vermersch@epsi.fr)
#  
# ----------------------------------------------------

import re,sys,commands,os
from datetime import datetime, timedelta

ip = "" # Ip de la machine à superviser
mdpMysql = "" # saisie du mot de passe mysql
utilisateurMysql = "" # saisie de l'utilisateur  mysql
dateDebut = datetime.now()
dateMoins = datetime.now() - timedelta(hours=4)

nb_commentaire = os.popen("mysql -h "+ ip +" -u "+ utilisateurMysql +" -p"+ mdpMysql +" -D wordpress -e \"SELECT COUNT(*) FROM wp_comments WHERE comment_date BETWEEN '"+ dateMoins.strftime("%Y-%m-%d %H:%M:%S") +"' AND '"+ dateDebut.strftime("%Y-%m-%d %H:%M:%S") +"'\";").read()

nb_commentaire =nb_commentaire[9:]

if nb_commentaire == "":
    nb_commentaire ="0"
    
#CRITICAL = 2
#WARNING = 1
#OK = 0
nb_max_ok = 5 # A modifier selon vos besoins
nb_max_warning = 10 # A modifier selon vos besoins
if int(nb_commentaire) < nb_max_ok :
    print("OK:")
    print("Il y a eu "+str(nb_commentaire)+ " commentaires")
    print("ces 4 dernieres heures")
    sys.exit(0)
elif int(nb_commentaire) >= nb_max_ok and int(nb_commentaire) <= nb_max_warning:
    print("WARNING:")
    print("Il y a eu "+str(nb_commentaire)+ " commentaires")
    print("ces 4 dernieres heures")
    sys.exit(1)
else:
    print("CRITICAL:")
    print("Il y a eu "+str(nb_commentaire)+ " commentaires")
    print("ces 4 dernieres heures")
    sys.exit(2)

