ViveLesCollegues_Louis
======================



## Faire un merge request

Pour faire un merge request, vous avez 2 possibilites.

### Avec un ticket (issue)

1) Creer un ticket (issue)
2) Clique sur la petite fleche de 'Create merge request' (bouton bleu)
3) Renommer la partie 'Branch name' par celui que vous voulez
4) Validez en cliquant sur 'Create merge request'

---- Passez sur GIT Bash ----

Rentrez les commandes suivantes dans l'ordre :
1) git pull origin 'nom de la branche choisie'
2) git switch 'nom de la branche choisie'
3) faites vos changement 
4) git add nom_du_fichier
5) git commit -m "message qui sera afficher'
6) git push origin 'nom de la branche choisie'

### Sans ticket

1) Creer une branche avec : git branch 'nom de la branche'
2) Selectionner la branche avec : git checkout 'nom de la branche'
3) Faites vos changement
4) git add nom_du_ficier
5) git commit -m "message qui sera afficher"
6) git push origin 'nom de la branche'

---- Passez sur GITlab ----

1) allez sur votre projet
2) tout en haut de la page on va vous proposer de faire un merge request, acceptez
3) rentrez les parametres du merge request et c'est bon !

Pensez à regarder le wiki sur gitlab pour connaître la procédure pour rentrer un nouvelle employer !