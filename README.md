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

### However:
There are also mechanisms to preconfigure an image without using Imager. To set up a user on first boot and bypass the wizard completely, create a file called userconf or userconf.txt in the boot partition of the SD card; this is the part of the SD card which can be seen when it is mounted in a Windows or MacOS computer.

This file should contain a single line of text, consisting of username:encrypted- password – so your desired username, followed immediately by a colon, followed immediately by an encrypted representation of the password you want to use.

To generate the encrypted password, the easiest way is to use OpenSSL on a Raspberry Pi that is already running – open a terminal window and enter


-----------------------------------------------------------------  
### Open terminal and enter:  
wpa_passphrase <YOUR_SSID> <YOUR_PASSWORD>  

Output:  
network={  
    ssid="YOUR_SSID"  
    #psk="YOUR_PASSWORD"  
    psk=6a24edf1592aec4465271b7dcd204601b6e78df3186ce1a62a31f40ae9630702  
}  

##### Then copy the psk line to your wpa_supplicant.conf
(See the provided wpa_supplicant.conf example)

https://unix.stackexchange.com/questions/278946/hiding-passwords-in-wpa-supplicant-conf-with-wpa-eap-and-mschap-v2


### Changing Wifi Password with Headless Pi  
add new wpa_supplicant.conf to boot directory of Pi (i.e. on micro SD card) and restart
