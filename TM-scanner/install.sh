
#----colors----
red='\033[1;91m'
green='\033[1;92m'
cyan='\033[1;96m'
yellow='\033[1;93m'


echo ""
echo ""
echo "$yellow installation starting....."
sleep 2
clear
sleep 0.2
echo ""
echo ""
echo "$green coded by @TechnicalMujeeb"
echo ""
sleep 1


if [ -f /data/data/com.termux/files/usr/bin/python ];
then 
    sleep 1
    echo "$green[✔]:[ python ]: $cyan Found !" 
else
    echo "$green[x]:[ python ]: $red Not Found ! "
    echo ""
    sleep 1 
    echo "$yellow installing python....."
    sleep 1
    apt install python
fi

echo ""

if [ -f /data/data/com.termux/files/usr/bin/python2 ];
then
    sleep 1
    echo "$green[✔]:[ python2 ]: $cyan Found !"
else 
    echo "$green[x]:[ python2 ]: $red Not Found ! "
    echo "" 
    sleep 1 
    echo "$yellow installing python2....." 
    sleep 1 
    apt install python2
fi

echo ""

if [ -f /data/data/com.termux/files/usr/bin/nmap ];
then
    sleep 1
    echo "$green[✔]:[ Nmap ]: $cyan Found !"
else 
    echo "$green[x]:[ Nmap ]: $red Not Found ! " 
    echo "" 
    sleep 1 
    echo "$yellow installing Nmap....." 
    sleep 1 
    apt install nmap
fi

echo ""
sleep 1
echo "$green installing requirements...."
sleep 0.9
pip install requests
pip2 install requests
pip install colorama
pip2 install colorama

echo ""
sleep 1
echo "installation Finished"
echo ""
sleep 1
echo "$cyan python2 tmscanner.py"
echo ""
echo "-----------------------------------------"
sleep 0.5
echo ""
ls
echo ""
