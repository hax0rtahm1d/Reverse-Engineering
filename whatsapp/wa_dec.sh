# Deobfuscated BY HTR-TECH | Tahmid Rayat

# Github    : https://github.com/htr-tech 
# Instagram : https://www.instagram.com/tahmid.rayat
# Facebook  : https://fb.com/tahmid.rayat.oficial 
# Messenger : https://m.me/tahmid.rayat.oficial 

clear
BANNER() {
printf "
\033[31;1m__      __\033[0;37m_
\033[31;1m\ \    / \033[0;37m/_\   \033[36;5m# Link Chat Wa Generator
\033[31;1m \ \/\/ \033[0;37m/ _ \  \033[32;5m# Support Direct Send
\033[31;1m  \_/\_\033[0;37m/_/ \_\ \033[35;5m# NO PHISING!
\033[30;1m╔═════════════════════════════════════════╗
║[31;1m➢ Author : Febry [ xNot_Found ]          [30;1m║
║[32;1m➣ Contact: +62823-8637-2115              [30;1m║
║[33;1m➢ Email  : febryafriansyah@programmer.net[30;1m║
║[34;1m➣ Website: http://hatakecnk.noads.biz    [30;1m║
║[37;1m➢ Github : https://github.com/hatakecnk  [30;1m║
╚═════════════════════════════════════════╝\n\n"
}
BANNER
DATA() {
URL="https://api.whatsapp.com/send?phone=$no&text=${tex}" 
printf "\033[37;0m┌─[ \033[31;1mDirect Send \033[32;1my/n \033[37;0m]\n└─[\033[31;1m$\033[37;0m]> \033[36;1m"
read send
if [[ $send == y ]];then
termux-open $URL
fi
if [[ $send == n ]]; then
echo -e "\033[34;1mSaved as send.txt"
echo "$URL" >> send.txt
echo -e "\nLink ==>\033[32;1m $URL"
exit
fi
}
printf "\033[37;0m┌─[ \033[31;1mInput Number Phone \033[37;0m]\n└─[\033[31;1m$\033[37;0m]>\033[36;1m +"
read no
printf "\033[37;0m┌─[ \033[31;1mInput Message \033[37;0m]\n└─[\033[31;1m$\033[37;0m]> \033[36;1m"
read tex
DATA $no $tex