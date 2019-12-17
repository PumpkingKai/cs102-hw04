import sys
import math
from PIL import Image

print(sys.argv)
assert len(sys.argv) == 3, "input_image.jpg"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size

new_img = Image.new("RGB", (width, height), "white")

wm = width / 2
hm = height / 2

for i in range(1, int(wm)):
    for j in range(1, height):
        dis = math.sqrt((i-wm)**2 + (j-hm)**2)
        if dis < (width / 4):
            r, g, b = img.getpixel((i, j))
            new_img.putpixel((i, j), (0, g, b))
        else:
            r, g, b = img.getpixel((i, j))
            new_img.putpixel((i, j), (0, 0, int(1.5 * b)))

for i in range(int(wm), int(width - (width / 4))):
    for j in range(1, height):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (r, g, b))

for i in range(int(width - (width / 4)), width):
    for j in range(1, height):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (r, 0, 0))
new_img.save(output_path, "JPEG")
