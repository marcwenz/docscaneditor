from pyzbar.pyzbar import decode
from pyzbar.wrapper import ZBarSymbol
from PIL import Image

def transpose(im, t):
    if t:
        return im.transpose(t)
    return im

def matchQrCode(im, info=None):
    info = str.encode(info)
    img = Image.open(im)
    res = goodDecode(img)
    if not res:
        return False
    elif not info:
        return True
    else:
        for r in res:
            if r.data == info:
                return True
    return False

def goodDecode(im):
    for rot in [None, Image.FLIP_TOP_BOTTOM, Image.ROTATE_90, Image.ROTATE_180, Image.ROTATE_270]:
        res = decode(transpose(im, rot), [ZBarSymbol.QRCODE])
        if res:
            return res

    return None
