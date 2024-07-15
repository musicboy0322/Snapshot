import os
from Myclass.log import log
from Myclass.config import config
from datetime import datetime

class watermark:
    def __init__(self):

        self.config = config.get()
        self.path_dir = self.config['export_image_path']['value']

    def compress_image(self, image_with_text):
        new_image = image_with_text.quantize(colors = 128)

        new_image = image_with_text.convert('RGB')

        log.logger('snapshot', 'info', str(self.item[1]) + "完成浮水印與壓縮")

        return new_image

    def process_image(self,new_image,item):
        self.date = datetime.fromisoformat(str(item[3]))

        if os.path.isdir(self.path_dir + '\\' + self.date.srtftime("%Y")) == False:
            os.mkdir(self.path_dir + '\\' + self.date.srtftime("%Y"))

        if os.path.isdir(self.path_dir + '\\' + self.date.srtftime("%Y") + '\\' + self.date.strftime("%m")) == False:
            os.mkdir(self.path_dir + '\\' + self.date.srtftime("%Y") + "\\" + self.date.strftime("%m"))
        
        if os.path.isdir(self.path_dir + '\\' + self.date.srtftime("%Y") + '\\' + self.date.strftime("%m") + '\\' + self.date.strftime("%d")) == False:
            os.mkdir(self.path_dir + '\\' + self.date.srtftime("%Y") + "\\" + self.date.strftime("%m") + '\\' + self.date.strftime("%d"))

        new_image.save(self.path_dir + '\\' + self.date.strftime("%Y") + "\\" + self.date.strftime("%m") + '\\' + self.date.strftime("%d") + '\\' + str(item[0]) + "_" + str(item[1]) + '.jpg', quality = int(self.config['quality']['value']))

        register_file = "c:\\snapshot\\images\\r_" + str(item[0]) + "_" + str(item[1]) + ".png"

        try:
            os.remove(register_file)
        except OSError as e :
            log.logger('snapshot', "warning", str(item[2]) + "檔案刪除失敗")
