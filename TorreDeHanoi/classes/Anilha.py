import pygame as pg


class Anilha:
    def __init__(self, size: int, img: pg.image, x=0, y=0):
        self.__img = img
        self.size = size
        self.__pos = self.__img.get_rect(midbottom=(x, y))

    def __repr__(self):
        return f"(size={self.size}; x={self.__pos[0]}; y={self.__pos[1]})"

    def get_img(self):
        return self.__img

    def get_pos(self):
        return self.__pos

    def set_pos(self, x, y):
        self.__pos = self.__img.get_rect(midbottom=(x, y))
