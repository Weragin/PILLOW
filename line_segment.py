import PIL.ImageOps
import numpy
from PIL import Image


def line_segment(point1: tuple, point2: tuple, size: tuple = (256, 256), bcgrnd_color: str = "white", line_color: tuple = (0, 0, 0)):
    img = Image.new("RGB", (256, 256), "white")
    pixels = img.load()
    vector = (1, (point2[1] - point1[1]) / (point2[0] - point1[0]))
    coordinates = [point1[0], point2[1]]
    for i in range(point1[0], point2[0] - 1):
        pixels[coordinates[0], int(coordinates[1])] = line_color
        coordinates[0] += vector[0]
        coordinates[1] += vector[1]
    img.show()


def flip_vertical(path: str = "data/lenna.jpg"):
    img0 = Image.open("data/lenna.jpg")
    img_new = Image.new("RGB", img0.size, "white")
    pixels_in = img0.load()
    pixels_out = img_new.load()

    for y in range(img0.height):
        for x in range(img0.width):
            pixels_out[- x - 1, y] = pixels_in[x, y]
    img_new.show()


def halve(path: str = "data/lenna.jpg"):
    img0 = Image.open("data/lenna.jpg")
    img_new = Image.new("RGB", img0.size, "white") # (img0.width//2, img0.height//2)
    pixels_in = img0.load()
    pixels_out = img_new.load()

    for y in range(img0.height//2):
        for x in range(img0.width//2):
            pixels_out[x, y] = pixels_in[2 * x, 2 * y]
    img_new.show()


def double(path: str = "data/lenna.jpg"):
    img0 = Image.open("data/lenna.jpg")
    img_new = Image.new("RGB", (img0.width*2, img0.height*2), "white")
    pixels_in = img0.load()
    pixels_out = img_new.load()
    for y in range(img0.height):
        for x in range(img0.width):
            pixels_out[x * 2, y * 2] = pixels_in[x, y]

    for y in range(0, img_new.height, 2):
        for x in range(1, img_new.width - 1, 2):
            pixels_out[x, y] = ((pixels_out[x - 1, y][0] + pixels_out[x + 1, y][0]) // 2,
                                (pixels_out[x - 1, y][1] + pixels_out[x + 1, y][1]) // 2,
                                (pixels_out[x - 1, y][2] + pixels_out[x + 1, y][2]) // 2)

    for y in range(0, img_new.height):
        pixels_out[img_new.width - 1, y] = pixels_out[img_new.width - 2, y]

    for y in range(1, img_new.height - 1, 2):
        for x in range(0, img_new.width):
            pixels_out[x, y] = ((pixels_out[x, y - 1][0] + pixels_out[x, y + 1][0]) // 2,
                                (pixels_out[x, y - 1][1] + pixels_out[x, y + 1][1]) // 2,
                                (pixels_out[x, y - 1][2] + pixels_out[x, y + 1][2]) // 2)

    for x in range(0, img_new.width):
        pixels_out[x, img_new.height - 1] = pixels_out[x, img_new.height - 2]

    img_new.show()


def flip_topleft_to_bottright(path: str = "data/lenna.jpg"):
    img0 = Image.open("data/lenna.jpg")
    img_new = Image.new("RGB", img0.size, "white")
    pixels_in = img0.load()
    pixels_out = img_new.load()
    for y in range(img0.height):
        for x in range(img0.width):
            pixels_out[x, y] = pixels_in[y, x]
    img_new.show()


def idk(path: str = "data/lenna.jpg", result_path: str = "data/results.txt"):
    img = PIL.ImageOps.grayscale(Image.open(path))
    pixels = img.load()
    fw = open(result_path, "w", encoding="ASCII")
    fw.write(f"{img.width} {img.height}\n")

    for y in range(img.height):
        for x in range(img.width):
            temp = hex(pixels[x, y])[2:]
            if len(temp) == 1:
                temp = "0" + temp
                fw.write(temp)
        fw.write("\n")
    fw.close()
# TODO toto iste ^^^^, ale cisto ciernobiely obrazok a namiesto ciernej 0 a namiesto bielej 1
# TODO tiez zobrat tento file a naspat vyprodukovat obrazok


image = Image.open("data/lenna.jpg")
image = PIL.ImageOps.grayscale(image)
image.show()

