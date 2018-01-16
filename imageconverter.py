from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("blank_slate.jpg")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("arial.ttf", 48)
# draw.text((x, y),"Sample Text",(r,g,b))
#try to keep limit to 40 characters per line
draw.text((0, 50),"12345678901234567890123456789012345678901234567890",(0,0,0),font=font)
img.save('sample-out.jpg')



#https://stackoverflow.com/questions/16373425/add-text-on-image-using-pil