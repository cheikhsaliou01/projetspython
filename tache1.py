#ma_list.reverse()
#print(ma_list)
#nbel = len(ma_list)
#print(nbel)
#Exo1 Écris un programme qui fait la somme des transaction
Exo1 = "Écris un programme qui fait la somme des transaction"
print(Exo1)
ma_list = [250, 12, 45, 32, 23, 25, 250, 12]
somme = sum(ma_list)
print("La somme des transaction est :",somme)
####################################################################
#Tâche 2 : Afficher la 5eme transaction 
exo2 = "Afficher la 5eme transaction "
print(exo2)
print("la 5eme transaction est :", ma_list[4])
###########################################
#Tâche 3:Ordonner la liste (asc)
exo3 = "Tâche 3:Ordonner la liste (asc)"
print(exo3)
ordonner = sorted(ma_list)
print(ordonner)
#ordonner.sort(reverse=True)
#print(ordonner)
ordonner.sort(reverse=False)
print(ordonner)
################################################################
#Tache 4 : Transformer la liste en tuple
exo4 = "Transformer la liste en tuple"
print(exo4)
transf = tuple(ma_list)
print(type(transf))
#Tâche 5:Afficher la transaction la plus petite
exo5 = "Afficher la transaction la plus petite"
print(exo5)
print(transf)
print("la transaction la plus petite est :",transf[1])
#Tâche 6:Afficher la dernière transaction
exo6 = "Afficher la dernière transaction"
print(exo6)
print("La dernier transaction est : ",transf[-1])
############################################################
#Tâche 7:Supprimer les transactions dupliquées
exo7 = "Supprimer les transactions dupliquées"
print(exo7)
sup = list(set(ma_list))
print(sup)
###########################################################
#Tâche 8:Supprimer la dernière transaction
exo8 = "Supprimer la dernière transaction"
print(exo8)
del ma_list[-1]
print(ma_list)
##########################################################
#Tâche 9:Créer une copie des transactions
exo9 = "Créer une copie des transactions"
print(exo9)
copyliste = ma_list.copy()
print("La liste a ete bien copier :",copyliste)
######################################################
#Tâche 10:Écris un programme qui fait la moyenne des transactions.
ex010 =  "Écris un programme qui fait la moyenne des transactions."
print(ex010)
print(ma_list)
s = 0 
for i in range(0,7):
    s = s + ma_list[i]
print("la moyenne de la transaction est :",s/7)

#Tâche 11:Convertir la liste en dictionnaire
exo11 = "Convertir la liste en dictionnaire"
print(exo11)
import itertools
ma_list_iter = iter(ma_list)
ma_list_dict_obj = itertools.zip_longest(ma_list_iter,ma_list_iter,fillvalue=None)
ma_list_dict = dict(ma_list_dict_obj)
print("La liste a ete bien convertit en dictionnaire :",ma_list_dict)