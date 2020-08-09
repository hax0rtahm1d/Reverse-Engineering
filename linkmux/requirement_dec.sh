clear
apt update -y
apt upgrade -y
pkg install pv -y
pkg install curl -y
clear

cd $HOME/linkmux
mkdir ext
cd ext
curl https://raw.githubusercontent.com/Bhai4You/bhai4you/master/lmux/logo.sh >> logo.sh
curl https://raw.githubusercontent.com/Bhai4You/bhai4you/master/lmux/logo1.sh >> logo1.sh
curl https://raw.githubusercontent.com/Bhai4You/bhai4you/master/lmux/Bhai4You.sh >> Bhai4You.sh
curl https://raw.githubusercontent.com/Bhai4You/bhai4you/master/lmux/E-Books.sh >> E-Books.sh
curl https://raw.githubusercontent.com/Bhai4You/bhai4you/master/lmux/Html.sh >> Html.sh
curl https://raw.githubusercontent.com/Bhai4You/bhai4you/master/lmux/Python.sh >> Python.sh
curl https://raw.githubusercontent.com/Bhai4You/bhai4you/master/lmux/TS.sh >> TS.sh
curl https://raw.githubusercontent.com/Bhai4You/bhai4you/master/lmux/eh.sh >> es.sh
curl https://raw.githubusercontent.com/Bhai4You/bhai4you/master/lmux/lan.sh >> lan.sh
curl https://raw.githubusercontent.com/Bhai4You/bhai4you/master/lmux/pdf.sh >> pdf.sh
clear
cd $HOME/linkmux
