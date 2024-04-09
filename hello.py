import librosa
import sys
import os
import librosa
import numpy as np


with open("C:\\Users\\HUGO\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\Beat_Script\\Davinci-Resolve-Beat-detection\\path.txt","r") as file:
    audio_file = file.read()

# https://musicinformationretrieval.com/onset_detection.html

file_path = audio_file


def onset():
    x, sr = librosa.load(file_path)
    onset_frames = librosa.onset.onset_detect(y=x, sr=sr)
    onset_times = librosa.frames_to_time(onset_frames)
    file_name_no_extension, _ = os.path.splitext(file_path)
    print(onset_times[1])
    
    with open("C:\\Users\\HUGO\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\Beat_Script\\Davinci-Resolve-Beat-detection\\beats.txt", 'w') as f:
        f.write('\n'.join(['%.4f' % onset_time for onset_time in onset_times]))
    return onset_times
def peak():

    y, sr = librosa.load(file_path)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr,
                                             hop_length=512,
                                             aggregate=np.median)
    peaks = librosa.util.peak_pick(onset_env)
    peaks_times = librosa.frames_to_time(peaks, sr=sr, hop_length=512)
    with open("C:\\Users\\HUGO\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\Beat_Script\\Davinci-Resolve-Beat-detection\\beats.txt", "w") as file:
        for peak in peaks_times:
            file.write(str(peak)+"\n")
    print(peaks_times[1])
    return peaks_times

def beat():
    y, sr = librosa.load(file_path)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    print(beat_times[1])
    
    with open("C:\\Users\\HUGO\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\Beat_Script\\Davinci-Resolve-Beat-detection\\beats.txt", "w") as file:
        for beat_time in beat_times:
            file.write(str(beat_time)+"\n")
    return beat_times

def beat_2():
    y, sr = librosa.load(audio_file)

    tempo_dynamic = librosa.feature.tempo(y=y, sr=sr, aggregate=None, std_bpm=4,hop_length=2048)


    beats_dynamic = []
    for tempo_value in tempo_dynamic:
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr, bpm=tempo_value, units='time', trim=False)
        beats_dynamic.extend(beats)


    beats_dynamic.sort()
    with open('C:\\Users\\HUGO\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\Beat_Script\\Davinci-Resolve-Beat-detection\\beats.txt', 'w') as file:
        for beat_time in beats_dynamic:
            file.write(str(beat_time) + '\n')
    return beats_dynamic

def big_beat(beats_arrays):
    occurrences = {}
    for algo in range(len(beats_arrays)):
        for element in beats_arrays[algo]:
            if element in occurrences:
                occurrences[element] += 1
            else:
                occurrences[element] = 1
    
    non_uniques = [element for element, count in occurrences.items() if count > 1]
    return non_uniques
    
#onset_tab = onset()
peak_tab = peak()
#beat_tab = beat()
#beat2_tab = beat_2()

tab = big_beat([onset_tab,peak_tab,beat_tab])
with open ('C:\\Users\\HUGO\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\Beat_Script\\Davinci-Resolve-Beat-detection\\beats.txt', 'w') as file:
    for line in tab:
        file.write(str(line)+"\n")

