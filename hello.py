import librosa

# Charger le fichier audio
audio_file = "C:\\Users\\HUGO\\Videos\\4K Video Downloader\\Future, Metro Boomin, Travis Scott, Playboi Carti - Type Shit (Official Video).mp3"
y, sr = librosa.load(audio_file)

# Détecter les beats
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# Convertir les indices des échantillons en secondes
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# Afficher les instants des beats
with open("beats.txt", "w") as file:
    for beat_time in beat_times:
        file.write(str(beat_time)+"\n")
