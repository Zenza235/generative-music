import librosa
import librosa.onset

import numpy as np

def get_audio_info(path, n_fft=2048):
    y, sr = librosa.load(path)
    
    S = np.abs(librosa.stft(y, n_fft=n_fft))
    freq_range = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    o_env = librosa.onset.onset_strength(y=y, sr=sr, max_size=S.shape[0])
    onsets = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr, units='frames')
    return S, freq_range, onsets

def get_note_data(note, num_bins=3):
    # list of the maximum values of each bin across the frames
    bin_maxes = np.amax(note, axis=1)
    # "num_bins"th highest bins ordered from least to greatest
    bins = np.argpartition(bin_maxes, -num_bins)[-num_bins:]
    print(bins)
    print(bin_maxes[bins])

    bin_frames = note[bins, :]
    # average magnitude of each bin across the frames
    bin_means = np.mean(bin_frames, axis=1)

    data = np.append([bins], [bin_means], axis=0)
    return data

if __name__ == '__main__':
    import os
    # temp path
    path = os.getcwd() + '/audio_files/test_audio/test_piano_old.wav'
    S, freq_range, onsets = get_audio_info(path)

    note = S[:, onsets[0]:onsets[1]]
    data = get_note_data(note, num_bins=10)

    print(data)