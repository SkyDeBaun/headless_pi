import os
from vcgencmd import Vcgencmd #monitor cpu temp (and other stuff..)

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


import time
import board
import digitalio
import adafruit_max31856




def print_temperature(thermocouple, position):
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    #get updated temperature------------------------------------
    tempC = thermocouple.temperature
    tempF = tempC * 9 / 5 + 32
    tempString = str(format(tempF, '.1f'))  #format and convert to string
  

    #get updated string(temp) size
    headingwidth, headingheight = heading_font.getsize(display_heading)
    textwidth, textheight = font.getsize(tempString)

    #calculate offset as sting grows to multiple digits
    offset = (width - textwidth)/2
    heading_offset = (width - headingwidth)/2

    #update text-------------------------------------------------
    draw.text((heading_offset,top+2), display_heading, font=heading_font, fill=255)
    draw.text((offset,top+12), tempString, font=font, fill=255)
    #draw.text((0,top+12), "Hi", font=heading_font, fill=255)

    if position == "Hi":
        draw.text((0,top+12), "Hi", font=heading_font, fill=255)
    else:
        draw.text((0,top+24), "Lo", font=heading_font, fill=255)

    #print to screen---------------------------------------------
    disp.image(image) #not just for "images!" (i.e. leave this..)
    disp.display()

    return tempString




# Create sensor object, communicating over the board's default SPI bus
spi = board.SPI()

# allocate a CS pin and set the direction

cs = digitalio.DigitalInOut(board.D5)
cs.direction = digitalio.Direction.OUTPUT

cs2 = digitalio.DigitalInOut(board.D6)
cs2.direction = digitalio.Direction.OUTPUT


# create a thermocouple object with the above
thermocouple = adafruit_max31856.MAX31856(spi, cs)
thermocouple2 = adafruit_max31856.MAX31856(spi, cs2)


#my vars-------------------------------------------------
display_heading = "T E M P E R A T U R E (F)"
my_font = "unispace.ttf"


#test MQTT self subscribe--------------------------------
os.system("mosquitto_sub -h localhost -t \"thermocouple\" &") #run MQTT subscription service in background




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


counter = 0


vcgm = Vcgencmd()



#loop---------------------------------------------------------------------------
#-------------------------------------------------------------------------------
while True:


    tempString = print_temperature(thermocouple, "Lo")   
    time.sleep(1)   
    tempString2 = print_temperature(thermocouple2, "Hi")   


    #test MQTT pub-----------------------------------------------
    if counter == 0:         
        #construct string----------------------------------------
        #os.system("mosquitto_pub -h localhost -t \"test\" -m \"hello\"")
        thermo_lo = "mosquitto_pub -h localhost -t \"thermo_low\" -m " + str(tempString)
        thermo_hi = "mosquitto_pub -h localhost -t \"thermo_high\" -m " + str(tempString2)

        #cpu temperature monitoring------------------------------
        cpu = vcgm.measure_temp()
        cpu_temp = "mosquitto_pub -h localhost -t \"cpu_temp\" -m " + str(cpu)

        os.system(thermo_lo)
        os.system(thermo_hi) 
        os.system(cpu_temp)

    time.sleep(1)

    
    #reset counter every 5 seconds
    '''
    if counter >= 4:
        counter = 0
    else:
        counter += 1
    '''

