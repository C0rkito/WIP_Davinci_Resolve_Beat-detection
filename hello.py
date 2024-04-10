import sys
import os
import librosa
import numpy as np



directory = os.getcwd()

with open(os.getcwd()+"\\path.txt","r") as file:
    file_path = file.read()




def onset():
    x, sr = librosa.load(file_path)
    onset_frames = librosa.onset.onset_detect(y=x, sr=sr,wait=1, pre_avg=1, post_avg=1, pre_max=1, post_max=1)
    onset_times = librosa.frames_to_time(onset_frames)
    file_name_no_extension, _ = os.path.splitext(file_path)
    print(onset_times[50])
    onset_times.sort()
    with open(os.getcwd()+"\\beats.txt", 'w') as f:
        f.write('\n'.join(['%.4f' % onset_time for onset_time in onset_times]))
    return onset_times
def peak():

    y, sr = librosa.load(file_path)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr,
                                             hop_length=512)
    peaks = librosa.util.peak_pick(onset_env, pre_max=1, post_max=1, pre_avg=1, post_avg=1, delta=0.8, wait=1)
    peaks_times = librosa.frames_to_time(peaks, sr=sr, hop_length=512)
    peaks_times.sort()
    with open(directory+"\\beats.txt", "w") as file:
        for peak in peaks_times:
            file.write(str(peak)+"\n")
    print(peaks_times[50])
    return peaks_times

def beat():
    y, sr = librosa.load(file_path)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    print(beat_times[50])
    
    beat_times.sort()
    with open(directory+"\\beats.txt", "w") as file:
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
    with open(directory+'\\beats.txt', 'w') as file:
        for beat_time in beats_dynamic:
            file.write(str(beat_time) + '\n')
    return beats_dynamic

def big_beat(beats_arrays):
    occurrences = {}
    for algo in range(len(beats_arrays)):
        for element in beats_arrays[algo]:
            if (element) in occurrences:
                occurrences[element] += 1
            else:
                occurrences[element] = 1

    non_uniques = [element for element, count in occurrences.items() if count >= 2]
    return non_uniques
    
onset_tab = onset()
peak_tab = peak()
beat_tab = beat()
#beat2_tab = beat_2()

tab = big_beat([onset_tab,peak_tab,beat_tab])
with open (directory+'\\beats.txt', 'w') as file:
    for line in tab:
        file.write(str(line)+"\n")

