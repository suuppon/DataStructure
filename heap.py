import numpy as np
import random, wave
from collections import deque
def generateNote(freq):
    nSamples = 44100
    sampleRate = 44100
    N = int(sampleRate/freq)
    # initialize ring buffer
    buf = deque([random.random() - 0.5 for i in range(N)]) # init sample buffer
    samples = np.array([0]*nSamples, 'float32')
    for i in range(nSamples):
        samples[i] = buf[0]
        avg = 0.995*0.5*(buf[0] + buf[1])
        buf.append(avg)
        buf.popleft()
    # samples to 16-bit to string
    # max value is 32767 for 16-bit
    samples = np.array(samples * 32767, 'int16')
    return samples
    
def writeWAVE(fname, data):
    file = wave.open(fname, 'wb')
    # WAV file parameters
    nChannels = 1 # mono channel sampleWidth = 2 # 2바이트 샘플 = 16 bits frameRate = 44100
    sampleWidth = 2
    frameRate = 44100
    nFrames = 44100
    # set parameters
    file.setparams((nChannels, sampleWidth, frameRate,
             nFrames,'NONE', 'noncompressed'))
    file.writeframes(data)
    file.close()
# generate D note
writeWAVE("D.wav", generateNote(146.83))