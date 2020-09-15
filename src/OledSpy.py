import time
import os.path
from luma.core.interface.serial import i2c, spi
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106
from luma.core.virtual import viewport
from luma.core.render import canvas
from PIL import Image , ImageFont
import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 3000
r.dynamic_energy_threshold = True

while True:
    with sr.Microphone(chunk_size=1024, sample_rate=16000) as source:
        serial = i2c(port=1, address=0x3C)
        device = ssd1306(serial)
        virtual = viewport(device, width=device.width, height=768)
        with canvas(virtual) as draw:
            font = ImageFont.truetype("fonts/FreeSansBoldOblique.ttf", 22, encoding="unic")
            draw.text((20, 20), "Ready ...", fill="red", align="center",font=font)
            
        r.adjust_for_ambient_noise(source ,duration=0.5)
        audio = r.listen(source, timeout=None , phrase_time_limit=5)
        img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'images', 'hand.png'))
        logo = Image.open(img_path)
        with canvas(virtual) as draw:
            draw.bitmap((20, 20), logo, fill="white")
            
        try:
            outF = open("myOutFile.txt", "a")
            outF.write(" "+r.recognize_google(audio ,language= "en-US")+"\n")
            outF.close()
            OutTxt = open("myOutFile.txt" , "r")
            Last_line = OutTxt.readlines()[-1]
            x = device.width
            with canvas(device) as draw:
                font = ImageFont.truetype("fonts/FreeSans.ttf", 34, encoding="unic")
                w, h = draw.textsize(Last_line, font=font)
            virtual = viewport(device, width=max(device.width, w + x + x), height=max(h, device.height))
            with canvas(virtual) as draw:
                draw.text((x, 20), Last_line,font=font,fill="white")
            i = 0
            speed=6
            while i < x + w:
                virtual.set_position((i, 0))
                i += speed
                
        except sr.UnknownValueError:
            with canvas(virtual) as draw:
                font = ImageFont.truetype("fonts/FreeMonoBold.ttf", 22, encoding="unic")
                draw.text((20, 20), "No sound...", fill="red", align="center",font=font)
                time.sleep(5)
            print("Google Speech Recognition could not understand audio")