from PIL import Image
from os import scandir, remove

for im in scandir("scans"):
    im = str(im.path).split(".")
    print(im[-1])
    if im[-1] != "tif":
        continue

    img = Image.open(".".join(im)).convert("1")
    img.save(im[0] + ".bmp", format="BMP")
    remove(".".join(im))
