import socket
import threading, wave, pyaudio,pickle,struct
import time
import sys

import pyaudio

DURATION = 10  # seconds

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345  # You can use any open port number

# Audio Settings
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


#Initialize pyaudio
audio = pyaudio.PyAudio()

#Open stream for input
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    output=True,
                    frames_per_buffer=CHUNK)

#create socket connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))
print("Connected to server")

def callback(in_data, frame_count, time_info, status):
    client_socket.sendall(in_data)
    return (None, pyaudio.paContinue)


stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    stream_callback=callback)

print("Streaming audio to the server....")
try:
    while stream.is_active():
        pass
except KeyboardInterrupt:
    print("Stream stopped")

stream.stop_stream()
stream.close()

audio.terminate()


client_socket.close()
print("connection closed")

# def callback(in_data, frame_count, time_info, status):
#     return (in_data, pyaudio.paContinue)

# p = pyaudio.PyAudio()
# stream = p.open(format=p.get_format_from_width(2),
#                 channels=1 if sys.platform == 'darwin' else 2,
#                 rate=44100,
#                 input=True,
#                 output=True,
#                 stream_callback=callback)

# start = time.time()
# while stream.is_active() and (time.time() - start) < DURATION:
#     pyaudio.parse
#     time.sleep(0.1)

# stream.close()
# p.terminate()
