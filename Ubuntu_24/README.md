
# New Rapberry Pi 5 Install
Attempting to setup the image such that on first boot ssh is enabled and the Pi autoconnects to my network. This will fascilitate an easy to use headless Pi.

## How to
- I use Raspberry Pi Imager to write Ubuntu Desktop 24.04.1 LTS (ubuntu-24.04.1-preinstalled-desktop-arm64+raspi.img.xz) to the SD card (despite primary use as Headless Pi, the desktop is useful.. so I may install this version)
- I will use the Pi Imager's (pre)configuration option to setup wifi and username/password (avoids issues specifing the correct wpa_supplicant.conf configuration)

## After booting up and seeing successful connection to my hotspot 
- I connect both Windows 10 laptop and Pi to my mobile hotspot
- Find the Pi's IP -> Use Win + R key and enter 'arp -a'
- Find the Pi's IP
- Alternatively.. when using hotspot the IP is available under the small "info" icon at top right of the device (after clicking the device name)

## Now that I have the Pi's IP
- Create ssh config for the pi (this is in my Ubuntu Virtual Machine running on Win 10 as I prefere to use Linux environment for this kind of work)

## After login
- create an rsa key and copy the public key to my local machine's known host file
- Edit '/etc/ssh/sshd_config' to enable:
    - PubkeyAuthentication yes
    - AuthorizedKeysFile .ssh/authorized_keys
    - AgentForwarding yes

- Next restart the ssh service
    - sudo systemctl restart ssh (this hung for me.. which makes some sense as I was connected via ssh)
    - alternatively: sudo reboot

 ## Install requirements
 - sudo apt-get update
 - sudo apt-get install build-essential
 - sudo apt-get install autoconf automake
 - sudo apt-get install make
 - sudo apt-get install libtool


 
## Install MBEDTLS
- download mbedtls 2.x release from Github repo: https://github.com/Mbed-TLS/mbedtls/releases
- verify the downloaded file's hash using this command: sha256sum <filename>
- install bzip utility (needed to extract .bz2 files)
- unzip: tar -xjf <filename> (only if the hash matches)
- build and install with:
    - make SHARED=1
    - sudo make install


## BPSec Requirements
For general logging and to enable the python regression test the following environmental variable must be set
- ION_RUN_EXPERT="yes"
- On Linux (bash) use: export ION_RUN_EXPERT="yes"
- On Solaris (tcsh) use: setenv ION_RUN_EXPERT "yes"


## Install ION
- since I enabled agent forwarding.. I can simply use my local key to git clone ION (using by github_rsa key)
- git clone
- git fetch
- git switch <branch>
- autoreconf -fi
- ./configure --enable-crypto-mbedtls --enable-bpsec-debugging
- make -j4
- sudo make install
- sudo ldconfig

### Build test binaries
- make test

  

  
