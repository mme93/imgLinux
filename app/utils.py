import numpy as np
import cv2
import statistics
from PIL import Image

class Utils:

    def calibrateImage(self,imageName,path):
        print('Calibrate Img')
        self.croppedImg(path,imageName)
        path='app/cutImg/'+imageName+'_calibrate.jpg'
        self.rotetImg(180,path)   
        self.croppedImg(path,imageName)
        self.rotetImg(180,path)
    
    def croppedImg(self,path,imageName):
        print('Start to cut Image: '+imageName)
        image = cv2.imread(path)            
        height = np.size(image, 0)
        width = np.size(image, 1)
        #Linke Seite wird ermittelt
        maxLeftSizeList=[]
        for i in range(0, height):
            for j in range(0, width):
                imgArray=image[i,j]
                averageRGB=(imgArray.item(0)+imgArray.item(1)+imgArray.item(2))/3
                if averageRGB<241:        
                    maxLeftSizeList.append(j)
                    break
        left=int(statistics.mean(maxLeftSizeList))
        if left<200:
            left=int(left/3);              
        else:
            left=int(left/100*97)

        #Ober Seite wird ermittelt         
        maxTopSizeList=[]
        for i in range(0, width):
            for j in range(0, height):
                imgArray=image[j,i]
                averageRGB=(imgArray.item(0)+imgArray.item(1)+imgArray.item(2))/3
                if averageRGB<241:        
                    maxTopSizeList.append(j)
                    break
        top=int(statistics.mean(maxTopSizeList))
        if top<200:
            top=int(top/3);              
        else:
            top=int(top/100*97)

        cropped = image[top:height,left:width]
        path='app/cutImg/'+imageName+'_calibrate.jpg'
        cv2.imwrite(path,cropped)

    def rotetImg(self, percent,path):
        try:
            bild = Image.open(path)
            neuesbild = bild.rotate(percent)
            neuesbild.save(path)
        except IOError:
            print("Fehler: kann %s nicht bearbeiten." % path)

    

