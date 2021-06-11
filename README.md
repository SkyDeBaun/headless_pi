# headless_pi

## Setup and configure Raspberry Pi headlessly
* install Raspian OS onto microSD card

### Add supplicant.conf and ssh to the microSD card
* create supplicant.conf (see example)
* create empty ssh file 
  * touch ssh (Linux)
  * copy NUL ssh (Windows)


### Scan network for new ip (needed for SSH access)
* on Windows 10 run in command console: arp -a
* Note: run before and after booting pi (and note the new addition.. that's our Pi)


### Login via SSH and change the password
* default user: pi
* default pass: raspberry
* change password with: passwd

