import librosa
import sys

with open("C:\\Users\\HUGO\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\Beat_Script\\Davinci-Resolve-Beat-detection\\path.txt","r") as file:
    audio_file = file.read()


print(audio_file)


y, sr = librosa.load(audio_file)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

with open("C:\\Users\\HUGO\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\Beat_Script\\Davinci-Resolve-Beat-detection\\beats.txt", "w") as file:
    for beat_time in beat_times:
        file.write(str(beat_time)+"\n")


#AUDIO FILTER

 
