apt update -y
apt upgrade -y
apt install curl -y
apt install php -y
apt install figlet -y
clear
echo
echo
echo
clear
cd /sdcard
mkdir php
cd php
mkdir image
mkdir css
cd image
curl https://raw.githubusercontent.com/Bhai4You/bhai4you/master/bull.png >> bull.png
clear
cd ..
cd css
curl https://raw.githubusercontent.com/Bhai4You/bhai4you/master/style.css >> style.css
clear
cd ..
curl https://raw.githubusercontent.com/Bhai4You/bhai4you/master/smsbomb.php >> smsbomb.php
clear
echo
echo
echo
printf "\e[32m\e[1mWhat is Your Name :\e[36m\e[1m "
read varname
echo "</div>" >> /sdcard/php/smsbomb.php
echo "<div class='footer'>"a >> /sdcard/php/smsbomb.php
echo "            <h2 style='color:lightblue'>Created by : <font color='white'>$varname</h2>" >> /sdcard/php/smsbomb.php
echo "        </div>" >> /sdcard/php/smsbomb.php
echo "    </body>" >> /sdcard/php/smsbomb.php
echo "</html>" >> /sdcard/php/smsbomb.php
clear
echo -e "\e[1m     Now You Can Run \e[33m bash start.sh\e[0m\e[1m....!!!!"
echo
echo
