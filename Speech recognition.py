import speech_recognition as s

Audio_file = "D:\Memories.wav"
r = s.Recognizer()
with s.AudioFile(Audio_file) as source:
    audio = r.record(source)
# this with block reads the audio file
try:
    print("Lyrics:\n" + r.recognize_google(audio))
except s.UnknownValueError:
    print("Google speech recognotion could not understand the audio ")
except s.RequestError:
    print("Can't connect to Google. Something Went wrong")