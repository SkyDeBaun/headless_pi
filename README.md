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

## Connect VS Code Remotely
Unfortunately Pi Zero does not support this feature due to low system memory

For a work around use sshfs to remotely mount the zero's file system
![image](https://user-images.githubusercontent.com/43687571/121786075-7f74bf80-cb72-11eb-9b7b-3aa78af6f8a2.png)
