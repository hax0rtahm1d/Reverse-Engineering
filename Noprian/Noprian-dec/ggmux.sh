echo
clear
blue='\e[1;34m'
green='\e[0;23m'
purple='\e[1;35m'
cyan='\e[1;36m'
red='\e[1;31m'
yellow='\e[1;33m'
lgreen='\e[1;34m'
brown='\e[0;33m'
white='\e[1;37m'
echo
echo -e $red".::!!!!!!!:."
echo -e $red"  .!!!!!:.                        .:!!!!!!!!!!!!"
echo -e $red"  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW\$\$\$"
echo -e $red"      :\$\$NWX!!:           .:!!!!!!XUWW\$\$\$\$\$\$\$\$\$P"
echo -e $red"      \$\$\$\$\$##WX!:      .<!!!!UW\$\$\$\$*  \$\$\$\$\$\$\$\$#"
echo -e $red"      \$\$\$\$\$  \$\$\$UX   :!!UW\$\$\$\$\$\$\$\$\$   4\$\$\$\$\$**"
echo -e $red"      ^\$\$\$B  \$\$\$\$\\     \$\$\$\$\$\$\$\$\$\$\$\$   d\$\$R*"
echo -e $red"        **\$bd\$\$\$\$      **\$\$\$\$\$\$\$\$\$\$\$o+#      ${yellow}*${white}GGmuX"
echo -e $red"             ****          *******"
echo
echo -e $purple"Author   : "$red"AsecC|~|eror404"
echo -e $purple"Team     : "$red"HaxID"
echo -e $purple"github   : "$red"https://github.com/muhammadfathul"
echo -e $purple"Contact  : "$red"085218949365"
echo
echo -e $brown "*===========================================================*"
echo
trap ctrl_c INT
ctrl_c() {
clear
echo -e $blue " [*] (Ctrl + C ) Detected, Trying To Exit ... "
echo -e $green " [*] Thanks"
sleep 1
echo -e $cyan " [*] Semoga Bermanfaat "
echo -e $purple " [*] By AsecC eror404 :)..."
sleep 1
exit
}
lagi=1
while [ $lagi -lt 14 ];
do
echo
echo -e $yellow "                    Tampilan Exs"
echo -e $red "<|--------------------------------------------------------|>"
echo -e $white "[01] Termux BOM"
echo -e $white "[02] Termux Pedang"
echo -e $white "[03] Termux Suriken "
echo -e $white "[04] Termux Cap Lima Jari"
echo -e $white "[05] Termux Topeng Anonymouse"
echo -e $red "<|--------------------------------------------------------|>"
echo
echo ""
echo -e $yellow "                  Tampilan Cowsay"
echo -e $red "<|--------------------------------------------------------|>"
echo -e $white "[1] beavis.zen         $white[15] ghostbusters  $white[29] ren"
echo -e $white "[2] bong               $white[16] head-in       $white[30] sheep"
echo -e $white "[3] bud-frogs          $white[17] hellokitty    $white[31] skeleton"
echo -e $white "[4] bunny              $white[18] kiss          $white[32] stegosaurus"
echo -e $white "[5] cheese             $white[19] kitty         $white[33] stimpy"
echo -e $white "[6] cower              $white[20] koala         $white[34] three-eyes"
echo -e $white "[7] daemon             $white[21] kosh          $white[35] turkey"
echo -e $white "[8] default            $white[22] luke-koala    $white[36] turtle"
echo -e $white "[9] dragon-and-cow     $white[23] mech-and-cow  $white[37] tux"
echo -e $white "[10] dragon            $white[24] meow          $white[38] vader-koala"
echo -e $white "[11] elephant-in-snake $white[25] milk          $white[39] vader"
echo -e $white "[12] elephant          $white[26] moofasa       $white[40] www"
echo -e $white "[13] eyes              $white[27] moose"
echo -e $white "[14] flaming-sheep     $white[28] mutilated"
echo -e $red "<|--------------------------------------------------------|>"
echo
echo -e $red "[00] ${purple}Keluar"
echo
echo -e $white
read -p "┌──AsecC@eror404~: └╼# " pil;
case $pil in
13) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f eyes $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
1) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f beavis.zen $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
2) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f bong $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
3) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f bud-frogs $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
4) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f bunny $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
5) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f cheese $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
6) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f cower $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
7) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f daemon $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
8) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f default $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
9) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f dragon-and-cow $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
10) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f dragon $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
11) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f elephant-in-snake $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
12) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f elephant $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
14) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f flaming-sheep $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
15) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f ghostbusters $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
16) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f head-in $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
17) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f hellokitty $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
18) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f kiss $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
19) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f kitty $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
20) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f koala $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
21) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f kosh $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
22) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f luke-koala $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
23) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f mech-and-cow $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
24) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f meow $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
29) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f ren $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
30) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f sheep $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
27) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f milk $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
25) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f moofasa $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
26) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f moose $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
28) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f mutilated $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
31) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f skeleton $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
32) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f stegosaurus $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
33) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f stimpy $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
34) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f three-eyes $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
35) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f turkey $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
36) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f turtle $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
37) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f tux $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
38) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f vader-koala $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
39) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f vader $t | lolcat" >> bash.bashrc
echo "figlet -f emboss $t | lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
40) echo ""
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
touch bash.bashrc
echo "clear" >> bash.bashrc
echo "blue='\e[1;34m'" >> bash.bashrc
echo "green='\e[0;23m'" >> bash.bashrc
echo "purple='\e[1;35m'" >> bash.bashrc
echo "cyan='\e[1;36m'" >> bash.bashrc
echo "red='\e[1;31m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "cowsay -f www $t | lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "figlet -f emboss $t | lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${blue}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${blue}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
01)
echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
echo "clear" >> bash.bashrc
echo "black='\e[0;30m'" >> bash.bashrc
echo "blue='\e[0;34m'" >> bash.bashrc
echo "green='\e[0;32m'" >> bash.bashrc
echo "cyan='\e[0;36m'" >> bash.bashrc
echo "red='\e[0;31m'" >> bash.bashrc
echo "purple='\e[0;35m'" >> bash.bashrc
echo "brown='\e[0;33m'" >> bash.bashrc
echo "lightgray='\e[0;37m'" >> bash.bashrc
echo "darkgray='\e[1;30m'" >> bash.bashrc
echo "lightblue='\e[1;34m'" >> bash.bashrc
echo "lightgreen='\e[1;32m'" >> bash.bashrc
echo "lightcyan='\e[1;36m'" >> bash.bashrc
echo "lightred='\e[1;31m'" >> bash.bashrc
echo "lightpurple='\e[1;35m'" >> bash.bashrc
echo "yellow='\e[1;33m'" >> bash.bashrc
echo "white='\e[1;37m'" >> bash.bashrc
echo "nc='\e[0m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo
echo "echo -e '\e[1;36m''                            D################D                        '" >> bash.bashrc
echo "echo -e '\e[1;36m''                      ;#####DDDDDDDDDDDDDDDDDDW####                   '" >> bash.bashrc
echo "echo -e '\e[1;36m''                   ###DDDDDDDDDDDDDDDDDDDDDDDDDDDDD#                  '" >> bash.bashrc
echo "echo -e '\e[1;36m''                  ##DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD#                 '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 #DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDW#                '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 #DDDDDDDDDDDDDKKKDDDDDDDDDDDDDDDDDDD#                '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 #DDDKKKDDKELLLLLLLDDWiDDDDDDDDDDDDDDE#               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 WDDDKKKDDKLLLLLLLLDDEiDDDDDDDDDDDDDDD#               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 WDDDDKDDDELLLLLLLii;Ei;iiiDDDDDDDDDDDE#              '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 #DDDDDDDWLLLLLLiWLLDDKDDD#iiDDDDDDDDDD#              '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 #KDDDDDWLLLLLLiLLLLLLLLKKKKiiDDDDDDDDDW#             '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 #KKLKKGLLLLLLiLLLLLLLLLKKKKKiiKKKKKDDDD#             '" >> bash.bashrc
echo "echo -e '\e[1;36m''                  #KLLLLLLLLLiLLLLLLLLLL#KKKKKiKKKKKKDDDKK            '" >> bash.bashrc
echo "echo -e '\e[1;36m''                   #LLLLLLLLjWLLLLLLLLLL# #####i#####DDDD#            '" >> bash.bashrc
echo "echo -e '\e[1;36m''                   #LLLjjjjjiffLLLLLLLLLL     #i#   #KDDD#            '" >> bash.bashrc
echo "echo -e '\e[1;36m''                  #ittttjjjjiffLLLLLLLLLL#    WiK#   #DDDE#           '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 #iittttjjjjiffLLLLLLLLLLL#    iW#   #KDDD#           '" >> bash.bashrc
echo "echo -e '\e[1;36m''                #iiittttjjjjiffLLLLLLLLLLLL#  KiK#    #DDD#           '" >> bash.bashrc
echo "echo -e '\e[1;36m''               #iiiittttjtGDiGDDDDDDDLLLLLLL# #i#     #KDDD#          '" >> bash.bashrc
echo "echo -e '\e[1;36m''               #iiGGGGGGGGGGjiDDDDDDDDDEEEELL##i#      #DDD#          '" >> bash.bashrc
echo "echo -e '\e[1;36m''              #LLLLGGGGGGGGGGiGDDDDDDDDEEEEEE#iK#      #DDDKi         '" >> bash.bashrc
echo "echo -e '\e[1;36m''              #LLLLGGGGGGGGGGGiDDDDDDDDEEEEEEiW#        #DDD#         '" >> bash.bashrc
echo "echo -e '\e[1;36m''              #LLLLGGGGGGGGGGGDiDDDDDDDEEEEEiW#         #DDD#         '" >> bash.bashrc
echo "echo -e '\e[1;36m''              #LLLLGGGDDttttttjEiiEEEDDEEEiiK#          #DDDKW        '" >> bash.bashrc
echo "echo -e '\e[1;36m''             ##LGDDDDDtttttttttjDEiiiiiiiiKKE##;         #DDD#        '" >> bash.bashrc
echo "echo -e '\e[1;36m''           ##DDjDDDDDtttttttttjjjEEEEjjjjffffKKK##       #DDD#        '" >> bash.bashrc
echo "echo -e '\e[1;36m''          #DDiiiiiDDEttttttttjjjjEEEEEjjffffffKKK##      #DDDKt       '" >> bash.bashrc
echo "echo -e '\e[1;36m''         #DiiiiiitDDttttttttjjjjjjEEEEjfffffffGKKK#D      #DDD#       '" >> bash.bashrc
echo "echo -e '\e[1;36m''        #iiiiiiitDDDtttttttjjjjjjjEEEEKffffffffKKKK#      #DDD#       '" >> bash.bashrc
echo "echo -e '\e[1;36m''       #iiiiiiittDDtttttttjjjjjjjjEEEEKfffffffffKKWW#     #DDD#       '" >> bash.bashrc
echo "echo -e '\e[1;36m''      #DiiiiiittfDDttttttjjjjjjjjjEEKKKffffffffLEWWW#     LDDDW#      '" >> bash.bashrc
echo "echo -e '\e[1;36m''      #iiiiiitttDDDtttttjjjjjjjjjjDEKKKKffffffLLEWWWW#     #DDD#      '" >> bash.bashrc
echo "echo -e '\e[1;36m''     #iiiiiitttiDDEttttjjjjjjjjjjjfKKKKKfffffLLLEEWWW#     #DDD#      '" >> bash.bashrc
echo "echo -e '\e[1;36m''     #iiiiittttDDDDtttjjjjjjjjjjjfKKKKKKfffffLLLEEWWWW#    #DDDK#     '" >> bash.bashrc
echo "echo -e '\e[1;36m''    #iiiiitttttDDDDttjjjjtfEKEEEKKKKKKKKKfffLLLLEEEWWW#     #DDK#     '" >> bash.bashrc
echo "echo -e '\e[1;36m''    #iiiitttttDDDDDEEEEEEEEEEEEKKKKKKKKKKKKKfLLLEEEWWWW#    #DDD#     '" >> bash.bashrc
echo "echo -e '\e[1;36m''   iiiiittttDDDDDDEEEEEEEEEEEEKKKKKKKKKKKKKWWWWWEEEWWWW#    #DDD#     '" >> bash.bashrc
echo "echo -e '\e[1;36m''    #jjEDDDDDDDDDEEEEEEEEEEEEKKKKKKKKKKKKKWWWWWWWWWWWW##    #DDDK#    '" >> bash.bashrc
echo "echo -e '\e[1;36m''    ##DDDDDDDDDDEEEEEEEEEEEEKEKKKKKKKKKKKWWWWWWWWWWWW#W#     #DDW#    '" >> bash.bashrc
echo "echo -e '\e[1;36m''     #DDDDDDDDDEEEjjjjjjjjjjfffffffWKKKKWWWfEWWWWWWW###      #DDD#    '" >> bash.bashrc
echo "echo -e '\e[1;36m''     #DDDDDEDDEEEjjjjjjjjjjfffffffffKKKWWWLLLLLLEEW####      #DDD#    '" >> bash.bashrc
echo "echo -e '\e[1;36m''   ##DEttttttEEEEjjjjjjjjjffffffffffKKWWWWLLLLLLEEEE#####    #DDDW#   '" >> bash.bashrc
echo "echo -e '\e[1;36m''  #ttttttttttEEEjjjjjjjjjfffffffffffKWWWWWLLLLLGEEEEE#####   .DDDK#   '" >> bash.bashrc
echo "echo -e '\e[1;36m'' #tttttttttttEEEjjjjjjjjfffffffffffLWWWWWWLLLLGDEEEEE######   #DDD#   '" >> bash.bashrc
echo "echo -e '\e[1;36m'' #ttttttttttjEEEjjjjjjjfffffffffffLLWWWWWWLLLGGEEEEEEE#####   #DDD#   '" >> bash.bashrc
echo "echo -e '\e[1;36m'' #tttttttttjtEEEjjjjjjfffffffffffLLLWWWWWWLLGGGEEEEEEE#####   #DDDK   '" >> bash.bashrc
echo "echo -e '\e[1;36m''#tttttttttjjEEEEjjjjjfffffffffffLLLLWWWWWWLGGGGEEEEEEE#####   #DDDK#  '" >> bash.bashrc
echo "echo -e '\e[1;36m''#ttttttttjjjEEEEjjjjfffffffffffLLLLLWWWWWWGGGGGEEEEEEE#####    WDDK#  '" >> bash.bashrc
echo "echo -e '\e[1;36m''#tttttttjjjjEEEEjjjfffffffffffLLLLLLWWWWWWGGGGGEEEEEEE######   #DDD#  '" >> bash.bashrc
echo "echo -e '\e[1;36m''#ttttttjjjjjEEEEjjfffffffffffLLLLLLLWWWWWWLGGGEEEEEEEE######   #DDD#  '" >> bash.bashrc
echo "echo -e '\e[1;36m''#tttttjjjjjjEEEEjfffffffffffLLLLLLLL#WWWW#DGGGEEEEEEEE######   #DDDW  '" >> bash.bashrc
echo "echo -e '\e[1;36m''#ttttjjjjjjjEEEKffffffffffffLLLLLLLL#WWW###GGGEEEEEEEE######   #DDDW# '" >> bash.bashrc
echo "echo -e '\e[1;36m''#tttjjjjjjjjEEKKfffffffffffLLLLLLLLLWWW####GGDEEEEEEEE######   ,DDDK# '" >> bash.bashrc
echo "echo -e '\e[1;36m''#ttjjjjjjjjKEKKKKKKKKKKKKKWWWWWWWWWWWW######GEEEEEEEEE######    #DDW# '" >> bash.bashrc
echo "echo -e '\e[1;36m''#ttjjjjEEEEEKKKKKKKKKKKKKWWWWWWWWWWWW###############E######     #DDD# '" >> bash.bashrc
echo "echo -e '\e[1;36m'' ##EEEEEEEEKKKKKKKKKKKKKWWWWWWWWWWWW#######################     #DDD# '" >> bash.bashrc
echo "echo -e '\e[1;36m''   #EEEEEEKKKKKKKKKKKKKWWWWWWWWWWWW#####################        #DDDK '" >> bash.bashrc
echo "echo -e '\e[1;36m''  ##EEEEEKKKKKKKKKffffLLLLLLLLLLLGG#########EEEEEEK######       #DDDK#'" >> bash.bashrc
echo "echo -e '\e[1;36m'' ##jjjjjjjfjKKKKWffffLLLLLLLLLLLGGGG#######EEEEEEEEEE#####      #DDDK#'" >> bash.bashrc
echo "echo -e '\e[1;36m'' #jjjjjjjfffKKKKffffLLLLLLLLLLLGGGGG######DEEEEEEEEEE#####       #DDK#'" >> bash.bashrc
echo "echo -e '\e[1;36m'' #jjjjjjfffffKKKDffLLLLLLLLLLLGGGGGG######EEEEEEEEEEE#####t      #DDK#'" >> bash.bashrc
echo "echo -e '\e[1;36m'' #jjjjjffffffKKKKfLLLLLLLLLLLGGGGGGG######EEEEEEEEEE######       #DDK#'" >> bash.bashrc
echo "echo -e '\e[1;36m''  #jjjfffffffWKKKLLLLLLLLLLLGGGGGGGG#####EEEEEEEEEEE######       #DKK#'" >> bash.bashrc
echo "echo -e '\e[1;36m''  #jjfffffffffKKWLLLLLLLLLLGGGGGGGGG#####EEEEEEEEEEE######       #DKK#'" >> bash.bashrc
echo "echo -e '\e[1;36m''  #fffffffffffKWWLLLLLLLLLGGGGGGGGGG#####EEEEEEEEEE######K       #KKK#'" >> bash.bashrc
echo "echo -e '\e[1;36m''   #ffffffffffWWWLLLLLLLLGGGGGGGGGGG#####EEEEEEEEEE######        ,WK# '" >> bash.bashrc
echo "echo -e '\e[1;36m''   #fffffffffLWWWfLLLLLLGGGGGGGGGGGG####EEEEEEEEEEE######         ### '" >> bash.bashrc
echo "echo -e '\e[1;36m''    #fffffffLLfWWWLLLLLLGGGGGGGGGGD#####EEEEEEEEEE######              '" >> bash.bashrc
echo "echo -e '\e[1;36m''    #fffffffLLLWWWLLLLLGGGGGGGGGGDD#####EEEEEEEEEE#####K              '" >> bash.bashrc
echo "echo -e '\e[1;36m''     #fffffLLLDWWWWGLLGGGGGGGGGGDD#######EEEEEEEE######               '" >> bash.bashrc
echo "echo -e '\e[1;36m''      ##KWWWWWWWWWWWW################################                 '" >> bash.bashrc
echo "echo -e '\e[1;36m''        E##WWWWWWWWW##############################                    '" >> bash.bashrc
echo "echo -e '\e[1;36m''          #WWWWWWWW###############################                    '" >> bash.bashrc
echo "echo -e '\e[1;36m''          #DLfL#WW########################W########                   '" >> bash.bashrc
echo "echo -e '\e[1;36m''         #LLLLLLL####GGGGGGGDDDEE#####EEEEEEEE#####                   '" >> bash.bashrc
echo "echo -e '\e[1;36m''         #LLLLLLGG###GGGGGGDDEEEEE####EEEEEEE######                   '" >> bash.bashrc
echo "echo -e '\e[1;36m''          #LLLLGGGE##GGGGGDEEEEEEE###EEEEEEEW#####                    '" >> bash.bashrc
echo "echo -e '\e[1;36m''          ##LLGGGGG##GGGGEEEEEEEE###EEEEEEEE######                    '" >> bash.bashrc
echo "echo -e '\e[1;36m''           ##GGGGGGG##DEEEEEEEEEE###EEEEEEE######                     '" >> bash.bashrc
echo "echo -e '\e[1;36m''            ##LLGEEEE#EEEEEEEEEEW##EEEEEEE######                      '" >> bash.bashrc
echo "echo -e '\e[1;36m''             D#EEEEEE##EEEEEEEEE###EEEEEE######                       '" >> bash.bashrc
echo "echo -e '\e[1;36m''               #EEEEEE#EEEEEEEEE##EEEEEE######                        '" >> bash.bashrc
echo "echo -e '\e[1;36m''                ##EEEEE#EEEEEEE###EEEE######                          '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 ###EEE##EEEEEE# #EEE#####j                           '" >> bash.bashrc
echo "echo -e '\e[1;36m''                    ###  ######   ###                                 '" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "figlet -f emboss $t | lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${lightgreen}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${lightgreen}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
02) echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
echo "clear" >> bash.bashrc
echo "black='\e[0;30m'" >> bash.bashrc
echo "blue='\e[0;34m'" >> bash.bashrc
echo "green='\e[0;32m'" >> bash.bashrc
echo "cyan='\e[0;36m'" >> bash.bashrc
echo "red='\e[0;31m'" >> bash.bashrc
echo "purple='\e[0;35m'" >> bash.bashrc
echo "brown='\e[0;33m'" >> bash.bashrc
echo "lightgray='\e[0;37m'" >> bash.bashrc
echo "darkgray='\e[1;30m'" >> bash.bashrc
echo "lightblue='\e[1;34m'" >> bash.bashrc
echo "lightgreen='\e[1;32m'" >> bash.bashrc
echo "lightcyan='\e[1;36m'" >> bash.bashrc
echo "lightred='\e[1;31m'" >> bash.bashrc
echo "lightpurple='\e[1;35m'" >> bash.bashrc
echo "yellow='\e[1;33m'" >> bash.bashrc
echo "white='\e[1;37m'" >> bash.bashrc
echo "nc='\e[0m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[1;35m''KE                                                       '" >> bash.bashrc
echo "echo -e '\e[1;35m'' WWKDG                                                      '" >> bash.bashrc
echo "echo -e '\e[1;35m''tWKW,GE                                                     '" >> bash.bashrc
echo "echo -e '\e[1;35m''#WWL GG                                                     '" >> bash.bashrc
echo "echo -e '\e[1;35m''#W .EGG                                                     '" >> bash.bashrc
echo "echo -e '\e[1;35m'' EEDGGGG.                                                   '" >> bash.bashrc
echo "echo -e '\e[1;35m''  EDGGEKK                                                   '" >> bash.bashrc
echo "echo -e '\e[1;35m'' G WWKD                                                  '" >> bash.bashrc
echo "echo -e '\e[1;35m'' .#WWK K                                                 '" >> bash.bashrc
echo "echo -e '\e[1;35m''    WWK .                                                '" >> bash.bashrc
echo "echo -e '\e[1;35m''     #WKK          DG                                    '" >> bash.bashrc
echo "echo -e '\e[1;35m''     W W#K        EGGG                                   '" >> bash.bashrc
echo "echo -e '\e[1;35m''      WK W i     EiGG                                    '" >> bash.bashrc
echo "echo -e '\e[1;35m''      tWEKWK    j.                                       '" >> bash.bashrc
echo "echo -e '\e[1;35m''         KKKK  G                                         '" >> bash.bashrc
echo "echo -e '\e[1;35m''         .KK.DGG                                         '" >> bash.bashrc
echo "echo -e '\e[1;35m''         ;KWK GG                                         '" >> bash.bashrc
echo "echo -e '\e[1;35m''          KDEi                                           '" >> bash.bashrc
echo "echo -e '\e[1;35m''          ED,#GE L                                       '" >> bash.bashrc
echo "echo -e '\e[1;35m''         EEDGK EEWK                                      '" >> bash.bashrc
echo "echo -e '\e[1;35m''        G#    DKKE                                       '" >> bash.bashrc
echo "echo -e '\e[1;35m''       G     W EKKKE                                     '" >> bash.bashrc
echo "echo -e '\e[1;35m''      D,      K#KKKEE                                    '" >> bash.bashrc
echo "echo -e '\e[1;35m''     EDG#       GKKKL#                                   '" >> bash.bashrc
echo "echo -e '\e[1;35m''     EDG         LKKKL                                   '" >> bash.bashrc
echo "echo -e '\e[1;35m''      f           GKKKf                                  '" >> bash.bashrc
echo "echo -e '\e[1;35m''                  tKKKKD                                 '" >> bash.bashrc
echo "echo -e '\e[1;35m''                   EKKKKE                                '" >> bash.bashrc
echo "echo -e '\e[1;35m''                    EKKKKE                               '" >> bash.bashrc
echo "echo -e '\e[1;35m''                     EKKKKE                              '" >> bash.bashrc
echo "echo -e '\e[1;35m''                      EKKKKE                             '" >> bash.bashrc
echo "echo -e '\e[1;35m''                       EKKKKE                            '" >> bash.bashrc
echo "echo -e '\e[1;35m''                        EKKKKE                           '" >> bash.bashrc
echo "echo -e '\e[1;35m''                         tKKKKE                          '" >> bash.bashrc
echo "echo -e '\e[1;35m''                          jKKKWE                         '" >> bash.bashrc
echo "echo -e '\e[1;35m''                           fKKW#W                        '" >> bash.bashrc
echo "echo -e '\e[1;35m''                            GWWWt                        '" >> bash.bashrc
echo "echo -e '\e[1;35m''                             WWWWj                       '" >> bash.bashrc
echo "echo -e '\e[1;35m''                             #WWWWt                      '" >> bash.bashrc
echo "echo -e '\e[1;35m''                              EWWWWE                     '" >> bash.bashrc
echo "echo -e '\e[1;35m''                               EWWWWW                    '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                EWWWWE                   '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                 EWWWWE                  '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                  EWWWWE                 '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                  jGWWWWE                '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                   .tWWWWE               '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                     fWWWW#              '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                      jWWW#              '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                       DWWWD             '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                       GWWWWL            '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                        EWWWWf           '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                         EWWWWf          '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                          EWWW#K         '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                           EW###E        '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                            E####E       '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                             E####f      '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                              E####      '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                              ;E###L     '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                                E###E    '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                                 ED#E    '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                                   EEE   '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                                    EEE  '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                                     tE  '" >> bash.bashrc
echo "echo -e '\e[1;35m''                                                       E '" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${lightgreen}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${lightgreen}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
03) echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
echo "clear" >> bash.bashrc
echo "black='\e[0;30m'" >> bash.bashrc
echo "blue='\e[0;34m'" >> bash.bashrc
echo "green='\e[0;32m'" >> bash.bashrc
echo "cyan='\e[0;36m'" >> bash.bashrc
echo "red='\e[0;31m'" >> bash.bashrc
echo "purple='\e[0;35m'" >> bash.bashrc
echo "brown='\e[0;33m'" >> bash.bashrc
echo "lightgray='\e[0;37m'" >> bash.bashrc
echo "darkgray='\e[1;30m'" >> bash.bashrc
echo "lightblue='\e[1;34m'" >> bash.bashrc
echo "lightgreen='\e[1;32m'" >> bash.bashrc
echo "lightcyan='\e[1;36m'" >> bash.bashrc
echo "lightred='\e[1;31m'" >> bash.bashrc
echo "lightpurple='\e[1;35m'" >> bash.bashrc
echo "yellow='\e[1;33m'" >> bash.bashrc
echo "white='\e[1;37m'" >> bash.bashrc
echo "nc='\e[0m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[1;36m''                ###                         ####              '" >> bash.bashrc
echo "echo -e '\e[1;36m''                #####                      #####              '" >> bash.bashrc
echo "echo -e '\e[1;36m''                ##,###                    ###,;#              '" >> bash.bashrc
echo "echo -e '\e[1;36m''                ##;;;##                 ####;ii#              '" >> bash.bashrc
echo "echo -e '\e[1;36m''                ##it;i###              ###;iLGi#              '" >> bash.bashrc
echo "echo -e '\e[1;36m''                ##ittiiG##           ####itLLiiD              '" >> bash.bashrc
echo "echo -e '\e[1;36m''                ##ttttttt##;        ####itLLLii               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                ##tittttjj###      ###itffLLLi#               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                #jtitttttff##   ####tjfffffLi#               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                #jtiiittttfL#   ##Gjffffffffi#               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                ##tiiiiittt,#   ##ttjjjfffff;#               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                ##jiiiiiii,,#    ##jjjjjjfff;#               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                ##j;iiiiii,,#    ##jjjjjjjff;#               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                ##f;;iiiii,,#   ###jtjjjjjjf;#               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                ##f;;;;iiii,######jftttjjjj;,;               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 ##L;i;;;;ii,,####jjtttttj,,;,                '" >> bash.bashrc
echo "echo -e '\e[1;36m''                  ###.tt;;;;i;;ittjittttj,###                 '" >> bash.bashrc
echo "echo -e '\e[1;36m''                    ##t,;;;;;iiiiiiiitt,#                    '" >> bash.bashrc
echo "echo -e '\e[1;36m''                    ##j;;;;;;iiiiiiiit;#                    '" >> bash.bashrc
echo "echo -e '\e[1;36m''            ###     ##f,;;;;;;;iiiiiii;#    ####K           '" >> bash.bashrc
echo "echo -e '\e[1;36m''          ######    ##f,,,;;;;;;;iiiiii##  ###,####         '" >> bash.bashrc
echo "echo -e '\e[1;36m''        #####L:##  ###L,,,,,;;ii;;;iiiit#####j,,,####       '" >> bash.bashrc
echo "echo -e '\e[1;36m''     #####ffL,tt#####L,,,,,;;t#itt;;;iitt###jftt;;i####     '" >> bash.bashrc
echo "echo -e '\e[1;36m''   #####jjji;;;tjjffL,,,,,;;#  ##tj;;;iijjjjfitttttttt####  '" >> bash.bashrc
echo "echo -e '\e[1;36m'' #####tttiiii;;;;Lf,,,,,,;;#    ##j,;;;;iiiiiiiitttttjjf####'" >> bash.bashrc
echo "echo -e '\e[1;36m''###,;ittiiiiiii;;;;;;;,,,;#      #Lj;;;;;;iiiiiiiitttttfLL##'" >> bash.bashrc
echo "echo -e '\e[1;36m''#,,,ttttttiiiiiii;;;;;;,,;#      ##f,;;;;;;;iiiiiiiittttt,,,'" >> bash.bashrc
echo "echo -e '\e[1;36m''###;;ittttttiiiiiii;;;;;;;##    ##jf,,;;;;;;;iiiiiiiii,,,G# '" >> bash.bashrc
echo "echo -e '\e[1;36m''  ###iittttttiiiiiii;;;;;;i##  ###f:,,,,;;,;;;;iiiii,,,##   '" >> bash.bashrc
echo "echo -e '\e[1;36m''     ##itjttttti,;;;ii;;;;ii#####jf,,,,,,,;;it;;;i,,,##     '" >> bash.bashrc
echo "echo -e '\e[1;36m''       ###ffftt,;###iiii;;;tti#jjf,,,,,,#####tj,,,i#        '" >> bash.bashrc
echo "echo -e '\e[1;36m''         ###LLG;#  ##ttiii;;;tjj,,,,,,,,:   ##,,##          '" >> bash.bashrc
echo "echo -e '\e[1;36m''           K##G#    ##tiiiii;;;;;;,,,,,#     ###            '" >> bash.bashrc
echo "echo -e '\e[1;36m''                    ##jiiiiii;;;;;;;,,,#                    '" >> bash.bashrc
echo "echo -e '\e[1;36m''                    ##jtiiiiiii;;;;;;;,##                   '" >> bash.bashrc
echo "echo -e '\e[1;36m''                   #####jtttiiiiiii;;;;;;;####                '" >> bash.bashrc
echo "echo -e '\e[1;36m''                  #####jtttttt;;iitji;;;;;iE###               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 ;#jjjfjjtttt,:####jjii;;;;tt,#               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 ##jfjjjjjjt,;#   ##fiii;;;;;,#               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 ##jffjjjjjj,#    ##fLiiii;;;,#               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 ##jffffjjjj,#    ##ffiiiiii;,#               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 ##fffffffjj;##   ##fitiiiiii,#               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 ##ffffffffj,,#   ##Lttttiiii,#               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 ##fLLfffff;;L#   ##iittttiii,:               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 ##fLLLLff;;#      ##itttttti,,#              '" >> bash.bashrc
echo "echo -e '\e[1;36m''                  #ffLLLLL;;#        f##jftttt;,#              '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 D#jfLLLi;##           ##fLtttt,#              '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 ##jfLLi;#              ##GGDtt,#              '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 ##jLii,#                 ##GGt,#              '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 ##jii#                    ##GG;#              '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 ##:i#                      ###t#              '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 ####                         ###              '" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${lightgreen}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${lightgreen}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
04) echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
echo "clear" >> bash.bashrc
echo "black='\e[0;30m'" >> bash.bashrc
echo "blue='\e[0;34m'" >> bash.bashrc
echo "green='\e[0;32m'" >> bash.bashrc
echo "cyan='\e[0;36m'" >> bash.bashrc
echo "red='\e[0;31m'" >> bash.bashrc
echo "purple='\e[0;35m'" >> bash.bashrc
echo "brown='\e[0;33m'" >> bash.bashrc
echo "lightgray='\e[0;37m'" >> bash.bashrc
echo "darkgray='\e[1;30m'" >> bash.bashrc
echo "lightblue='\e[1;34m'" >> bash.bashrc
echo "lightgreen='\e[1;32m'" >> bash.bashrc
echo "lightcyan='\e[1;36m'" >> bash.bashrc
echo "lightred='\e[1;31m'" >> bash.bashrc
echo "lightpurple='\e[1;35m'" >> bash.bashrc
echo "yellow='\e[1;33m'" >> bash.bashrc
echo "white='\e[1;37m'" >> bash.bashrc
echo "nc='\e[0m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[1;36m''                       ####E                                          '" >> bash.bashrc
echo "echo -e '\e[1;36m''                       #####                                          '" >> bash.bashrc
echo "echo -e '\e[1;36m''                      #######                                         '" >> bash.bashrc
echo "echo -e '\e[1;36m''                      #######                                         '" >> bash.bashrc
echo "echo -e '\e[1;36m''                      #######                                         '" >> bash.bashrc
echo "echo -e '\e[1;36m''                     ########               ;                         '" >> bash.bashrc
echo "echo -e '\e[1;36m''                     ########             #####                       '" >> bash.bashrc
echo "echo -e '\e[1;36m''    ###W             ########            #######                      '" >> bash.bashrc
echo "echo -e '\e[1;36m''   W####             ########           ########                      '" >> bash.bashrc
echo "echo -e '\e[1;36m''   #####;            ########          #########                      '" >> bash.bashrc
echo "echo -e '\e[1;36m''   ######            #######           #########                      '" >> bash.bashrc
echo "echo -e '\e[1;36m''   #####W             W#####           ########                       '" >> bash.bashrc
echo "echo -e '\e[1;36m''   #####W             ##  #           #########                       '" >> bash.bashrc
echo "echo -e '\e[1;36m''   #####W            #:  ;            ########W                       '" >> bash.bashrc
echo "echo -e '\e[1;36m''      ###           #######           ########                        '" >> bash.bashrc
echo "echo -e '\e[1;36m''   :#####           #######W         #########            ###W        '" >> bash.bashrc
echo "echo -e '\e[1;36m''    #####           ########         ########           W#####W       '" >> bash.bashrc
echo "echo -e '\e[1;36m''    ######          ########         ########           #######       '" >> bash.bashrc
echo "echo -e '\e[1;36m''    ######          #######G        #########          ########       '" >> bash.bashrc
echo "echo -e '\e[1;36m''    ######          #######         #########         #########       '" >> bash.bashrc
echo "echo -e '\e[1;36m''    #######        :#######        ###     #          ########        '" >> bash.bashrc
echo "echo -e '\e[1;36m''    #######        G#######        ####              #########        '" >> bash.bashrc
echo "echo -e '\e[1;36m''    #######        #######:       #######W          #########         '" >> bash.bashrc
echo "echo -e '\e[1;36m''    #######        W######        #########         #########         '" >> bash.bashrc
echo "echo -e '\e[1;36m''     ######        W###           #########         #######           '" >> bash.bashrc
echo "echo -e '\e[1;36m''     ######         ####GW       W########         ########           '" >> bash.bashrc
echo "echo -e '\e[1;36m''        ####        #            #########        ########            '" >> bash.bashrc
echo "echo -e '\e[1;36m''      ######       ######,       #########          ######            '" >> bash.bashrc
echo "echo -e '\e[1;36m''       #####       #######      G########        #  #####             '" >> bash.bashrc
echo "echo -e '\e[1;36m''       #####       ######;         ######       #########             '" >> bash.bashrc
echo "echo -e '\e[1;36m''       #####       ######        #W#####        ########              '" >> bash.bashrc
echo "echo -e '\e[1;36m''       #####       ######       ##### #        ######                 '" >> bash.bashrc
echo "echo -e '\e[1;36m''       #####       #####W       ######        #######W                '" >> bash.bashrc
echo "echo -e '\e[1;36m''       ,####       #####       ########       ########                '" >> bash.bashrc
echo "echo -e '\e[1;36m''        ####       ####        #######       ########                 '" >> bash.bashrc
echo "echo -e '\e[1;36m''        W##                    #######       ########                 '" >> bash.bashrc
echo "echo -e '\e[1;36m''        ######       ########                  '" >> bash.bashrc
echo "echo -e '\e[1;36m''        ,####K      ### W###                   '" >> bash.bashrc
echo "echo -e '\e[1;36m''             #####              ###       #####  #                    '" >> bash.bashrc
echo "echo -e '\e[1;36m''          ###########                    ######                       '" >> bash.bashrc
echo "echo -e '\e[1;36m''         #############j  W####           #######                      '" >> bash.bashrc
echo "echo -e '\e[1;36m''       ########################         ########                      '" >> bash.bashrc
echo "echo -e '\e[1;36m''      ###########################       #######                       '" >> bash.bashrc
echo "echo -e '\e[1;36m''     #############################      #####                         '" >> bash.bashrc
echo "echo -e '\e[1;36m''    W###########E################## W#  W###                          '" >> bash.bashrc
echo "echo -e '\e[1;36m''    ###################################W                              '" >> bash.bashrc
echo "echo -e '\e[1;36m''   ############ W######f#################                             '" >> bash.bashrc
echo "echo -e '\e[1;36m''   ############ ;###### ##################                            '" >> bash.bashrc
echo "echo -e '\e[1;36m''   #################### ##################                            '" >> bash.bashrc
echo "echo -e '\e[1;36m''  #####  ############## ######### #########                           '" >> bash.bashrc
echo "echo -e '\e[1;36m''  ####W  W###   ####### ######## W#########                           '" >> bash.bashrc
echo "echo -e '\e[1;36m''  ######  ######W    ######### ############                           '" >> bash.bashrc
echo "echo -e '\e[1;36m''  ##########  ##########   ###### ########,                           '" >> bash.bashrc
echo "echo -e '\e[1;36m''  #########################W  ### W#######                            '" >> bash.bashrc
echo "echo -e '\e[1;36m''  #############################  ########                             '" >> bash.bashrc
echo "echo -e '\e[1;36m'' :############# ###G ############  #####                              '" >> bash.bashrc
echo "echo -e '\e[1;36m'' W###############W       ########   #                                 '" >> bash.bashrc
echo "echo -e '\e[1;36m'' ######################        G #  W#                                '" >> bash.bashrc
echo "echo -e '\e[1;36m'' ####################  ;  W W###W #######                             '" >> bash.bashrc
echo "echo -e '\e[1;36m'' ################# ;######### #####W                                  '" >> bash.bashrc
echo "echo -e '\e[1;36m'' ###############  ############# ########                              '" >> bash.bashrc
echo "echo -e '\e[1;36m'' ############## ################W ########                            '" >> bash.bashrc
echo "echo -e '\e[1;36m'' #################################:########                           '" >> bash.bashrc
echo "echo -e '\e[1;36m''E##########################################                           '" >> bash.bashrc
echo "echo -e '\e[1;36m''W##########################################                   G       '" >> bash.bashrc
echo "echo -e '\e[1;36m''###########################################                ########   '" >> bash.bashrc
echo "echo -e '\e[1;36m''##########################################                ##########  '" >> bash.bashrc
echo "echo -e '\e[1;36m''#########################################              ############## '" >> bash.bashrc
echo "echo -e '\e[1;36m''#########################################            #################'" >> bash.bashrc
echo "echo -e '\e[1;36m''#########################################     W#######################'" >> bash.bashrc
echo "echo -e '\e[1;36m''#########################################W   #########################'" >> bash.bashrc
echo "echo -e '\e[1;36m'' #################### ####################  ##########################'" >> bash.bashrc
echo "echo -e '\e[1;36m'' ###################W#####################  ######################### '" >> bash.bashrc
echo "echo -e '\e[1;36m'' :################## ##################### ########## ##############  '" >> bash.bashrc
echo "echo -e '\e[1;36m''  #################W###################### ######W.   ############    '" >> bash.bashrc
echo "echo -e '\e[1;36m''   W############### #####################t  ##                        '" >> bash.bashrc
echo "echo -e '\e[1;36m''     ############## #####################                             '" >> bash.bashrc
echo "echo -e '\e[1;36m''       W####     ## ####################                              '" >> bash.bashrc
echo "echo -e '\e[1;36m''               #### ###################                               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 ## #################                                 '" >> bash.bashrc
echo "echo -e '\e[1;36m''                     ###############                                  '" >> bash.bashrc
echo "echo -e '\e[1;36m''                     ##############                                   '" >> bash.bashrc
echo "echo -e '\e[1;36m''                      ############                                    '" >> bash.bashrc
echo "echo -e '\e[1;36m''                       ##########                                     '" >> bash.bashrc
echo "echo -e '\e[1;36m''                         ######                                       '" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "figlet -f emboss $t |lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${lightgreen}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${lightgreen}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
05) echo ""
cd /data/data/com.termux/files/usr/etc
cp bash.bashrc /data/data/com.termux/files/home/GGMUX
rm -rf bash.bashrc
touch bash.bashrc
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Tampilan:"
echo
read t
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt User:"
echo
read p1
echo -e $red "<*-------------------------*>"
echo -e $cyan "Masukan Nama Promt Host:"
echo
read p2
echo "clear" >> bash.bashrc
echo "black='\e[0;30m'" >> bash.bashrc
echo "blue='\e[0;34m'" >> bash.bashrc
echo "green='\e[0;32m'" >> bash.bashrc
echo "cyan='\e[0;36m'" >> bash.bashrc
echo "red='\e[0;31m'" >> bash.bashrc
echo "purple='\e[0;35m'" >> bash.bashrc
echo "brown='\e[0;33m'" >> bash.bashrc
echo "lightgray='\e[0;37m'" >> bash.bashrc
echo "darkgray='\e[1;30m'" >> bash.bashrc
echo "lightblue='\e[1;34m'" >> bash.bashrc
echo "lightgreen='\e[1;32m'" >> bash.bashrc
echo "lightcyan='\e[1;36m'" >> bash.bashrc
echo "lightred='\e[1;31m'" >> bash.bashrc
echo "lightpurple='\e[1;35m'" >> bash.bashrc
echo "yellow='\e[1;33m'" >> bash.bashrc
echo "white='\e[1;37m'" >> bash.bashrc
echo "nc='\e[0m'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "#Figlet nama" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[1;36m''                       fLWWW####WEDG                        '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 DE##################W#W#WE                 '" >> bash.bashrc
echo "echo -e '\e[1;36m''             L#################################t            '" >> bash.bashrc
echo "echo -e '\e[1;36m''          K######################################           '" >> bash.bashrc
echo "echo -e '\e[1;36m''         #########################################          '" >> bash.bashrc
echo "echo -e '\e[1;36m''        E##########################################         '" >> bash.bashrc
echo "echo -e '\e[1;36m''        ###########################################W        '" >> bash.bashrc
echo "echo -e '\e[1;36m''       ;############################################        '" >> bash.bashrc
echo "echo -e '\e[1;36m''       K############################################W       '" >> bash.bashrc
echo "echo -e '\e[1;36m''       W#######KW##########################WW########       '" >> bash.bashrc
echo "echo -e '\e[1;36m''       #####fLLLLLLf###################WLLLLLLL######.      '" >> bash.bashrc
echo "echo -e '\e[1;36m''      .W###LLf  i#GLLL###############ELLLKE  ,LLL#####      '" >> bash.bashrc
echo "echo -e '\e[1;36m''      E###L         W##W############GW#L        L#####      '" >> bash.bashrc
echo "echo -e '\e[1;36m''      ###E  fLLi      ###############       fLL; L####      '" >> bash.bashrc
echo "echo -e '\e[1;36m''      ##W LLLLLLLLL     ############    ;LLLLLLLLLE###      '" >> bash.bashrc
echo "echo -e '\e[1;36m''      ###########LLLL    ##########   ;LLL############;     '" >> bash.bashrc
echo "echo -e '\e[1;36m''      #############GLLL   ########   LLL##############W     '" >> bash.bashrc
echo "echo -e '\e[1;36m''      ###############LLLi ######## LLLL################     '" >> bash.bashrc
echo "echo -e '\e[1;36m''      ################LLf##########LLW#################     '" >> bash.bashrc
echo "echo -e '\e[1;36m''      #################LL#########ELW##################     '" >> bash.bashrc
echo "echo -e '\e[1;36m''     :########:,,i,,,W##L#########L####;,,,,,##########     '" >> bash.bashrc
echo "echo -e '\e[1;36m''     ,#K#####,##W   KD,##f########L##,,#KE#W#,t########     '" >> bash.bashrc
echo "echo -e '\e[1;36m''     i##W##W,#         ,j#######EW#;,:       #,E####W##     '" >> bash.bashrc
echo "echo -e '\e[1;36m''     L##LW#,,           ,#######G##,           ,D##W###     '" >> bash.bashrc
echo "echo -e '\e[1;36m''     K###,,,,WK       t,;#######G##,D         #,,,j####     '" >> bash.bashrc
echo "echo -e '\e[1;36m''     G#fKL##K,,,,it;,,,####W####D###:,;W###K;,,t#f,W###     '" >> bash.bashrc
echo "echo -e '\e[1;36m''     L#t#######D,,,j######EW####D####WK,,,,,,W#W###W#W#     '" >> bash.bashrc
echo "echo -e '\e[1;36m''     ,E###################DK####DD#####################     '" >> bash.bashrc
echo "echo -e '\e[1;36m''     :####################DW####DD####################W     '" >> bash.bashrc
echo "echo -e '\e[1;36m''     :###################DDW####DD#####################     '" >> bash.bashrc
echo "echo -e '\e[1;36m''      ###################DDW####DDD####################     '" >> bash.bashrc
echo "echo -e '\e[1;36m''      ##################DDD#####DDDE##################E     '" >> bash.bashrc
echo "echo -e '\e[1;36m''      #################DD#D#####DD#D##################:     '" >> bash.bashrc
echo "echo -e '\e[1;36m''      ##############W##D##D#####KD##D#################      '" >> bash.bashrc
echo "echo -e '\e[1;36m''      ##############f#D###D######D###G#fW##########W##      '" >> bash.bashrc
echo "echo -e '\e[1;36m''      ##f#########ffG#####D######D###D#fff#########L##      '" >> bash.bashrc
echo "echo -e '\e[1;36m''      ##fLf###ELLLK###W###D######D###D###GffL####LLL##      '" >> bash.bashrc
echo "echo -e '\e[1;36m''      G##LL   ########## #DD####DK#W#########K;;jfL###      '" >> bash.bashrc
echo "echo -e '\e[1;36m''      .##LL#  ###########f#WDDDD#j ##########t  #LL##L      '" >> bash.bashrc
echo "echo -e '\e[1;36m''       ##KLDL  ########### L#### ############  WDLE##       '" >> bash.bashrc
echo "echo -e '\e[1;36m''       ###Lf#   #########,        ##########  ;WLL###       '" >> bash.bashrc
echo "echo -e '\e[1;36m''       K##WLDK  W#######K    E     #######W   #ELW###       '" >> bash.bashrc
echo "echo -e '\e[1;36m''       :###fL#   GWWWKt     .##       iDKK   ##LL###L       '" >> bash.bashrc
echo "echo -e '\e[1;36m''        ####LGW             ####            ##LL####        '" >> bash.bashrc
echo "echo -e '\e[1;36m''        ####fLW#           W#####          j#LLf####        '" >> bash.bashrc
echo "echo -e '\e[1;36m''        ,####LLG#####WWW            #WWW####LfL####E        '" >> bash.bashrc
echo "echo -e '\e[1;36m''         #####L#LW##W###WW########W#WW#####f#L#####         '" >> bash.bashrc
echo "echo -e '\e[1;36m''         L####DL#W###W#####WWWWWW########K##fG####W         '" >> bash.bashrc
echo "echo -e '\e[1;36m''          #####f####DW####W############L####L#####          '" >> bash.bashrc
echo "echo -e '\e[1;36m''          .#####L###############W##########L#####L          '" >> bash.bashrc
echo "echo -e '\e[1;36m''           E#####f########W     ##########f#####W           '" >> bash.bashrc
echo "echo -e '\e[1;36m''            K###############    ################            '" >> bash.bashrc
echo "echo -e '\e[1;36m''             W####W#########   ##########K#####             '" >> bash.bashrc
echo "echo -e '\e[1;36m''              W####E########   j########D#####:             '" >> bash.bashrc
echo "echo -e '\e[1;36m''               E############    #############               '" >> bash.bashrc
echo "echo -e '\e[1;36m''                ###########W    ############                '" >> bash.bashrc
echo "echo -e '\e[1;36m''                 E##########    ##########W                 '" >> bash.bashrc
echo "echo -e '\e[1;36m''                  W#########    ##########                  '" >> bash.bashrc
echo "echo -e '\e[1;36m''                   L#######W    ########L                   '" >> bash.bashrc
echo "echo -e '\e[1;36m''                    G#######    ######WL                    '" >> bash.bashrc
echo "echo -e '\e[1;36m''                     f######   f######                      '" >> bash.bashrc
echo "echo -e '\e[1;36m''                       #####.  #####W                       '" >> bash.bashrc
echo "echo -e '\e[1;36m''                        G####  ####t                        '" >> bash.bashrc
echo "echo -e '\e[1;36m''                          K##  ##D                          '" >> bash.bashrc
echo "echo -e '\e[1;36m''                             j                              '" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "figlet -f emboss $t | lolcat" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -ne '${lightgreen}Today is:\t\t${red}' `date`; echo ''" >> bash.bashrc
echo "echo -e '${lightgreen}Kernel Information: \t${red}' `uname -smr`" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;36m' 'Indonesian HaxID Team'" >> bash.bashrc
echo "echo -e '\e[0;36m' ''the quieter you become, the more you able to hear''" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo -e '\e[0;35m' '<|-----------------------------------------------------------------|>'" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "echo" >> bash.bashrc
echo "command_not_found_handle() {" >> bash.bashrc
echo "        /data/data/com.termux/files/usr/libexec/termux/command-not-found ""$1" >> bash.bashrc
echo "}" >> bash.bashrc
echo "" >> bash.bashrc
echo "PS1='\033[01;34m\]┌──\[\033[01;32m\]$p1\[\033[01;34m\]@\[\033[01;31m\]$p2\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]: \[\033[01;34m\]└╼\[\033[01;31m\]#\[\033[01;32m\]'" >> bash.bashrc
echo
sleep 1
bash bash.bashrc
sleep 2
echo
echo -e $cyan "ingin Mengubah Tampilan Termux [Y] / Coba yang lain [T] ("$yellow" Y/T"$cyan" )"$white"\n\n"
read -p "AsecC|~|eror404 ~# " pil3;
if [ $pil3 = y ] || [ $pil3 = Y ];
then
clear
echo -e $cyan "[*]Loading..."
sleep 1
echo -e $cyan "[*]Tunggu Sebentar"
sleep 3
echo -e $purple "[*] Berhasil"
sleep 3
echo -e $purple "[*] Silahkan Buka seasion baru Untuk Melihat Hasil"
sleep 3
else
echo -e $red "Terima Kasih"
rm -rf bash.bashrc
cd /data/data/com.termux/files/home/GGMUX
cp bash.bashrc /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
sleep 2
fi
;;
00) echo -e $purple " [*] Created By : AsecC eror404"
sleep 1
echo -e $cyan " [*] Terima Kasih"
sleep 1
exit
;;
*) echo -e $red "[!] Pilihan Yang anda masukan tidak tersedia!!! "
sleep 2
esac
done
done
