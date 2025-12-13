from gtts import gTTS

import os
# Texte à convertir en audio

# Créer un objet gTTS en français
tts = gTTS(text=text, lang='fr')


ospf=[
    ("zone ospf","groupe d'ip et de routeurs qui partagent la meme base de données ospf"),
    ("lsdb","link state database, tableau interne présent dans chaque routeur ospf qui contient une copie complète de la carte réseau"),
    ("ospf","open shortest path first"),
    ("LSAs","Link state advertissement, petit document qui décrit l'état de ses liens, ses interfaces et parfois du réseau derrière lui"),
    ("abr: area border router","Routeur qui relie deux zones ospf dont au moins une est une zone areao"),
    ("adjency","Relation synchronisé entre deux routeurs ospf voisins permettant l'échangent complet des lsa"),
    ("Neighbor","routeur détecté via des paquets hello"),
    ("hello paquet","paquet ospf envoyé périodiquement pour détecter les voisins et maintenir les liens"),
    ("spf","algorithme qui calcule le plus court chemin vers chaque réseau en utilisant la LSDB"),
    ("DR : Désignated Router","router élu sur les réseaux multi-accès pour réduire le nombre d'adjacences"),
    ("BDR : ","DR qui prends le relais si le DR principale tombe"),
    ("Hello interval","fréquence d'envoie des hellos paquet"),
    ("Dead Interval ","Temps après lequel un voisin est déclaré mort"),
    ("LSA Refresh","fréquence de régénération des LSAs"),
    ("Network type ","détermin le comportement ospf de l'interface"),
    ("asbr","Autonomous system boundary : Router qui connecte un ospf as à un autre as, il injecte des routes externes dans ospf via des lsas type 5"),
    ("type lsa","messages ospf qui décrivent ll'état des liens et des routeurs. Il construit la lsdb et fait des calculs spf"),
    ("lsa type 1","Router lsa: créer par chaque routeur, il décrit les interfaces et les liens du routeur dans sa zone"),
    ("lsa type 2","Network lsa: créer par le DR, il décrit les routeurs connectés à un réseau multi-access"),
    ("lsa type 3","Summary lsa: créer par les abr, il annaonce les réseaux d'une zone vers une autre zone"),
    ("MPLS","Multi Protocole Label Switching : techno de commutation de paquet utilisée dans les réseaux ip et autres protocoles"),
]
# Sauvegarder le fichier audio


os.makedirs("audio",exist_ok=True)



for index, (terme, definition) in enumerate(ospf, start=1):

    # 1️⃣ Terme
    tts_terme = gTTS(text=terme, lang="fr")
    tts_terme.save(f"audio/ospf_{index}_1.mp3")

    # 2️⃣ Définition
    tts_definition = gTTS(text=definition, lang="fr")
    tts_definition.save(f"audio/ospf_{index}_2.mp3")

print("Tous les fichiers audio ont été générés.")







    
