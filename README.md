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
