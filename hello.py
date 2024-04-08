import librosa
import sys

audio_file = sys.argv[1]
print(audio_file)

with open("C:\\Users\\HUGO\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\Beat_Script\\Davinci-Resolve-Beat-detection\\accusse.txt","w") as file:
    file.write(audio_file)
y, sr = librosa.load(audio_file)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

with open("beats.txt", "w") as file:
    for beat_time in beat_times:
        file.write(str(beat_time)+"\n")


#AUDIO FILTER

 
