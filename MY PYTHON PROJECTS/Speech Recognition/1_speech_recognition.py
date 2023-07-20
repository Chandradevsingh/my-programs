import wave

obj = wave.open('sample-6s.wav', "rb")

print('Number of channels', obj.getnchannels())
print('Sample Width', obj.getsampwidth())
print('Frame Rate', obj.getframerate())
print('Number of Frames', obj.getnframes())
print('All the Parameters', obj.getparams())

t_audio = obj.getnframes()/obj.getframerate()
print(t_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames)/4)

obj.close()

obj_new = wave.open('sample-6s1.wav', 'wb')

obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(44100.0)

obj_new.writeframes(frames)
obj_new.close()