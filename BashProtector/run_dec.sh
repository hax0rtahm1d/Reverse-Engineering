# Deobfuscated BY HTR-TECH | Tahmid Rayat

# Github    : https://github.com/htr-tech 
# Instagram : https://www.instagram.com/tahmid.rayat
# Facebook  : https://fb.com/tahmid.rayat.oficial 
# Messenger : https://m.me/tahmid.rayat.oficial 

#!/bin/bash

ijo='\e[1;32m'
kuning='\e[1;33m'
NC='\e[0;37m'

banner(){
    printf """\x1b[30;1m╔═══════════════════════════════════════════════════════════════╗
║\x1b[31;1m➢ Author : Febry [ xNot_Found ]                                \x1b[30;1m║
║\x1b[32;1m➣ Contact: +62823-8637-2115                                    \x1b[30;1m║
║\x1b[33;1m➢ Email  : febryafriansyah@programmer.net                      \x1b[30;1m║
║\x1b[34;1m➣ Website: http://hatakecnk.noads.biz                          \x1b[30;1m║
║\x1b[37;1m➢ Github : https://github.com/hatakecnk                        \x1b[30;1m║
╚═══════════════════════════════════════════════════════════════╝"""
}

febry(){
    printf "\n\e[31;1m[${NC}+\e[31;1m]${NC} Bash File To Be Obfuscated : ";
    read file
    if [[ ! -f $file ]]; then
        printf "\n\e[31;1m[${NC}+\e[31;1m]${NC} File Not Found..\n"
        exit
    fi
    printf "\e[31;1m[${NC}+\e[31;1m]${NC} Output File (without extension) : ";
    read Out
}

obf(){
    printf "\e[33;1m[${NC}+\e[33;1m]${NC} Obfuscating...\n"
    randm1=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm2=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm3=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm4=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm5=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm6=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm7=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm8=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm9=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm10=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm11=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm12=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm13=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm14=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm15=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm16=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm17=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm18=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm19=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm20=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm21=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm22=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm23=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm24=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm25=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm26=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm27=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm28=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm29=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm30=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm31=$(cat /dev/urandom | tr -dc 'A-Za-z' | fold -w 100 | head -n 1)
    randm32=$(cat /dev/urandom | tr -dc 'A-Za--z' | fold -w 100 | head -n 1)
    febry=$(cat $file | base64 | tr -d '\n' )
    febry=$(echo "$febry" | rev)
    nasa="$randm1=\"$randm2\";$randm3=\"$randm4\";$randm5=\"ch\";$randm6=\"4\";$randm7=\"\";$randm9=\"$randm10\";$randm11=\" $febry | r\";$randm12=\"$randm13\";$randm14=\"\";$randm15=\"as\";$randm16=\"$randm17\";$randm18=\"$randm19\";$randm20=\"o\";$randm21=\"6\";$randm22=\"$randm23\";$randm24=\" -d\";$randm25=\"$randm26\";$randm27=\"\";$randm28=\"b\";$randm29=\"e\";$randm30=\"v |\";Tx="Eds";$randm31=\"\""
    de=''"$randm32"'=$(eval '"\"\$$randm14\$$randm29\$$randm5\$$randm7\$$randm20\$$randm11\$$randm29\$$randm30\$$randm14\$$randm28\$$randm31\$$randm15\$$randm29\$$randm21\$$randm7\$$randm6\$$randm24\$$randm31\""')'
    zc='eval '"\"\$$randm27\$$randm32\$$randm14\$$randm7\""''
    rm -f $Out"-febry.sh" #Delete Provious File
    printf "#!/bin/bash\n#Obfuscated By xNot_Found\n#Github : https://github.com/hatakecnk/BashProtector\n" >> $Out"-febry.sh"
    printf "$nasa;$de;$zc" >> $Out"-febry.sh"
    printf "\e[34;1m[${NC}+\e[34;1m]${NC} Obfuscated...\n"
    printf "${ijo}[${NC}+${ijo}]${NC} Output : $Out-febry.sh\n"
}

clear
banner
febry
obf
