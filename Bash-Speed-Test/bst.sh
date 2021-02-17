#!/bin/bash

# XOWMIK IS STARTING FUCKING YOU
sleep 0.5
clear
sleep 0.5
command -v python2 > /dev/null 2>&1 || { printf "\n\t\e[0m\e[0m\e[36m[\e[1;37m+\e[36m] \e[34m   Installing PYTHON... \e[0m\n\n"; gem install python2 -y; clear; }
command -v speedtest > /dev/null 2>&1 || { printf "\n\t\e[0m\e[0m\e[36m[\e[1;37m+\e[36m] \e[34m   Installing REQUIREMENTS... \e[0m\n\n"; pip2 install speedtest-cli; clear; }
# FIRST STEP IS SUCKING, YOU KNOW IT BETTER :D
logo(){
clear
echo -e "\e[1;91m    ____ ___________"
echo -e "\e[1;36m   / __ ) ___/_  __/"
echo -e "\e[1;31m  / __  \__ \ / / \e[1;30mv1.0 "
echo -e "\e[1;36m / /_/ /__/ // /"
echo -e "\e[1;31m/_____/____//_/ \e[1;33mBash-Speed-Test"
printf "\e[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
printf "\e[1;32m║ \e[1;37mAUTHOR : SHAYER MAHMUD SOWMIK \e[1;32m║  \n"
printf "\e[1;32m║ \e[1;97mGIHUB  : GITHUB/IGN0R3DH4X0R  \e[1;32m║ \n"
printf "\e[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\e[0m"
echo ""
}
# SECOND STEP IS LICKING; BUT I WON'T LICK YOUR DIRTY PUSSY :)
index(){
sleep 0.2
printf " \e[1;96m>> \e[1;31mIndex Menu:"
printf "  \n\n\e[0m \e[1;32m[\e[1;37m01\e[1;32m] \e[1;93mSTART SPEED TEST"
printf "  \n\e[0m \e[1;32m[\e[1;37m02\e[1;32m] \e[1;93mABOUT THIS NOOB"
read -p $'  \n\n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m SELECT: \e[0m\e[1;96m\en' sel
if [[ $sel == 1 || $sel == 01 ]]; then
  test_speed
elif [[ $sel == 2 || $sel == 02  ]]; then
  xdg-open http://github.com/Ign0r3dH4x0r
else
  printf "\n  \e[31m[\e[1;33m~\e[31m] Invalid Options! Try again."
  sleep 2
  logo
  index
fi
}
# FUCKING YOUR HARDLY; YOUR ARE JUST SHOUTING :D
check_net(){
  {
  NET="$(ping -c 1 -q www.google.com >&/dev/null; echo $?)"
  } &> /dev/null
  if [[ "$NET" != 0 ]]
  then
     printf "\n\e[1;93m [x] \e[1;97m NO INTERNET CONNECTION; OR YOUR INTERNET SPEED TOO SLOW."
     exit 1
  fi
}
test_speed(){
check_net
logo
sleep 0.3
printf "  \n\e[1;31m[\e[0m\e[1;37m!\e[0m\e[1;31m]\e[0m\e[1;92m SPEESTEST SERVER STARTED SUCCESSFULLY..."
sleep 1
printf "  \n\e[1;31m[\e[0m\e[1;37m!\e[0m\e[1;31m]\e[0m\e[1;92m PLEASE WAIT ~30 SECONDS TILL THE TEST IS COMPLETED...\n\n"
testResult=$(speedtest --json)
download=$(echo $testResult | grep -Po '(?<="download":)[^},]*' | tr -d '[]"' | sed 's/\(<[^>]*>\|<\/>\|{1|}\)//g')
download_readable=$(numfmt --to=iec-i --suffix=B --padding=7 $download)
upload=$(echo $testResult | grep -Po '(?<="upload":)[^},]*' | tr -d '[]"' | sed 's/\(<[^>]*>\|<\/>\|{1|}\)//g')
upload_readable=$(numfmt --to=iec-i --suffix=B --padding=7 $upload)
ping=$(echo $testResult | grep -Po '(?<="ping":)[^},]*' | tr -d '[]"' | sed 's/\(<[^>]*>\|<\/>\|{1|}\)//g')
country_1=$(echo $testResult | grep -Po '(?<="country":)[^},]*' | tr -d '[]"' | sed 's/\(<[^>]*>\|<\/>\|{1|}\)//g')
city=$(echo $testResult | grep -Po '(?<="name":)[^},]*' | tr -d '[]"' | sed 's/\(<[^>]*>\|<\/>\|{1|}\)//g')
url=$(echo $testResult | grep -Po '(?<="url":)[^},]*' | tr -d '[]"' | sed 's/\(<[^>]*>\|<\/>\|{1|}\)//g')
latency=$(echo $testResult | grep -Po '(?<="latency":)[^},]*' | tr -d '[]"' | sed 's/\(<[^>]*>\|<\/>\|{1|}\)//g')
lat=$(echo $testResult | grep -Po '(?<="lat":)[^},]*' | tr -d '[]"' | sed 's/\(<[^>]*>\|<\/>\|{1|}\)//g')
time=$(echo $testResult | grep -Po '(?<="timestamp":)[^},]*' | tr -d '[]"' | sed 's/\(<[^>]*>\|<\/>\|{1|}\)//g')
lon=$(echo $testResult | grep -Po '(?<="lon":)[^},]*' | tr -d '[]"' | sed 's/\(<[^>]*>\|<\/>\|{1|}\)//g')
clientip=$(echo $testResult | grep -Po '(?<="ip":)[^},]*' | tr -d '[]"' | sed 's/\(<[^>]*>\|<\/>\|{1|}\)//g')
isp=$(echo $testResult | grep -Po '(?<="isp":)[^},]*' | tr -d '[]"' | sed 's/\(<[^>]*>\|<\/>\|{1|}\)//g')
rating=$(echo $testResult | grep -Po '(?<="isprating":)[^},]*' | tr -d '[]"' | sed 's/\(<[^>]*>\|<\/>\|{1|}\)//g')
server_lat=$(echo $lat | awk '{print $1}')
client_lat=$(echo $lat | awk '{print $2}')
server_lon=$(echo $lon | awk '{print $1}')
client_lon=$(echo $lon | awk '{print $2}')
country=$(echo $country_1 | awk '{print $1}')
# FINALLY, CUM ON YOUR ASS :)
logo
printf "\n \e[1;97m>>> \e[1;34mTEST RESULT => \n"
printf "\n \e[0m \e[1;91m>>\e[1;93m DOWNLOAD   :  $download_readable/s"
printf "\n \e[0m \e[1;91m>>\e[1;93m UPLOAD     :  $upload_readable/s"
printf "\n \e[0m \e[1;91m>>\e[1;93m PING       :  $ping"
printf "\n\n \e[1;97m>>> \e[1;34mSERVER INFO => \n"
printf "\n \e[0m \e[1;91m>>\e[1;93m HOST       :  $url"
printf "\n \e[0m \e[1;91m>>\e[1;93m LATITUDE   :   $server_lat"
printf "\n \e[0m \e[1;91m>>\e[1;93m LONGITUDE  :   $server_lon"
printf "\n\n \e[1;97m>>> \e[1;34mYOUR INFO => \n"
printf "\n \e[0m \e[1;91m>>\e[1;93m IP         :  $clientip"
printf "\n \e[0m \e[1;91m>>\e[1;93m OPERATOR   :  $isp"
printf "\n \e[0m \e[1;91m>>\e[1;93m COUNTRY    :   $country"
printf "\n \e[0m \e[1;91m>>\e[1;93m ISP RATING :  $rating"
printf "\n\n \e[1;97m>>> \e[1;34mTIMESTAMP => $time \n"
sleep 2
xdg-open https://github.com/IGN0R3DH4X0R
}
logo
index

# OKEY FUCKING YOUR
