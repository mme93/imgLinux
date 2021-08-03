from base64Coder import Base64Coder
from utils import Utils
from PIL import Image

class Main:
    base64Coder = Base64Coder()
    base64Coder.createImgFromString()
    utils=Utils()
    utils.calibrateImage('scan1','app/scan1.jpg')
    image = Image.open('app/cutImg/scan1_calibrate.jpg')
    image.show()