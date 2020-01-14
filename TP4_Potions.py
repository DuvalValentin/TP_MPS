etats_possibles=["poison","ortie","arriere","avant"]
#dict_etat={"poison":None,"ortie":None,"arriere":None,"avant":None}#Bon ben avec ça ça marche pas (même référence)
list_potions = {1:{"poison":None,"ortie":None,"arriere":None,"avant":None},2:{"poison":None,"ortie":None,"arriere":None,"avant":None},3:{"poison":None,"ortie":None,"arriere":None,"avant":None},4:{"poison":None,"ortie":None,"arriere":None,"avant":None},5:{"poison":None,"ortie":None,"arriere":None,"avant":None},6:{"poison":None,"ortie":None,"arriere":None,"avant":None},7:{"poison":None,"ortie":None,"arriere":None,"avant":None}}

def init():
  # 3 et 6 ne contiennent pas de poison
  list_potions[3]["poison"]=False
  list_potions[6]["poison"]=False
  # 1 et 7 ne permettent pas d'avancer
  list_potions[1]["avant"]=False
  list_potions[7]["avant"]=False
  # 2 et 6 sont égaux et ne peuvent pas être avancer ou reculer
  list_potions[2]["arriere"]=False
  list_potions[6]["arriere"]=False
  list_potions[2]["avant"]=False
  list_potions[6]["avant"]=False
  #1 est tout à gauche et ne peux pas être une ortie
  list_potions[1]["ortie"]=False

# Poison à gauche des orties
def OrtiesPoison():
  for i in range(2,8):
    if(list_potions[i]["ortie"]):
      list_potions[i-1]["poison"]=True

# 2 et 6 sont égaux
def twoAndSix():
  for etat in etats_possibles:
    if(list_potions[2][etat]!=None):
      list_potions[6][etat]=list_potions[2][etat]
    if(list_potions[6][etat]!=None):
      list_potions[2][etat]=list_potions[6][etat]

# 1 et 7 sont différents
def oneAndSeven():
  for etat in etats_possibles:
    if(list_potions[1][etat]==True):
      list_potions[7][etat]=False
    if(list_potions[7][etat]==True):
      list_potions[1][etat]=False

# si un True alors le reste est Faux, si 3 Faux alors le restant est Vrai
def TrueFalse():
  for etats in list_potions.values():
    falseCount=0
    for etat in etats_possibles:
      if(etats[etat]==True):
        for etat_bis in etats_possibles:
          if(etat!=etat_bis):
            etats[etat_bis]=False
      if(etats[etat]==False):
        falseCount+=1
    if (falseCount==3):
      for etat in etats_possibles:
        if(etats[etat]==None):
          etats[etat]=True
          break

# Si toutes les potions d'un type ont été trouvés les autres sont passés à false pour ce type
def foundedPotions():
  for etat in etats_possibles:
    foundedCount=0
    for etats in list_potions.values():
      if(etats[etat]==True):
        foundedCount+=1
    if((etat=="poison" and foundedCount==3)or (etat=="ortie" and foundedCount==2)or (etat=="arriere" and foundedCount==1)or (etat=="avant" and foundedCount==1)):
      for etats in list_potions.values():
        if(etats[etat]!=True):
          etats[etat]=False

# Compte le nombre de True
def countTrue():
  countTrue=0
  for etats in list_potions.values():
    for etat in etats_possibles:
      if(etats[etat]==True):
        countTrue+=1
  return countTrue

# On lance les vérifications nécessaires plusieurs fois
def loop():
  OrtiesPoison()
  twoAndSix()
  oneAndSeven()
  TrueFalse()
  foundedPotions()
def run():
  init()
  while(countTrue()!=7):
    loop()
  for numero, etats in list_potions.items():
    if(etats["poison"]==True):
      print("La potion "+str(numero)+" est un poison.")
    if(etats["ortie"]==True):
      print("La potion "+str(numero)+" est du vin d'ortie.")
    if(etats["arriere"]==True):
      print("La potion "+str(numero)+" permet de reculer.")
    if(etats["avant"]==True):
      print("La potion "+str(numero)+" permet d'avancer.")

run()