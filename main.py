from random import choice

import pygame


pygame.init()


class Barray2Image:
    def __init__(self,
                 barray: list = None,
                 barray_random_size=100,
                 img_size=(600, 600),
                 img_name='sample',
                 img_ext='.png'):
        self.barray = barray if barray is not None else self.get_random_barray(barray_random_size)
        self.img_size = img_size
        self.img_name = img_name
        self.img_ext = img_ext

    def count_blocks(self):
        white, black = 0, 0
        for row in self.barray:
            white += row.count(1)
            black += row.count(0)
        print(f'white: {white} | black: {black}')

    def get_image(self):
        row_biggest = sorted([len(i) for i in self.barray])[-1]
        pixel_w = self.img_size[0] // row_biggest
        pixel_h = self.img_size[1] // len(self.barray)
        img_w = self.img_size[0] if pixel_w > 0 else row_biggest * pixel_w
        img_h = self.img_size[1] if pixel_h > 0 else len(self.barray) * pixel_h
        self.img_size = img_w, img_h
        surf = pygame.Surface(self.img_size, pygame.SRCALPHA)
        for y, row in enumerate(self.barray):
            for x, col in enumerate(row):
                pygame.draw.rect(surf, ['black', 'white'][col], [x * pixel_w, y * pixel_h, pixel_w, pixel_h])
        return surf

    def save_image(self, count_blocks=True):
        pygame.image.save(self.get_image(), f'{self.img_name}{self.img_ext}')
        if count_blocks:
            self.count_blocks()

    @staticmethod
    def get_random_barray(size: int):
        return [[choice([0, 1]) for _ in range(size)] for _ in range(size)]


if __name__ == '__main__':
    tool = Barray2Image([[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1]])
    tool.save_image()
