import pygame
from moviepy.editor import VideoFileClip

ico_image = "src/Genshin ICO.png"
program_name = "原神"
screen_size = (1280,720)
cartoon = "src/cartoon.mp4"

pygame.display.set_caption(program_name)
pygame.display.set_icon(pygame.image.load(ico_image))
screen = pygame.display.set_mode(screen_size)
clip = VideoFileClip(cartoon)
clip.preview()

clip.close()
pygame.quit()
