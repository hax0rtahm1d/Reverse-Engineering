#! /bin/bash
#
#
#
#
# CODED BY - SHAYER MAHMUD SOWMIK
# GITHUB/Ign0r3dH4x0r
# FB/Ign0r3dH4x0r
# IF YOU USE ANY PART OF THIS SCRIPT IN YOUR PROJECT, PLEASE GIVE ME CREDIT.
# IT WILL INSPIRE ME TO DO SOMETHING NEW FOR YOU GUYS :D
# HAPPY CODING :V
# If you wanna take credit of this script, please look back to yourself again :)
#
#
#
#
sleep 1
clear
sleep 2
logo(){
clear
printf "\n\e[1;31m ██████╗░██╗░░░░░░█████╗░░█████╗░██████╗░██╗░░░██╗    \n"
printf " ██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝    \n"
printf " ██████╦╝██║░░░░░██║░░██║██║░░██║██║░░██║░╚████╔╝░    \n"
printf " ██╔══██╗██║░░░░░██║░░██║██║░░██║██║░░██║░░╚██╔╝░░    \n"
printf " ██████╦╝███████╗╚█████╔╝╚█████╔╝██████╔╝░░░██║░░░    \n"
printf " ╚═════╝░╚══════╝░╚════╝░░╚════╝░╚═════╝░░░░╚═╝░░░ IP  \e[0m  \n"
printf "\e[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
printf "\e[1;97m AUTHOR    : SHAYER MAHMUD SOWMIK  \n"
printf " FACEBOOK  : FB/IGN0R3DH4X0R \n"
printf " GIHUB     : GITHUB/IGN0R3DH4X0R \n"
printf "\e[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
}
command -v nmap > /dev/null 2>&1 || { printf "\n\t\e[0m\e[0m\e[36m[\e[1;37m+\e[36m] \e[34m   Installing NMAP... \e[0m\n\n"; apt install nmap -y; logo; }
command -v lynx > /dev/null 2>&1 || { printf "\n\t\e[0m\e[0m\e[36m[\e[1;37m+\e[36m] \e[34m   Installing LYNX... \e[0m\n\n"; apt install lynx -y; logo; }
command -v curl > /dev/null 2>&1 || { printf "\n\t\e[0m\e[0m\e[36m[\e[1;37m+\e[36m] \e[34m   Installing CURL... \e[0m\n\n"; apt install curl -y; logo; }
index(){
sleep 1
printf "\n  \e[1;32m>>> \e[1;33mINDEX:\n"
sleep 0.5
printf "\n"
printf "\e[1;31m  [\e[1;37m01\e[1;31m] \e[1;36mINFO GRABBER    \n"
printf "\e[1;31m  [\e[1;37m02\e[1;31m] \e[1;36mWHOIS LOOKUP    \n"
printf "\e[1;31m  [\e[1;37m03\e[1;31m] \e[1;36mDNS LOOKUP    \n"
printf "\e[1;31m  [\e[1;37m04\e[1;31m] \e[1;36mREVERSE IP LOOKUP    \n"
printf "\e[1;31m  [\e[1;37m05\e[1;31m] \e[1;36mGEOIP LOOKUP    \n"
printf "\e[1;31m  [\e[1;37m06\e[1;31m] \e[1;36mNMAP SCANNER    \n"
printf "\e[1;31m  [\e[1;37m07\e[1;31m] \e[1;36mPAGE LINKS GRABBER    \n"
printf "\e[1;31m  [\e[1;37m08\e[1;31m] \e[1;36mTRACEROUTE SCANNER    \n"
printf "\e[1;31m  [\e[1;37m09\e[1;31m] \e[1;36mMORE EPIC TOOLS    \n"
printf "\e[1;31m  [\e[1;37m10\e[1;31m] \e[1;36mUPDATE THIS TOOL    \n"
echo
read -p $'  \n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m Select an option: \e[0m\e[1;96m\en' sel
if [[ $sel == 1 || $sel == 01 ]]; then
  info_grabber
elif [[ $sel == 2 || $sel == 02  ]]; then
  whois_loookup
elif [[ $sel == 3 || $sel == 03  ]]; then
  DNS_lookup
elif [[ $sel == 4 || $sel == 04  ]]; then
  rDNS_lookup
elif [[ $sel == 5 || $sel == 05  ]]; then
  GEOIP_lookup
elif [[ $sel == 6 || $sel == 06  ]]; then
  Nmap_scan
elif [[ $sel == 7 || $sel == 07  ]]; then
  Link_grabber
elif [[ $sel == 8 || $sel == 08  ]]; then
  traceroute_scanner
elif [[ $sel == 9 || $sel == 09  ]]; then
  xdg-open http://github.com/Ign0r3dH4x0r
elif [[ $sel == 9 || $sel == 09  ]]; then
  git pull origin
else
  printf "\n  \e[31m[\e[1;33m~\e[31m] Invalid Options! Try again."
fi
}

# √

whois_loookup(){
sleep 1
logo
read -p $'  \n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m ENTER DOMAIN NAME [ LIKE: GOOGLE.COM ] : \e[0m\e[1;96m\en' domain
sleep 2
printf "\n\e[1;31m [\e[1;37m√\e[1;31m]\e[1;36m PERFORMING WHOIS LOOKUP    \n"
printf "\e[1;35m\n\n\n"
whois $domain
printf "\e[0m"
read -n 1 -s -r -p $'  \n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m PRESS ANY KEY FOR MAIN MENU..'
sleep 0.5
logo
index
}



DNS_lookup(){
  sleep 1
  logo
  read -p $'  \n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m ENTER DOMAIN NAME [ LIKE: GOOGLE.COM ] : \e[0m\e[1;96m\en' domain
  sleep 2
  printf "\n\e[1;31m [\e[1;37m√\e[1;31m]\e[1;36m RUNNING DNS SCANNER    \n"
  printf "\e[1;35m\n\n\n"
  curl https://api.hackertarget.com/dnslookup/?q=$domain
  printf "\e[0m"
  read -n 1 -s -r -p $'  \n\n\n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m PRESS ANY KEY FOR MAIN MENU..'
  sleep 0.5
  logo
  index

}

rDNS_lookup(){
  sleep 1
  logo
  read -p $'  \n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m ENTER DOMAIN NAME [ LIKE: GOOGLE.COM ] : \e[0m\e[1;96m\en' domain
  sleep 2
  printf "\n\e[1;31m [\e[1;37m√\e[1;31m]\e[1;36m RUNNING REVERSE DNS SCANNER    \n"
  printf "\e[1;35m\n\n\n"
  curl https://api.hackertarget.com/reversedns/?q=$domain
  printf "\e[0m"
  read -n 1 -s -r -p $'  \n\n\n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m PRESS ANY KEY FOR MAIN MENU..'
  sleep 0.5
  logo
  index
}



GEOIP_lookup(){
  sleep 1
  logo
  read -p $'  \n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m ENTER DOMAIN NAME [ LIKE: GOOGLE.COM ] : \e[0m\e[1;96m\en' domain
  sleep 2
  printf "\n\e[1;31m [\e[1;37m√\e[1;31m]\e[1;36m RUNNING GEOIP SCANNER    \n"
  printf "\e[1;35m\n\n\n"
  curl https://api.hackertarget.com/geoip/?q=$domain
  printf "\e[0m"
  read -n 1 -s -r -p $'  \n\n\n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m PRESS ANY KEY FOR MAIN MENU..'
  sleep 0.5
  logo
  index
}



Nmap_scan(){
sleep 1
logo
read -p $'  \n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m ENTER DOMAIN NAME [ LIKE: GOOGLE.COM ] : \e[0m\e[1;96m\en' domain
sleep 2
printf "\n\e[1;31m [\e[1;37m√\e[1;31m]\e[1;36m PERFORMING NMAP SCAN    \n"
printf "\e[1;35m\n\n\n"
nmap $domain
printf "\e[0m"
read -n 1 -s -r -p $'  \n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m PRESS ANY KEY FOR MAIN MENU..'
sleep 0.5
logo
index
}



Link_grabber(){
  sleep 1
  logo
  read -p $'  \n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m ENTER DOMAIN NAME [ LIKE: GOOGLE.COM ] : \e[0m\e[1;96m\en' domain
  sleep 2
  printf "\n\e[1;31m [\e[1;37m√\e[1;31m]\e[1;36m RUNNING LINK GRABBER    \n"
  printf "\e[1;35m\n\n\n"
  lynx -listonly -dump $domain
  printf "\e[0m"
  read -n 1 -s -r -p $'  \n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m PRESS ANY KEY FOR MAIN MENU..'
  sleep 0.5
  logo
  index
}



traceroute_scanner(){
  sleep 1
  logo
  read -p $'  \n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m ENTER DOMAIN NAME [ LIKE: GOOGLE.COM ] : \e[0m\e[1;96m\en' domain
  sleep 2
  printf "\n\e[1;31m [\e[1;37m√\e[1;31m]\e[1;36m RUNNING TRACEROUTE SCANNER    \n"
  printf "\e[1;35m\n\n\n"
  nmap -sn -Pn --traceroute $domain
  printf "\e[0m"
  read -n 1 -s -r -p $'  \n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m PRESS ANY KEY FOR MAIN MENU..'
  sleep 0.5
  logo
  index
}


info_grabber(){
logo
read -p $'  \n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m ENTER DOMAIN NAME [ LIKE: GOOGLE.COM ] : \e[0m\e[1;96m\en' domain
printf "\n\n\e[1;31m [\e[1;37m√\e[1;31m]\e[1;36m PERFORMING WHOIS LOOKUP    \n"
printf "\e[1;35m\n\n\n"
whois $domain
printf "\e[0m"
printf "\n\n\e[1;31m [\e[1;37m√\e[1;31m]\e[1;36m RUNNING DNS SCANNER    \n"
printf "\e[1;35m\n\n\n"
curl https://api.hackertarget.com/dnslookup/?q=$domain
printf "\e[0m"
printf "\n\n\e[1;31m [\e[1;37m√\e[1;31m]\e[1;36m RUNNING REVERSE DNS SCANNER    \n"
printf "\e[1;35m\n\n\n"
curl https://api.hackertarget.com/reversedns/?q=$domain
printf "\e[0m"
printf "\n\n\e[1;31m [\e[1;37m√\e[1;31m]\e[1;36m RUNNING GEOIP SCANNER    \n"
printf "\e[1;35m\n\n\n"
curl https://api.hackertarget.com/geoip/?q=$domain
printf "\e[0m"
printf "\n\n\e[1;31m [\e[1;37m√\e[1;31m]\e[1;36m PERFORMING NMAP SCAN    \n"
printf "\e[1;35m\n\n\n"
nmap $domain
printf "\e[0m"
printf "\n\n\e[1;31m [\e[1;37m√\e[1;31m]\e[1;36m RUNNING LINK GRABBER    \n"
printf "\e[1;35m\n\n\n"
lynx -listonly -dump $domain
printf "\e[0m"
printf "\n\n\e[1;31m [\e[1;37m√\e[1;31m]\e[1;36m RUNNING TRACEROUTE SCANNER    \n"
printf "\e[1;35m\n\n\n"
nmap -sn -Pn --traceroute $domain
printf "\e[0m"
sleep 0.5
printf "\n\n\e[1;31m [\e[1;37m√\e[1;31m]\e[1;36m GRABBING DONE!    \n"
read -n 1 -s -r -p $'  \n\n\n\e[1;31m[\e[0m\e[1;37m+\e[0m\e[1;31m]\e[0m\e[1;92m PRESS ANY KEY FOR MAIN MENU..'
sleep 0.5
logo
index
}
logo
index
