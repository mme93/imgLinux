import base64
from PIL import Image
from io import BytesIO

class Base64Coder:
    print("Ich bin ein Base64Coder")
    
    def createImgFromString(self):
        with open('./app/image.txt') as f:
            lines = f.readlines()
            str1 = ''.join(lines)
            im = Image.open(BytesIO(base64.b64decode(str1)))
            im.save('./app/image1.png', 'PNG')
