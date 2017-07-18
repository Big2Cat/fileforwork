#!/usr/bin/env python
# encoding: utf-8
import PIL.Image as image
from testchrome import main
import time
import re
import cStringIO
import urllib2
import random

main()

def get_merge_image(filename, location_list):

    im = image.open(filename)

    new_im = image.new('RGB',(260, 116))

    im_list_upper = []
    im_list_dowm = []

    for location in location_list:

        if location['y'] == -58:

            im_list_upper.append(im.crop((abs(location['x']),58,abs(location['x'])+10,166)))

        if location['y'] == 0:

            im_list_dowm.append(im.crop((abs(location['x']),0,abs(location['x'])+10,58)))

    x_offset = 0

    for im in im_list_upper:

        new_im.paste(im,(x_offset,0))
        x_offset += im.size[0]

    x_offset = 0

    for im in im_list_dowm:

        new_im.paste(im,(x_offset,58))
        x_offset += im.size[0]

    return new_im

def get_image(driver, div):


    background_images = driver.find_elements_by_xpath(div)

    location_list = []

    imageurl = ''

    for background_image in background_images:

        location = {}

        location['x']=int(re.findall("background-image: url\(\"(.*)\"\); background-position: (.*)px (.*)px;",background_image.get_attribute('style'))[0][1])
        location['y']=int(re.findall("background-image: url\(\"(.*)\"\); background-position: (.*)px (.*)px;",background_image.get_attribute('style'))[0][2])
        imageurl=re.findall("background-image: url\(\"(.*)\"\); background-position: (.*)px (.*)px;",background_image.get_attribute('style'))[0][0]

        location_list.append(location)

    imageurl = imageurl.replace('webp','jpg')

    jpgfile = cStringIO.StringIO(urllib2.urlopen(imageurl).read())

    image = get_merge_image(jpgfile,location_list)
    image.show()
    #return image
get_image()

'''
def is_similar(image1,image2,x,y):


    pixel1 = image1.getpixel((x,y))
    pixel2 = image2.getpixel((x,y))

    for i in range(0,3):
        if abs(pixel1[i]-pixel2[i])>=50:
            return False

    return True

def get_diff_location(image1,image2):


    i = 0

    for i in range(0,260):
        for j in range(0, 116):
            if is_similar(image1,image2,i,j)==False:
                return i


'''

