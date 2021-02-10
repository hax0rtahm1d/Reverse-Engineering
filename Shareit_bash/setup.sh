#/bin/bash

# Just Checking The Codes .. Happy Coding 


detect_distro() {
os=$(echo $OSTYPE)
    if [[ "$os" == "linux-android" ]]; then
      home_dir="$PREFIX/bin/shareit"
    else
      home_dir="$PREFIX/../usr/local/bin/shareit"
    fi
}
detect_distro
sleep 0.5
clear
sleep 0.5
# FIRST STEP IS SUCKING, YOU KNOW IT BETTER :D
logo(){
clear
echo -e "\e[1;33m         __                    \e[1;36m  ______  "
echo -e "\e[1;33m   _____/ /_  ____  _________ \e[1;36m  /  _/ /_ "
echo -e "\e[1;33m  / ___/ __ \/ __ \/ ___/ _ | \e[1;36m / // __/ "
echo -e "\e[1;33m (__  ) / / / /_/ / /  /  __/\e[1;36m / // /_   "
echo -e "\e[1;33m/____/_/ /_/\__,_/_/\e[1;30m1.2\e[1;33m\___/ \e[1;36m/__/\__/   "
printf "\e[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
printf "\e[1;32m║ \e[1;37m  SHARE FILES FROM TERMINAL   \e[1;32m║  \n"
printf "\e[1;32m║ \e[1;37mAUTHOR : SHAYER MAHMUD SOWMIK \e[1;32m║  \n"
printf "\e[1;32m║ \e[1;97mGIHUB  : GITHUB/IGN0R3DH4X0R  \e[1;32m║ \n"
printf "\e[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\e[0m"
echo ""
main_setup
}
main_setup(){
sleep 1
printf "  \n\e[1;31m[\e[0m\e[1;37m!\e[0m\e[1;31m]\e[0m\e[1;92m SETTING UP \e[1;34m \n\n "
apt install curl -y
rm -f $home_dir
cp .ign0r3dh4x0r $home_dir
chmod +x $home_dir
printf "  \n\e[1;31m[\e[0m\e[1;37m!\e[0m\e[1;31m]\e[0m\e[1;92m INSTALLATION COMPLETE! RUN THIS TOOL BY TYPING 'shareit' IN YOUR TERMINAL.\n\n"
sleep 3
xdg-open https://linktr.ee/Xowmik
}
logo
