clear
toilet -f standard  '          127 . 0 . 0 . 1 '  -F gay
echo -e "\e[1m\e[31m<\e[33m------------❌\e[32m-( There's No Place Like 127.0.0.1 )-\e[33m❌-----------------\e[31m>\e[0m"
echo
echo -e "\e[1m\e[31m<\e[33m----------------------❌\e[32m-( \e[36mBhai 4 You\e[32m )-\e[33m❌----------------------------\e[31m>\e[0m"
echo
echo
sleep 3
echo " "
echo " "
echo " "
clear
echo
echo
figlet -f pagga "       Image Setup          " | lolcat
echo
cd
cd /sdcard
mkdir php
cd
echo -e " \e[1m\e[36m\t  First of Enter Your image in /sdcard/php folder..!!!"
echo
echo -e "\e[1m\e[33m\nWhat is Your Image Name (\e[36meg. Hack.jpg\e[33m)\e[32m :\n\n "
read varimg
clear
echo
echo
figlet -f pagga "    Enter Your Name      " | lolcat
echo -e "\e[1m\e[36m\t          Enter Your Coded Name..!! ( e.g, 8h4i )\n"
echo -e "\e[1m\e[33m\n Hacked by ( \e[36mYour Name \e[33m)\e[32m :\n\n "
read varhack
echo
clear
echo
echo
figlet -f pagga "    Width and Height    " | lolcat
echo
echo -e "\e[1m\e[36m\tAnytime You can change your image width and height..!!!"
echo
echo -e "\e[1m\e[33m Enter Your Image Width\e[32m :\n\n "
read varwidth
echo
echo
echo
echo -e "\e[1m\e[33m\n Enter Your Image Height\e[32m :\n\n "
read varheight
cd
echo >> /sdcard/php/index.html
echo "
<html>
<head>
<title>   you are hacked </title>
</head>
<body bgcolor='black'>
<center> " >> /sdcard/php/index.html
echo "<img src='$varimg' width=''$varwidth' height='$varheight' />" >> /sdcard/php/index.html
echo
echo "
</center>
<font color=red size='10px' face='tahoma'>
<h1> <p align='center'> <b>you are hacked <br> </h1>
<font color=white size='10px' face='tahoma'> " >> /sdcard/php/index.html
echo
echo
echo "<h3> <p align="center"> by <b> $varhack  </h3>
</body>
</html> " >> /sdcard/php/index.html
clear
echo
cd
cd T-Host
cd setup
bash setup.sh
