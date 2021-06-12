# Configure Raspberry Pi to run a program (ie service) at startup

From
https://www.raspberrypi.org/documentation/linux/usage/systemd.md

## Create the .service file
![image](https://user-images.githubusercontent.com/43687571/121790973-d17d0b80-cb99-11eb-82c8-b854cfc0f511.png)

## Copy to /etc/systemd/system/ as root
     sudo cp myscript.service /etc/systemd/system/myscript.service
     
## Inform systemd the new service has been added
     sudo systemctl daemon-reload
     
## Start the service
     sudo systemctl start myscript.service
     
## Enable on restart (i.e. auto start on boot/reboot)
     sudo systemctl enable myscript.service
