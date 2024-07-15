from PIL import Image, ImageFont, ImageDraw
import os
from datetime import datetime
from Myclass.log import log
from configparser import ConfigParser
from Myclass.config import config


class watermark:
    def __init__(self):
        self.config = config.get()
        self.path_dir = self.config['export_image_path']['value']
        
    def watermark_image(self,item):
        self.font = ImageFont.truetype('c:\\snapshot\\micross.ttf', 36, index = 0) if '/buy/' in item[2] else ImageFont.truetype('c:\\snapshot\\micross.ttf', 24, index = 0) 

        self.image = Image.open("c:\\snapshot\\images\\r_" + str(item[0]) + "_"+str(item[1]) + ".png")
        self.date = datetime.fromisoformat(str(item[3]))

        text = str(item[0]) + "_" + str(item[1]) + "(" + self.date.strftime("%Y%m/%d") + ")"
        rgba_image = self.image.convert('RGBA')

        text_overlay = Image.new('RGBA', rgba_image.width, rgba_image.height, (255, 255, 255, 0))
        image_draw = ImageDraw.Draw(text_overlay)

        text_size_x, text_size_y = image_draw.textsize(text, font=self.font)
        text_image = Image.new('RGBA', (text_size_x, text_size_y), (255, 255, 255, 0))
        text_draw = ImageDraw.Draw(text_image)
        text_draw.text((0, 0), text, font=self.font, fill=(int(self.config['watermark_text_color']['r_value']), int(self.config['watermark_text_color']['g_value']), int(self.config['watermark_text_color']['b_value']), 100))

        angle = 45  
        rotated_text_image = text_image.rotate(angle, expand=1)

        text_x = (rgba_image.width - rotated_text_image.width) // 2
        text_y = (rgba_image.height - rotated_text_image.height) // 2
        text_overlay.paste(rotated_text_image, (text_x, text_y), rotated_text_image)

        image_with_text = Image.alpha_composite(rgba_image, text_overlay)

        return image_with_text
    
        
    
