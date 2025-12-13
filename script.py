from gtts import gTTS

# Texte à convertir en audio

# Créer un objet gTTS en français
tts = gTTS(text=text, lang='fr')

ospf=[
    "zone ospf"
]
# Sauvegarder le fichier audio
tts.save("gtts.mp3")

print("Audio généré : pression_gtts.mp3")
