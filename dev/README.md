Setup Environment WSL:
Tested on Windows version:
Microsoft Windows [Version 10.0.18362.836]
This build uses WSL 1
Linux Kernel: 4.4.0-18362-Microsoft
lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.4 LTS
Release:        18.04
Codename:       bionic

sudo apt-get install python-pip

Download Atom from the official website in Windows.
Add Atom to the windows environment variables.
- Run the following: win+rand type in SystemPropertiesAdvanced.exe
- Open: Environment Variables
- Add your Atom path:
C:\Users\<user-name>\AppData\Local\atom\bin
Go into the WSL and add an alias for Atom in your bashrc file:
- Open your bash configuration: vim ~/.bashrc
- Add to the end of the file and save/exit:
alias atom=”/mnt/c/Windows/System32/cmd.exe /c 'atom'"
- Update your bash profile: source ~/.bashrc
Now you can use atom . & to open your python projects from WSL command line.

Needed to install python-tk
sudo apt-get install python-tk

Error:
ValueError: Only know how to handle extensions: [u'png']; with Pillow installed matplotlib can handle more images

Fix:
pip install Pillow

Error:
_tkinter.TclError: no display name and no $DISPLAY environment variable

Fix:
Install Xming X Server for Windows
X Window System Server for Windows
https://sourceforge.net/projects/xming/
At the following to end of ~/.bashrc
export DISPLAY=:0;

# At this point jpg and png files should be working.
