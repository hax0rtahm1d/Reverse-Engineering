clear
cd $HOME/linkmux/ext
bash logo.sh
echo
echo
echo -e "\e[31m\e[1m1. \e[0m\e[1m Google"
echo -e "\e[31m\e[1m2.\e[0m\e[1m  Bhai 4 You"
echo -e "\e[31m\e[1m3.\e[0m\e[1m  Termux-Tools"
echo -e "\e[31m\e[1m4.\e[0m\e[1m  Programming Language"
echo -e "\e[31m\e[1m5.\e[0m\e[1m  Hack to School"
echo -e "\e[31m\e[1m6.\e[0m\e[1m  Ethical Hacking"
echo -e "\e[31m\e[1m7.\e[0m\e[1m  E-Books"
echo -e "\e[31m\e[1m8.\e[0m\e[1m  EH Tutorials"
echo -e "\e[31m\e[1m9.\e[0m\e[1m  Technical Sagar\e[0m\e[1m"
echo -e "\e[31m\e[1m10.\e[0m\e[1m PDF\e[0m\e[1m"
echo -e "\e[31m\e[1m11.\e[0m\e[1m About Us\e[0m\e[1m"
echo
echo
echo
printf "\e[1m\e[32mE\e[0m\e[1mnter \e[32mN\e[0m\e[1mumber : \e[36m\e[1m"
read varno
if [ $varno == '1' ]
then
clear
termux-open-url https://google.com
clear
elif [ $varno == '2' ]
then
clear
cd $HOME/linkmux/ext
bash Bhai4You.sh
elif [ $varno == '3' ]
then
clear
termux-open-url https://github.com/Bhai4You/Termux-Tools/raw/master/Termux%20Tools.apk
clear
elif [ $varno == '4' ]
then
clear
cd $HOME/linkmux/ext
bash lan.sh
clear
elif [ $varno == '5' ]
then
clear
termux-open-url https://www.mediafire.com/download/b5t8vcd6lwfdk3z
clear
elif [ $varno == '6' ]
then
clear
termux-open-url https://www.mediafire.com/download/t9vd4a08gbev466
clear
elif [ $varno == '7' ]
then
clear
cd $HOME/linkmux/ext
bash E-Books.sh
clear
elif [ $varno == '8' ]
then
clear
cd $HOME/linkmux/ext
bash eh.sh
clear
elif [ $varno == '9' ]
then
clear
cd $HOME/linkmux/ext
bash TS.sh
clear
elif [ $varno == '11' ]
then
clear
echo
echo
bash $HOME/linkmux/ext/logo1.sh
echo
echo -e "\e[1m\e[31mN\e[0mame     : \e[32m\e[1mL\e[0m\e[1minkmux"
echo -e "\e[1m\e[31mA\e[0muthor   : \e[32m\e[1mS\e[0m\e[1mutariya \e[32m\e[1mP\e[0m\e[1marixit"  | pv -qL 23;
echo -e "\e[1m\e[31mP\e[0mlatform : \e[32m\e[1mT\e[0m\e[1mermux"
echo -e "\e[1m\e[31mS\e[0mec.code : \e[32m\e[1m8\e[0m\e[1mh4i"  | pv -qL 23;
echo -e "\e[1m\e[31mS\e[0mite     : \e[32m\e[1mh\e[0m\e[1mttps://bhai4you.blogspot.com"
echo -e "\e[1m\e[31mG\e[0mithub   : \e[32m\e[1mh\e[0m\e[1mttps://github.com/Bhai4You"  | pv -qL 23;
echo -e "\e[1m\e[31mY\e[0moutube  : \e[32m\e[1mh\e[0m\e[1mttps://youtube.com/BullAnonymous"
echo
echo
elif [ $varno == '10' ]
then
clear
cd $HOME/linkmux/ext
bash pdf.sh
clear
else
exit
fi
