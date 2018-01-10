import pyaudio
import wave
import sys

def play1():
    CHUNK = 10240

    #if len(sys.argv) < 2:
        #print("Plays a wave file.\n\nUsage: %s tts_output.wav" % sys.argv[0])
    #sys.exit(-1)

    wf = wave.open("tts_output.wav", 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()

def play2():
    CHUNK = 10240

    #if len(sys.argv) < 2:
        #print("Plays a wave file.\n\nUsage: %s tts_output.wav" % sys.argv[0])
    #sys.exit(-1)

    wf = wave.open("tts2_output.wav", 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()

def play3():
        CHUNK = 10240

        # if len(sys.argv) < 2:
        # print("Plays a wave file.\n\nUsage: %s tts_output.wav" % sys.argv[0])
        # sys.exit(-1)

        wf = wave.open("tts3_output.wav", 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(CHUNK)

        while data != b'':
            stream.write(data)
            data = wf.readframes(CHUNK)

        stream.stop_stream()
        stream.close()

        p.terminate()

#play()
