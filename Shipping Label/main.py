from PIL import Image, ImageDraw, ImageFont
from barcode import EAN13
from barcode.writer import ImageWriter
import Util


def get_concat_v_blank(im1, im2, color=(0, 0, 0)):
    dst = Image.new('RGB', (max(im1.width, im2.width), im1.height + im2.height), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

returnOne = input("Reciever's Name: ")
returnTwo = input("Reciever's Address: ")
returnThree = input("Apt-Suite: ")
returnFour = input("Recievers Phone Number: ")
returnAddress = (returnOne+"\n"+returnTwo+"\n"+returnThree+"\n"+returnFour)
shipOne = input("Sender's Name: ")
shipTwo = input("Sender's Address: ")
shipThree = input("Apt-Suite: ")
shipFour = input("Sender's Phone Number: ")
shipAddress = (shipOne+"\n"+shipTwo+"\n"+shipThree+"\n"+shipFour)


img_bfr = Image.new('RGB', (500, 550), color=(255, 255, 255))


titleFont = ImageFont.truetype(r'/Library/Fonts/Arial.ttf', 80)
companyFont = ImageFont.truetype(r'/Library/Fonts/Arial.ttf', 40)
returnAddressFont = ImageFont.truetype(r'/Library/Fonts/Arial.ttf', 20)
postageWarningFont = ImageFont.truetype(r'/Library/Fonts/Arial.ttf', 20)
shipToFont = ImageFont.truetype(r'/Library/Fonts/Arial.ttf', 15)
shippingAddressFont = ImageFont.truetype(r'/Library/Fonts/Arial.ttf', 25)

number = Util.generateBarCode(13)
while(Util.contains(number)):
    number = Util.generateBarCode(13)
Util.insert(str(number))
barcode = EAN13(str(number), writer=ImageWriter())
barcode.save("barcode")
barcodeImage = Image.open(r'barcode.png')

get_concat_v_blank(img_bfr, barcodeImage, (255, 255, 255)).save('blank.jpg')

Util.stop()

img_new = Image.open('blank.jpg')
d = ImageDraw.Draw(img_new)

width = 523
height = 830


d.line((0, 0, 0, height), fill=(0, 0, 0), width=6)
d.line((0, 0, width, 0), fill=(0, 0, 0), width=6)
d.line((width, 0, width, height), fill=(0, 0, 0), width=10)
d.line((0, height, width, height), fill=(0, 0, 0), width=12)

d.text((180, 0), "PSS", font=titleFont, align="center", fill=(0, 0, 0))
d.line((0, 100, width, 100), fill=(0, 0, 0), width=3)

d.text((20, 110), "Premier Shipping Services", font=companyFont, align="center", fill=(0, 0, 0))
d.line((0, 160, width, 160), fill=(0, 0, 0), width=3)

d.text((30, 170), shipAddress,
       font=returnAddressFont, fill=(0, 0, 0))#150
d.text((100, 270), "NO POSTAGE STAMP NECESSARY\nPOSTAGE HAS BEEN PREPAID ", font=postageWarningFont, fill=(0, 0, 0))
d.text((25, 350), "SHIP TO:", font=shipToFont, fill=(0, 0, 0))
d.text((120, 370), returnAddress,
       font=shippingAddressFont, fill=(0, 0, 0))
d.line((0, 500, width, 500), fill=(0, 0, 0), width=3)

img_new.save('output.jpg')

img_label = Image.open('output.jpg')

img_back = Image.new('RGB', (900, 900), color=(255, 255, 255))


def fin_save(im1, im2):
	img = Image.new('RGB', (900, 900), color=(255, 255, 255))
	img.paste(im2, (200,25))
	return img

fin_save(img_back, img_label).save('LABEL.jpg')





