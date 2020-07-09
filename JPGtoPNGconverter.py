import sys
import os
from PIL import Image

folder1 = sys.argv[1]
folder2 = sys.argv[2]

if not os.path.exists(folder2):
    os.makedirs(folder2)

for filename in os.listdir(folder1):
    img = Image.open(f'{folder1}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{folder2}{clean_name}.png','png')
    print("DONE!")
