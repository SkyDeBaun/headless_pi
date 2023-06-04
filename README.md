# Setup and configure Raspberry Pi headlessly
* Download and install Raspian OS onto microSD card
* I like Balena Etcher for this

### Add supplicant.conf and ssh to the microSD card
* Create supplicant.conf (see provided example)
* Create empty ssh file (no file extension)
  * touch ssh (Linux)
  * copy NUL ssh (Windows)


### Scan network for new ip (needed for SSH access)
* On Windows 10 run in command console: arp -a
* Note: run before and after booting pi (and note the new addition.. that's our Pi)


### Login via SSH and change the password
* Default user: pi
* Default pass: raspberry
* Change password with: passwd

-------------------------------------------------------------  
##UPDATE
Was unable to login using default password using the above method.  

Instead I used the Raspberry Pi Imager program: allows configuring username, password, wifi -> super easy  
https://www.raspberrypi.com/news/raspberry-pi-bullseye-update-april-2022/

![image](https://github.com/SkyDeBaun/headless_pi/assets/43687571/85374c00-5224-414b-91e9-f7dfebf183f8)
