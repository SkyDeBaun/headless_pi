# headless_pi

## how to setup and configure Raspberry Pi headlessly
* install Raspian OS onto microSD card

Add the following to the microSD card
* add supplicant.conf (see example)
* add empty ssh file 
  * touch ssh (Linux)
  * copy NUL ssh (Windows)


Scan network for new ip
* on Windows 10 run in command console: arp -a
* Note: run before and after booting pi (and note the new addition.. that's our Pi)

Login and change the password
* default user pi
* default pass raspberry
* change password with: passwd
