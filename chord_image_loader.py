from PIL import Image
from random_number_generate import random_number_generate

def chord_image_loader(dir):
    random_list = random_number_generate()
    image_list = []
    for i in range(0,5):
        image_list.append(Image.open(f"GuitarChords/{dir}/{random_list[i]}.jpg"))

    return image_list




    