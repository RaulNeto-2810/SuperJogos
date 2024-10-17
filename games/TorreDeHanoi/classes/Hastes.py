import pygame
from collections import deque
# from anilha import Anilha


class Haste:
    def __init__(self, img: pygame.image, x: int, y: int):
        super().__init__()
        self.__img = img
        self.__pos = self.__img.get_rect(midbottom=(x, y))
        self.deque = deque()

    def get_img(self):
        return self.__img

    def get_pos(self):
        return self.__pos
