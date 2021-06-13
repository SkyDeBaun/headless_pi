import os

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


import time
import board
import digitalio
import adafruit_max31856

# Create sensor object, communicating over the board's default SPI bus
spi = board.SPI()

# allocate a CS pin and set the direction
cs = digitalio.DigitalInOut(board.D5)
cs.direction = digitalio.Direction.OUTPUT

# create a thermocouple object with the above
thermocouple = adafruit_max31856.MAX31856(spi, cs)


#my vars-------------------------------------------------
display_heading = "T E M P E R A T U R E (F)"
my_font = "unispace.ttf"


#configuration for LED screen----------------------------
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0


# init 128x32 display with hardware I2C------------------
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

#initialize display-------------------------------------
disp.begin()

#clear display------------------------------------------
disp.clear()
disp.display()

#create blank image for drawing-------------------------
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))


#create drawing object to draw on image-----------------
draw = ImageDraw.Draw(image)

#draw a black filled box to clear the image-------------
draw.rectangle((0,0,width,height), outline=0, fill=0)

# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
x = 0 #horizontal offset (from left)

# default font
#font = ImageFont.load_default()

#create fonts for display--------------------------------
heading_font = ImageFont.truetype(my_font, 8)
font = ImageFont.truetype(my_font, 24)


#loop---------------------------------------------------------------------------
#-------------------------------------------------------------------------------
while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    #get updated temperature------------------------------------
    tempC = thermocouple.temperature
    tempF = tempC * 9 / 5 + 32
    tempString = str(format(tempF, '.1f'))  #format and convert to string

    #test MQTT pub-----------------------------------------------
    if tempF > 150:
        os.system("mosquitto_pub -h localhost -t \"test\" -m \"hello\"")



    #get updated string(temp) size
    headingwidth, headingheight = heading_font.getsize(display_heading)
    textwidth, textheight = font.getsize(tempString)


    #calculate offset as sting grows to multiple digits
    offset = (width - textwidth)/2
    heading_offset = (width - headingwidth)/2

    #update text-------------------------------------------------
    draw.text((heading_offset,top+2), display_heading, font=heading_font, fill=255)
    draw.text((offset,top+12), tempString, font=font, fill=255)


    #print to screen---------------------------------------------
    disp.image(image)
    disp.display()
    time.sleep(1)
