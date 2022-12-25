from audioplayer import AudioPlayer
from time import sleep
player = AudioPlayer('assets/oxxxy.mp3')
player.play(loop=False, block=False)
sleep(20)
print("Стоп!")
player.stop()


