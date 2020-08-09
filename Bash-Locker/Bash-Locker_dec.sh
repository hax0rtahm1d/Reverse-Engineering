clear
figlet  "   Mr . Locker "
echo
echo -e "\e[33m\e[1m      -------------\e[33m(\e[32m Bash Locker \e[33m)------------"
echo
echo
echo -e "\e[36m\e[1m Name    \e[33m  : \e[32m Mr . Locker"
echo -e "\e[36m\e[1m Code      \e[33m: \e[32m Bash / Shell"
echo -e "\e[36m\e[1m Sec.Code \e[33m : \e[32m 8h4i"
echo -e "\e[36m\e[1m Platform  \e[33m: \e[32m Termux"
echo -e "\e[36m\e[1m Coder     \e[33m: \e[32m Sutariya Parixit"
echo -e "\e[36m\e[1m Idea      \e[33m: \e[32m github.com/remo7777"
echo -e "\e[36m\e[1m Github   \e[33m : \e[32m github.com/Bhai4You"
echo -e "\e[36m\e[1m Youtube   \e[33m: \e[32m youtube.com/BullAnonymous"
echo -e "\e[36m\e[1m Site      \e[33m: \e[32m https://bhai4you.blogspot.com\e[0m\e[1m"
echo
echo
echo
echo -e "Enter To Continue..."
read
clear
echo -e "\e[32m\e[1m e.x. \e[36m parixit.sh"
echo
printf "\e[33m\e[1mWhat Is Your File Name : \e[32m "
read varname
echo
echo
clear
echo -e "\e[32m\e[1m e.x. \e[36m /sdcard/parixit.sh"
echo
printf "\e[33m\e[1mWhat Is Your File Location : \e[32m "
read varloc
echo
echo
clear
bash-obfuscate $varloc -o /sdcard/$varname
echo
echo
echo " " >> /sdcard/$varname
curl https://raw.githubusercontent.com/Bhai4You/bhai4you/master/copyright.sh >> /sdcard/$varname
clear
echo -e " \e[33m \e[1mYour Bash File \e[31m$varname \e[33mis Successful Locked By Bash-Locker Tools "
echo
echo
echo -e " \e[0m\e[1mLocation : /sdcard/$varname"
