dialog --title "<==[ Bhai 4 You ]==>" \
--clear \
--msgbox "\n                    Everything is Possible !! \n\n\n\n❌ Name     : Termux-Os\n\n❌ Coding   : Bash\n\n❌ Coder    : Sutariya Parixit\n\n❌ Sec.Code : 8h4i\n\n❌ Site     : https://bhai4you.blogspot.com\n\n❌ Github   : github.com/Bhai4You\n\n❌ Date     : 25-jan-18" 25 71
redirection
: ${DIALOG_OK=0} ${DIALOG_CANCEL=1} ${DIALOG_HELP=2}
: ${DIALOG_EXTRA=3} ${DIALOG_ITEM_HELP=4} ${DIALOG_ESC=255}
exec 3>&1
Os=$(dialog --title "<==[ Termux-Os ]==>" \
--clear \
--msgbox "\n                      All in One Termux Os !! \n\n\n\n Termux-Os by 8h4i\n\n❌ 1] Arch\n❌ 2] Blackarch\n❌ 3] ArchStrike\n❌ 4] Debian\n❌ 5] Fedora (arm)\n❌ 6] Fedora (arm64)\n❌ 7] Kalinethunter\n❌ 8] Ubuntu\n❌ 0] exit\n\n\n Choose Your Target Os Number and Put Target Os Number in Input Box..!!!" 25 71 2>&1 1>&3)
return_value=$?
exec 3>&-
case $return_value in
$DIALOG_OK)
redirection
: ${DIALOG_OK=0} ${DIALOG_CANCEL=1} ${DIALOG_HELP=2}
: ${DIALOG_EXTRA=3} ${DIALOG_ITEM_HELP=4} ${DIALOG_ESC=255}
exec 3>&1
os=$(dialog --title "<==[ Termux-Os ]==>" \
--clear  \
--inputbox  "\n           All in One Termux Os !! \n\n\n\n Enter Your Target-Os Number\n\n " 16 51 2>&1 1>&3)
return_value=$?
exec 3>&-
echo
echo
echo
echo " Searching Your Os : $os"
echo
echo
echo -e "\e[1m\e[33mSetup \e[36m$os Os\e[33m...!! \e[31m(Wait)\e[0m"
sleep 3
apt install git -y
clear
;;
esac
clear
sleep 4
if [ $os == '1' ]
then
clear
echo -e "\e[1m\e[36m ARCH LINUX IS INSTALLING IN TERMUX..!" | pv -qL 10;
sleep 1
clear
figlet -f pagga '       Arch linux        ' | lolcat
echo
echo
echo -e "\e[1m\e[33m Arch Linux Installation...!!! \e[0m"
echo
echo
pkg install wget -y
cd $HOME
mkdir Arch-Os
cd Arch-Os
wget https://raw.githubusercontent.com/sdrausty/TermuxArch/master/setupTermuxArch.sh
bash setupTermuxArch.sh
elif [ $os == '2' ]
then
clear
echo
figlet -f Cyberlarge.flf "Blackarch" | lolcat
echo -e "\e[1m\e[31m     <------------❌\e[36m  H A C K E R ' S   O S \e[31m ❌------------>\e[0m"
echo
echo
echo
echo -e "\e[1m\e[32mInstallation Step :\e[0m"
echo
echo
echo -e "\e[1m\e[31m1)\e[33m Install Arch Linux in Termux\n\n\e[31m2)\e[33m startarch\n\n\e[31m3)\e[33m cd /etc\n\n\e[31m4) \e[33mecho '[blackarch]
Server = http://blackarch.org/blackarch/$repo/os/\$arch' >> pacman.conf\n\n\e[31m5) \e[33mpacman -Syu\n\n\e[31m6)\e[33m pacman -S blackarch"
echo
echo
echo
elif [ $os == '3' ]
then
clear
echo
figlet -f Cyberlarge.flf "Archstrike" | lolcat
echo -e "\e[1m\e[31m     <------------❌\e[36m  B A A P     O F     L I N U X \e[31m ❌------------>\e[0m"
echo
echo
echo
echo -e "\e[1m\e[32mInstallation Step :\e[0m"
echo
echo
echo -e "\e[1m\e[31m1)\e[33m Install Arch Linux in Termux\n\n\e[31m2)\e[33m startarch\n\n\e[31m3)\e[33m cd /etc\n\n\e[31m4) \e[33mecho '[archstrike]
Server = https://mirror.archstrike.org/$arch/$repo' >> pacman.conf\n\n\e[31m5) \e[33mpacman -Syu\n\n\e[31m6)\e[33m pacman -S archstrike"
echo
echo
echo
elif [ $os == '4' ]
then
clear
echo -e "\e[1m\e[36m DEBIAN IS INSTALLING IN TERMUX..!!" | pv -qL 10;
sleep 1
clear
figlet -f pagga '       Debian        ' | lolcat
echo
echo
echo -e "\e[1m\e[33m Debian Installation...!!! \e[0m"
echo
echo
cd $HOME
apt update
apt install wget -y
hash -r
sleep
wget https://raw.githubusercontent.com/sp4rkie/debian-on-termux/master/debian_on_termux.sh
sh debian_on_termux.sh
tail -F $HOME/deboot_debian/debootstrap/debootstrap.log
echo
echo
echo "type below command to run Debian os in Termux..!!"
echo
echo -e "\e[1m\e[32m$HOME/bin/enter_deb\e[0m"
elif [ $os == '5' ]
then
clear
echo -e "\e[1m\e[36m FEDORA_(arm) IS INSTALLING IN TERMUX..!" | pv -qL 10;
sleep 1
clear
figlet -f pagga '       Fedora Arm       ' | lolcat
echo
echo
echo -e "\e[1m\e[33m Fedora_arm Installation...!!! \e[0m"
echo
echo
pkg install wget -y
cd $HOME
mkdir Fedora-Os
cd Fedora-Os
wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh
chmod +x termux-fedora.sh
clear
echo
echo
echo
echo
bash termux-fedora.sh f26_arm
elif [ $os == '6' ]
then
clear
echo -e "\e[1m\e[36m FEDORA_(arm64) IS INSTALLING IN TERMUX..!" | pv -qL 10;
sleep 1
clear
figlet -f pagga '       Fedora arm64        ' | lolcat
echo
echo
echo -e "\e[1m\e[33m Fedora_arm64 Installation...!!! \e[0m"
echo
echo
pkg install wget -y
cd $HOME
mkdir Fedora-Os
cd Fedora-Os
wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh
chmod +x termux-fedora.sh
clear
echo
echo
echo
echo
bash termux-fedora.sh f26_arm64
elif [ $os == '7' ]
then
clear
echo -e "\e[1m\e[36m KALINETHUNTER IS INSTALLING IN TERMUX..!" | pv -qL 10;
sleep 1
clear
figlet -f pagga '       Kali nethunter      ' | lolcat
echo
echo
echo -e "\e[1m\e[33m KaliNethunter Installation...!!! \e[0m"
echo
echo
pkg install wget -y
cd $HOME
mkdir Kali-Os
cd Kali-Os
wget https://raw.githubusercontent.com/Hax4us/Nethunter-In-Termux/master/kalinethunter
chmod +x kalinethunter
bash kalinethunter
elif [ $os == '8' ]
then
clear
echo -e "\e[1m\e[36m UBUNTU IS INSTALLING IN TERMUX..!" | pv -qL 10;
sleep 1
clear
figlet -f pagga '       UBUNTU        ' | lolcat
echo
echo
echo -e "\e[1m\e[33m UBUNTU Installation...!!! \e[0m"
echo
echo
cd $HOME
mkdir Ubuntu-Os
cd Ubuntu-Os
pkg install wget -y
wget https://raw.githubusercontent.com/Neo-Oli/termux-ubuntu/master/ubuntu.sh
chmod +x ubuntu.sh
echo
echo
bash ubuntu.sh
cd $HOME
cd Ubuntu-Os
bash start.sh
clear
elif [ $os == '0' ]
then
clear
echo "Exit Termux-Os...!!!" | pv -qL 10;
exit
else
clear
figlet -f pagga '      Wrong Input !!        ' | lolcat
fi
