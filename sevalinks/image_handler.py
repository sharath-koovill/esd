import classifieds.settings as settings
from PIL import Image
from urllib import urlretrieve
from mimetypes import guess_extension, guess_type
import tempfile
import re, os
import uuid

def save_from_base64(postDict):
    imageDict = postDict["user_image_values"]
    imageDict = eval(imageDict)
    print imageDict
    imageOriginalWidth = imageDict["imageOriginalWidth"]
    imageOriginalHeight = imageDict["imageOriginalHeight"]
    imageWidth = imageDict["imageWidth"]
    imageHeight = imageDict["imageHeight"]
    width = imageDict["width"]
    height = imageDict["height"]
    #left = abs(imageDict["left"])
    #top = abs(imageDict["top"])
    left = 0
    top = 0
    right = left + imageDict["width"]
    bottom = top + imageDict["height"]
    filename, m = urlretrieve(imageDict['data'])
    print filename
    print "==========="
    print guess_type(imageDict['data'])
    print guess_extension(guess_type(imageDict['data'])[0])
    print tempfile.gettempdir()
    print left, top, right, bottom
    imageData = re.sub('^data:image/.+;base64,', '', imageDict['data'])
    extension = guess_extension(guess_type(imageDict['data'])[0])
    uuidStr = str(uuid.uuid4())
    tempName = uuidStr + extension
    imageName = uuidStr + ".png"
    #scaleSize = (imageWidth, imageHeight)
    scaleSize = (200, 200)    
    tmpImage = save_image_temp(imageData, tempName)
    tmpConvImage = image_format_change(tmpImage, imageName)
    tmpConvImage = scale_image(scaleSize, tmpConvImage)
    imageBox = (left, top, right, bottom)
    userImageName = crop_and_save(tmpConvImage, imageName, imageBox)
    return userImageName    

def crop_and_save(imagePath, imageName, imageBox):
    img = Image.open(imagePath)
    print settings.STATIC_LOCAL
    localPath = os.path.join(settings.STATIC_LOCAL, imageName)
    #crop((left, top, right, bottom))    
    img2 = img.crop(imageBox)
    img2.save(localPath)
    return imageName
    
def save_image_temp(imgData, imageName):
    imagePath = os.path.join(tempfile.gettempdir(), imageName)
    fh = open(imagePath, "wb")
    fh.write(imgData.decode('base64'))
    fh.close()
    return imagePath

def image_format_change(imagePath, newName):
    newPath = os.path.join(tempfile.gettempdir(), newName)
    img = Image.open(imagePath)    
    img.save(newPath)
    return newPath

def scale_image(scaleSize, imagePath):
    img = Image.open(imagePath)
    img.thumbnail(scaleSize, Image.ANTIALIAS)
    img.save(imagePath)
    return imagePath

def save_image_local(imageName):    
    fh = open(imagePath, "wb")
    fh.write(imgData.decode('base64'))
    fh.close()
    return imagePath