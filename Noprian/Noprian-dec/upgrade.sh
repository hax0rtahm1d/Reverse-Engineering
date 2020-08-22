#!/bin/bash
#upgrade.sh
clear
#color
blue='\e[1;34m'
green='\e[0;23m'
purple='\e[1;35m'
cyan='\e[1;36m'
red='\e[1;31m'

echo -e $purple "Upgrade... Tool $Cyan AllTools"
sleep 2
echo -e $red "Loading..."
sleep 2
cd $HOME/FBH
rm -rf MKBRUTUS
rm -rf .FBH .call.php .wa.php .create.py .FBHtarget.py .FBHrombongan.py .hammer.py .wifite.py setup .upgrade.sh .Bot.py .cloning.py
sleep 1
curl -o .FBH https://raw.githubusercontent.com/BLackWhite0711/Noprian/master/.FBH
curl -o .FBHtarget.py https://raw.githubusercontent.com/BLackWhite0711/Noprian/master/.FBHtarget.py
curl -o .FBHrombongan.py https://raw.githubusercontent.com/BLackWhite0711/Noprian/master/.FBHrombongan.py
curl -o .call.php https://raw.githubusercontent.com/BLackWhite0711/Noprian/master/.call.php
curl -o .wifite.py https://raw.githubusercontent.com/BLackWhite0711/Noprian/master/.wifite.py
curl -o .wa.php https://raw.githubusercontent.com/BLackWhite0711/Noprian/master/.wa.php
curl -o .hammer.py https://raw.githubusercontent.com/BLackWhite0711/Noprian/master/.hammer.py
curl -o setup https://raw.githubusercontent.com/BLackWhite0711/Noprian/master/setup
curl -o .create.py https://raw.githubusercontent.com/BLackWhite0711/Noprian/master/.create.py
curl -o .upgrade.sh https://raw.githubusercontent.com/BLackWhite0711/Noprian/master/.upgrade.sh
curl -o .Bot.py https://raw.githubusercontent.com/BLackWhite0711/Noprian/master/.Bot.py
curl -o .cloning.py https://raw.githubusercontent.com/BLackWhite0711/Noprian/master/.cloning.py
sleep 2


chmod +x *
clear
bash 
bash .FBH
