from PIL import Image,ImageDraw,ImageFont
import pandas as pd
import os
import sys


filename = sys.argv[1]
font_file = sys.argv[2]
font_size = sys.argv[3]
font_size = int(font_size)
input_template_certificate = sys.argv[4]
output_folder = sys.argv[5]

df = pd.read_csv(filename, encoding = "utf-8")

font = ImageFont.truetype(font_file,font_size)

path = os.getcwd() + "\\" + output_folder
output_folder_check = os.path.exists(path)
if(output_folder_check):
	pass
else:
	os.mkdir(path)

img = Image.open(input_template_certificate)
image_width = img.width
image_height = img.height

print("**************")
for index,j in df.iterrows():
	img = Image.open(input_template_certificate)
	draw = ImageDraw.Draw(img)
	message = text='{}'.format(j[0])
	_, _, w, h = draw.textbbox((0, 0), message, font=font)
	draw.text(((image_width-w)/2, (image_height-h)/2),text='{}'.format(j[0]),fill=(0,0,0),font=font,align='Left')
	output_file =  output_folder + '/{}.jpg'.format(j[0])
	img.save(output_file)
	print(output_file + " Saved")

print("**************")

# python3 certificate.py list.csv Charm-Bold.ttf 60 certificate_template.jpg output_certificate