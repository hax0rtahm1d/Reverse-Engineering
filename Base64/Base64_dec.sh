clear
banner(){
toilet -t -f pagga  "    Base64    " -F border | lolcat
echo -e "      All in One Encryption Tools"
echo
echo
}
req(){
command -v nodejs-lts > /dev/null 2>&1 || { echo >&2 "...";clear;echo "";echo "";echo "[^^] Requirement Installing...";pkg install nodejs-lts -y;clear;}
command -v bash-obfuscate > /dev/null 2>&1 || { echo >&2 "...";clear;echo "";echo "";echo "[^^] Requirement Installing...";npm install -g bash-obfuscate;clear;}
command -v toilet > /dev/null 2>&1 || { echo >&2 "...";clear;echo "";echo "";echo "[^^] Requirement Installing...";pkg install toilet -y;clear;}
command -v python > /dev/null 2>&1 || { echo >&2 "...";clear;echo "";echo "";echo "[^^] Requirement Installing...";pkg install python -y;clear;}
command -v python2 > /dev/null 2>&1 || { echo >&2 "...";clear;echo "";echo "";echo "[^^] Requirement Installing...";pkg install python2 -y;clear;}
command -v lolcat > /dev/null 2>&1 || { echo >&2 "...";clear;echo "";echo "";echo "[^^] Requirement Installing...";pip2 install lolcat;clear;}
}
echo
menu(){
echo -e "\e[1m1. \e[36m\e[1mEncrypt\e[0m\e[1m"
sleep 0.2
echo -e "2. \e[36m\e[1mRun Script Generator\e[0m\e[1m"
sleep 0.2
echo -e "3. \e[36m\e[1mAbout Us\e[0m\e[1m"
sleep 0.2
echo
echo
printf "\e[33m\e[1mSelect Option : \e[0m\e[1m"
read option
if [ -z "$option" ]; then
exit 1
fi
if [ "$option" -eq 1 ]; then
clear
banner
sleep 0.4
echo -e "First Move Your Script File in Bash64 Folder Then Continue...^^)"
echo "Ex., Bull.sh"
echo
echo
printf "\e[33m\e[1mScript Name :\e[92m\e[1m "
read location
clear
banner
echo "Ex., Bullenc.sh, Bullenc.py, Bullenc.php.."
echo
echo
printf "\e[33m\e[1mEncrypted Script Name :\e[92m\e[1m "
read name
clear
base64 -i $location >> $name
clear
banner
echo "Ex., bash,python or python2."
echo
echo
printf "\e[33m\e[1mScript Language :\e[92m\e[1m "
read scriptname
clear
cd $HOME
echo "base64 -d $name | $scriptname" >> bull$ex
bash-obfuscate bull$ex >> run_$scriptname.sh
rm -rvf bull$ex
clear
toilet -t -f pagga  "    Done ^^    " -F border | lolcat
echo -e "         Created by Parixit Sutariya"
fi
if [ "$option" -eq 2 ];then
clear
banner
sleep 1
echo "Ex., Bullenc.sh"
echo
echo
printf "\e[33m\e[1mEncrypted Script Name :\e[92m\e[1m "
read enclocation
clear
banner
echo "Ex., bash,python or python2."
echo
echo
printf "\e[33m\e[1mScript Language :\e[92m\e[1m "
read scriptname
clear
cd $HOME
echo "base64 -d $enclocation | $scriptname" >> bull$ex
bash-obfuscate bull$ex >> run_$scriptname.sh
rm -rvf bull$ex
clear
toilet -t -f pagga  "    Done ^^    " -F border | lolcat
echo -e "         Created by Parixit Sutariya"
fi
if [ "$option" -eq 3 ];then
clear
banner
echo
echo
echo -e "    \e[33m\e[1m[^^]\e[0m\e[1m Name  \t\e[91m\e[1m        :  \e[92m\e[1mBase64"
sleep 1
echo -e "    \e[33m\e[1m[^^]\e[0m\e[1m Lang.  \t\e[91m\e[1m:  \e[92m\e[1mBash"
sleep 1
echo -e "    \e[33m\e[1m[^^] \e[0m\e[1mAuthor  \t\e[91m\e[1m:  \e[92m\e[1mParixit Sutariya"
sleep 1
echo -e "    \e[33m\e[1m[^^] \e[0m\e[1mYT  \t\e[91m\e[1m        : \e[92m\e[1m yt.com/BullAnonymous"
sleep 1
echo -e "    \e[33m\e[1m[^^] \e[0m\e[1mGithub  \t\e[91m\e[1m:  \e[92m\e[1mgithub.com/Bhai4You"
sleep 1
echo -e "    \e[33m\e[1m[^^] \e[0m\e[1mDate  \t\e[91m\e[1m        :  \e[92m\e[1m28-4-20\e[0m"
sleep 1
echo
fi
}
req
banner
menu
