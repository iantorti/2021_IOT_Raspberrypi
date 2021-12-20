import pygame

pygame.init()

pygame.mixer.music.load('나비보벳따우.mp3')

while True:
    cmd = input('play: p, pause: pp, unpause: up, stop: s,quit: q, vloume: v >')
    if cmd == 'p':
        pygame.mixer.music.play()
    elif cmd == 'pp':
        pygame.mixer.music.pause()
    elif cmd == 'up':
        pygame.mixer.music.unpause()
    elif cmd == 's':
        pygame.mixer.music.stop()
    elif cmd == 'q':
        break
    elif cmd == 'v':
        pygame.mixer.music.setvolume
    else:
        print('incorrect cmd')

pygame.mixer.music.unload()
