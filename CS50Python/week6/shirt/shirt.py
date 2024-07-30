import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("incorrect number of args")
    read_file = sys.argv[1]
    ex1 = check_ext(read_file)
    write_file = sys.argv[2]
    ex2 = check_ext(write_file)
    if ex1 != ex2:
        sys.exit("non matching")
    overlay(read_file, write_file)
    #print(write_file)

def check_ext(name):
    ext_list = [".jpg", ".jpeg", ".png"]
    file_name, extension = os.path.splitext(name)
    #print(extension)
    if extension in ext_list:
        return extension
    else:
        sys.exit("not correct extension")

def overlay(input, output):
    try:
        original = Image.open(input, mode = 'r', formats = None)
        shirt = Image.open("shirt.png")
        #gets size of png in pixels
        size = shirt.size
        #resizes photo to fit shirt
        resized = ImageOps.fit(original, size)
        resized.paste(shirt, shirt)
        resized.save(output)

    except FileNotFoundError:
        sys.exit("no such file")



if __name__ == "__main__":
    main()
