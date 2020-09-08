from PIL import Image
from PIL.ImageQt import ImageQt

def generateThumbnail(im):
    im = Image.open(im)
    im.thumbnail((500, 550), Image.ANTIALIAS)
    return ImageQt(im)

if __name__ == "__main__":
    # qim = ImageQt(im)
    # pix = QtGui.QPixmap.fromImage(qim)
    # self.setPixmap(pix)
    im = Image.open("scans/1.bmp")
    print(im.size)
    im.thumbnail((100, 100))
    print(im.size)
    im.save("scans/11.bmp")
