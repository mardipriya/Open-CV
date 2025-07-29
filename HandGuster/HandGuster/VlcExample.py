import vlc
import cv2
import time
player = vlc.MediaPlayer('Videos/maharshi.mp4')
player.play()
while True:
    player.audio_set_volume(100)
    time.sleep(1)
    player.set_time(player.get_time() + 10000)
    player.audio_set_volume(200)
    time.sleep(1)



