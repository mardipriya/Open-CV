import speech_recognition as sr
import time
import vlc
import os
path = os.getcwd()+'\\Videos';
list = []
for e in os.walk(path):
    list = e[2]
count = 0
volume = 0
vlength = len(list)
player = vlc.MediaPlayer('Videos/'+list[count])
player.play()
player.audio_set_volume(volume)
rec = sr.Recognizer()

while True:
    with sr.Microphone () as source:
        print('Speak Anything...')
        audio = rec.listen(source)
        try:
            text = rec.recognize_google(audio)
            print(text)
            if text == 'forward':
                player.set_time(player.get_time() + 10000)
            elif text == 'backward':
                player.set_time(player.get_time() - 10000)
            elif text == 'increase volume':
                if volume <=200:
                    volume = volume+25
                    player.audio_set_volume(volume)
                else:
                    print('Full Volume')

            elif text == 'decrease volume':
                if volume !=0:
                    volume = volume-25
                    player.audio_set_volume(volume)
                else:
                    print('Volume Zero')
            elif text == 'stop':
                player.stop()
            elif text == 'start':
                count=0
                player = vlc.MediaPlayer('Videos/' + list[count])
                player.play()
                volume = 0
                player.audio_set_volume(volume)
            elif text == 'pause':
                player.pause()
            elif text == 'play':
                player.pause()
            elif text == 'next':
                if count < vlength-1:
                    count = count+ 1
                    player.stop()
                    player = vlc.MediaPlayer('Videos/' + list[count])
                    player.play()
                    volume = 0
                    player.audio_set_volume(volume)
                else:
                    print('No Next Videos')

            elif  text == 'previous':
                if count == 0:
                    print('No Previous Videos')
                else:
                    count = count - 1
                    player.stop()
                    player = vlc.MediaPlayer('Videos/' + list[count])
                    player.play()
        except Exception as e:
            print(e)
    time.sleep(1)
