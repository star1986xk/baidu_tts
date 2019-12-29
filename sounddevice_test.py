# -*- coding: utf-8 -*-

import numpy as np
import sounddevice as sd
from scipy.io import wavfile


# print(sd.query_devices())
fs = 44100 # Hz
length = 10 # s
# sd.default.device[0] = 8
recording = sd.rec(frames=fs * length, samplerate=fs, blocking=True, channels=1)
wavfile.write('recording.wav', fs, recording)