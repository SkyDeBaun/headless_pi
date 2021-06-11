# Setup MAX31856
https://learn.adafruit.com/thermocouple/python-circuitpython  


## Update Pi
     sudo apt-get update
     sudo apt-get upgrade
     sudo apt-get install python3-pip
     sudo pip3 install --upgrade setuptools

## Install Adafruit components
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi  

     cd ~
     sudo pip3 install --upgrade adafruit-python-shell
     wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
     sudo python3 raspi-blinka.py
     
## Check 12C and SPI
     ls /dev/i2c* /dev/spi*
   
You should see the response:
* /dev/i2c-1 /dev/spidev0.0 /dev/spidev0.1

## Connect the MAX 31856 to Pi

![image](https://user-images.githubusercontent.com/43687571/121630905-e723f100-ca32-11eb-86f0-2bd269bfe128.png)


## Install MAX31856 Library
     sudo pip3 install adafruit-circuitpython-max31856

## Example Code
![image](https://user-images.githubusercontent.com/43687571/121631190-729d8200-ca33-11eb-91de-f461a88c3bbd.png)

Note the different model number used
