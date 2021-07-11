# Setup MAX31856
https://learn.adafruit.com/thermocouple/python-circuitpython  


## Update Pi
     sudo apt-get update
     sudo apt-get upgrade
     sudo apt-get install python3-pip
     sudo pip3 install --upgrade setuptools

## Install Adafruit components (enable SPI 0 and I2C. See link to enable SPI 1)
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi  

     cd ~
     sudo pip3 install --upgrade adafruit-python-shell
     wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
     sudo python3 raspi-blinka.py
     
     
 Reboot when prompted  
     
## Check 12C and SPI
     ls /dev/i2c* /dev/spi*
   
You should see the response:
* /dev/i2c-1 /dev/spidev0.0 /dev/spidev0.1

## Connect the MAX 31856 to Pi

![image](https://user-images.githubusercontent.com/43687571/121639226-13466e80-ca41-11eb-91f3-908dcdfe75c6.png)



## Install MAX31856 Library
https://learn.adafruit.com/adafruit-max31856-thermocouple-amplifier/python-circuitpython  
     sudo pip3 install adafruit-circuitpython-max31856

## Example Code
![image](https://user-images.githubusercontent.com/43687571/121639462-6b7d7080-ca41-11eb-9d65-6648cda9c668.png)

and with a loop and temperature conversion (example from MAX31855)
![image](https://user-images.githubusercontent.com/43687571/121640533-e85d1a00-ca42-11eb-8771-c59a804dee29.png)


