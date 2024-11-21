from scipy.io import wavfile
samplerate, data = wavfile.read('Recording.wav')
wavfile.write('Recording0.wav', samplerate, data[:, 0])