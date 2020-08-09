apt update -y
apt upgrade -y
pkg install git -y
pkg install golang -y
export GOPATH=/data/data/com.termux/files/home/go
echo
echo
echo -e "\e[32m\e[1m Wait Until Done !!! Message"
echo
echo
echo
echo -e "\e[1m ðŸ•¦ 5-6 Minutes Wait Karo...Ye Aapke â†• Internet Speed Par Depend Karta He â˜‘ Done ðŸ“¨ Message Na Aaye Tab tak ðŸ•š Wait Karo..."
go get -u -v github.com/kataras/iris
clear
pkg install figlet -y
pkg install ruby -y
gem install lolcat
clear
cd /sdcard
mkdir Alien-Host
cd $HOME/Alien-Host/src/photo
mv * /sdcard/Alien-Host
cd $HOME/Alien-Host/src
rm -rvf photo
cd $HOME
clear
figlet -f big "   Done..!!" | lolcat
