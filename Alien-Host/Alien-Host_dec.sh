cd
cd $HOME
cd Alien-Host
cd src
cd logo
bash alien.sh
echo
echo -e "\e[0m\e[1m...:;'':,.. [ Alien-Option ] ..,.:'';:..."
echo
echo -e "\e[1m\e[32m         1) \e[33m  Localhost:8080"
echo -e "\e[1m\e[32m         2) \e[33m \e[33m Admin Panel"
echo -e "\e[1m\e[32m         3)   \e[33mLogin"
echo -e "\e[1m\e[32m         4) \e[33m  Date & Time"
echo -e "\e[1m\e[32m         5)  \e[33m Visit Counter (1)"
echo -e "\e[1m\e[32m         6)  \e[33m Visit Counter (2)"
echo -e "\e[1m\e[32m         7) \e[33m  Online Counter"
echo -e  "\e[1m\e[32m         8) \e[33m  Web Link"
echo -e  "  \e[1m\e[32m       9)  \e[33m Localhost:9091"
echo -e "\e[1m\e[32m         10)  \e[33mTodos"
echo -e "\e[1m\e[32m         11)  \e[33mDesi chat"
echo -e "  \e[1m\e[32m       12)  \e[33mCookies-Stealer"
echo -e "  \e[1m\e[32m       13)  \e[33mAbout"
echo
echo -e "         \e[0m\e[1m-+++---+++---+++-"
echo
echo
printf " \e[36m\e[1mAlien Host \e[31m: \e[0m\e[1m"
read varname
if [ "$varname" = "1" ]
then
clear
figlet -f big  "Localhost" | lolcat
cd
cd go/src/github.com/kataras/iris/_examples/hello-world
go run main.go
fi
if [ "$varname" = "2" ]
then
clear
figlet -f big  "Admin Panel" | lolcat
cd
cd go/src/github.com/kataras/iris/_examples/authentication/basicauth/
go run main.go
echo "Goood bye. ..!!!"
fi
if [ "$varname" = "3" ]
then
clear
figlet -f big  "  Login" | lolcat
cd
cd go/src/github.com/kataras/iris/_examples/mvc/login/
go run main.go
echo "Goood bye. ..!!!"
fi
if [ "$varname" = "4" ]
then
clear
figlet -f big  "Date & Time" | lolcat
cd
cd go/src/github.com/kataras/iris/_examples/mvc/middleware
go run main.go
echo "Goood bye. ..!!!"
fi
if [ "$varname" = "5" ]
then
clear
figlet -f big  "Visit one" | lolcat
cd
cd go/src/github.com/kataras/iris/_examples/mvc/session-controller
go run main.go
echo "Goood bye. ..!!!"
fi
if [ "$varname" = "6" ]
then
clear
figlet -f big  "Visit two" | lolcat
cd
cd go/src/github.com/kataras/iris/_examples/mvc/singleton
go run main.go
echo "Goood bye. ..!!!"
fi
if [ "$varname" = "7" ]
then
clear
figlet -f big  "Online Counter" | lolcat
cd
cd go/src/github.com/kataras/iris/_examples/mvc/websocket
go run main.go
echo "Goood bye. ..!!!"
fi
if [ "$varname" = "8" ]
then
clear
figlet -f big  "Web Link" | lolcat
cd
cd go/src/github.com/kataras/iris/_examples/miscellaneous/pprof
go run main.go
echo "Goood bye. ..!!!"
fi
if [ "$varname" = "9" ]
then
clear
figlet -f big  "Localhost:9091" | lolcat
cd
cd go/src/github.com/kataras/iris/_examples/tutorial/caddy/server1
go run main.go
echo "Goood bye. ..!!!"
fi
if [ "$varname" = "10" ]
then
clear
figlet -f big  "  Todos" | lolcat
cd
cd go/src/github.com/kataras/iris/_examples/tutorial/vuejs-todo-mvc/src/web
go run main.go
echo "Goood bye. ..!!!"
fi
if [ "$varname" = "11" ]
then
clear
figlet -f big  "Desi Chat" | lolcat
cd
cd go/src/github.com/kataras/iris/_examples/websocket/chat
go run main.go
echo "Goood bye. ..!!!"
fi
if [ "$varname" = "12" ]
then
clear
figlet -f big  "Cookies.   Stealer" | lolcat
cd
cd go/src/github.com/kataras/iris/_examples/http_request/request-logger
go run main.go
echo "Goood bye. ..!!!"
fi
if [ "$varname" = "13" ]
then
clear
figlet -f big  " Alien  -  Host " | lolcat
echo -e "\e[1m\e[32m         Name        \e[31m:  \e[33mAlien-Host"
echo -e "\e[1m\e[32m         Platform \e[33m \e[33m  \e[31m:  \e[33mTermux"
echo -e "\e[1m\e[32m         Code   \e[33m     \e[31m:  \e[33mBash/Shell"
echo -e "\e[1m\e[32m         Sec.Code \e[33m   \e[31m:  \e[33m8h4i"
echo -e "\e[1m\e[32m         Author \e[33m     \e[31m:  \e[33mSutariya Parixit"
echo -e "\e[1m\e[32m         Github  \e[33m    \e[31m:  \e[33mhttps://github.com/Bhai4You"
echo -e "\e[1m\e[32m         Youtube  \e[33m   \e[31m: \e[33m https://youtube.com/BullAnonymous"
echo -e "\e[1m\e[32m         Site \e[33m       \e[31m:  \e[33mhttps://bhai4you.blogspot.com"
fi
