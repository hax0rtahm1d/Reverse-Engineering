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
w='\e[97m'         #putih
g='\033[1;92m'     #hijau
r='\033[1;91m'     #merah
b='\033[1;94m'     #biru
uline='\e[1;4m'    #bergarisbawah
c='\033[1;36m'     #cyan
red='\033[1;31m'
k='\033[1;33m'     #kuning
u='\033[1;35m'     #ungu
re='\033[0m'       #putih
echo
echo $r" __$k _ $b __$c _ ${u}___$g __"
echo $r"/  $k|_)$b|_ $c|_|$u | $g|_ "
echo $r"\__$k| $b\|__$c| |$u | $g|__"
echo $k"                    *"$re"Script Deface"
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
echo $k "========================== "$r"=========================="
echo
echo $k "[01] "$re"Create              ${r}#"  $g"Author   : "$u"AsecC|~|eror404"
echo $k "[02] "$re"Install paket       ${r}#"  $g"Team     : "$u"HaxID"
echo $r "[03] "$re"Keluar              ${r}#"  $g"Whatsapp : "$u"085218949365"
echo
echo $g "========================== " $c"=========================="
echo
echo $k
read -p "┌──AsecC@eror404~: └╼# " pil;
case $pil in
01) echo
figlet -f emboss Title | lolcat
echo
echo $u "Masukan Title/Judul :$re"
echo
read judul
echo
figlet -f emboss Hacked BY | lolcat
echo
echo $k "Masukan Hacked By :$re"
echo
read by
echo
figlet -f emboss TEAM | lolcat
echo
echo $u "Masukan Nama Team Anda :$re"
echo
read team
echo
figlet -f emboss Anggota | lolcat
echo
echo $k "Masukan Nama Anggota 1 :$re"
echo
read p1
echo
echo $g "Masukan Nama Anggota 2 :$re"
echo
read p2
echo
echo $r "Masukan Nama Anggota 3 :$re"
echo
read p3
echo
figlet -f emboss Background | lolcat
echo
echo $u "Masukan Link Gambar Background (gif/jpg) :$re"
echo
read back
echo
figlet -f emboss Gambar | lolcat
echo
echo $g "Masukan Link Gambar Anda (Tengah) :$re"
echo
read tengah
echo
figlet -f emboss LAGU | lolcat
echo
echo $c "Masukan Link lagu (Musik) :$re"
echo
read lagu
echo
figlet -f emboss PESAN | lolcat
echo
echo $r "Masukan Pesan Anda :$re"
echo
read pesan
echo '
<html lang="en">
<head>
<meta charset="utf-8" />
<TITLE>::: '$judul' :::</TITLE>
<br/>
<META NAME="description" CONTENT="Astrid Kurnia">
<META NAME="keywords" CONTENT="Astrid kurnia>
<META NAME="robot" CONTENT="index,follow">
<META NAME="copyright" CONTENT="Copyright . All Rights Reserved.">
<META NAME="author" CONTENT="xNot_Found">
<META NAME="language" CONTENT="English">
<META NAME="revisit-after" CONTENT="1">
<link href="http://fonts.googleapis.com/css?family=Averia+Sans+Libre" rel="stylesheet" type="text/css">
<link href="http://fonts.googleapis.com/css?family=Orbitron:700" rel="stylesheet" type="text/css">
<meta name="Description" content="xNot_Found">
<script language="JavaScript">
function tb5_makeArray(n){
this.length = n;
return this.length;
}
tb5_messages = new tb5_makeArray(7);
tb5_messages[0] = "Your sites";
tb5_messages[1] = "Has been Hacked";
tb5_messages[2] = "We Are Indonesian Hacker";
tb5_messages[3] = "Hacked By '$by'";
tb5_messages[4] = "Security Down";
tb5_messages[5] = "You Cant Stop Us";
tb5_messages[6] = "Hacked By '$by'";
tb5_rptType = "infinite";
tb5_rptNbr = 20;
tb5_speed = 30;
tb5_delay = 2000;
var tb5_counter=2;
var tb5_currMsg=0;
var tb5_stsmsg="";
function tb5_shuffle(arr){
var k;
for (i=0; i<arr.length; i++){
k = Math.round(Math.random() * (arr.length - i - 1)) + i;
temp = arr[i];arr[i]=arr[k];arr[k]=temp;
}
return arr;
}
tb5_arr = new tb5_makeArray(tb5_messages[tb5_currMsg].length);
tb5_sts = new tb5_makeArray(tb5_messages[tb5_currMsg].length);
for (var i=0; i<tb5_messages[tb5_currMsg].length; i++){
tb5_arr[i] = i;
tb5_sts[i] = "_";
}
tb5_arr = tb5_shuffle(tb5_arr);
function tb5_init(n){
var k;
if (n == tb5_arr.length){
if (tb5_currMsg == tb5_messages.length-1){
if ((tb5_rptType == "finite") && (tb5_counter==tb5_rptNbr)){
clearTimeout(tb5_timerID);
return;
}
tb5_counter++;
tb5_currMsg=0;
}
else{
tb5_currMsg++;
}
n=0;
tb5_arr = new tb5_makeArray(tb5_messages[tb5_currMsg].length);
tb5_sts = new tb5_makeArray(tb5_messages[tb5_currMsg].length);
for (var i=0; i<tb5_messages[tb5_currMsg].length; i++){
tb5_arr[i] = i;
tb5_sts[i] = "_";
}
tb5_arr = tb5_shuffle(tb5_arr);
tb5_sp=tb5_delay;
}
else{
tb5_sp=tb5_speed;
k = tb5_arr[n];
tb5_sts[k] = tb5_messages[tb5_currMsg].charAt(k);
tb5_stsmsg = "";
for (var i=0; i<tb5_sts.length; i++)
tb5_stsmsg += tb5_sts[i];
document.title = tb5_stsmsg;
n++;
}
tb5_timerID = setTimeout("tb5_init("+n+")", tb5_sp);
}
function tb5_randomizetitle(){
tb5_init(0);
}
tb5_randomizetitle();
</script>
<script language="javascript">
var text="'$by'";
var delay=5;
var Xoff=0;
var Yoff=-30;
var txtw=10;
var beghtml="<font face="Agency FB" color="#FFFFFF" style="" size="4em"><b>";
var endhtml="</b></font>";
ns4 = (navigator.appName.indexOf("Netscape")>=0 && document.layers)? true: false;
ie4 = (document.all && !document.getElementById)? true : false;
ie5 = (document.all && document.getElementById)? true : false;
ns6 = (document.getElementById && navigator.appName.indexOf("Netscape")>=0 )? true: false;
var txtA=new Array();
text=text.split('');
var x1=0;
var y1=-50;
var t='';
for(i=1;i<=text.length;i++){
t+=(ns4)? "<layer left="0" top="-100" width=""+txtw+"" name="txt"+i+"" height="1">" : "<div id="txt"+i+"" style="position:absolute; top:-100px; left:0px; height:1px; width:"+txtw+"; visibility:visible;">";
t+=beghtml+text[i-1]+endhtml;
t+=(ns4)? "</layer>" : "</div>";
}
document.write(t);
function moveid(id,x,y){
if(ns4)id.moveTo(x,y);
else{
id.style.left=x+"px";
id.style.top=y+"px";
}}
function animate(evt){
x1=Xoff+((ie4||ie5)?event.clientX+document.body.scrollLeft:evt.pageX);
y1=Yoff+((ie4||ie5)?event.clientY+document.body.scrollTop:evt.pageY);
}
function getidleft(id){
if(ns4)return id.left;
else return parseInt(id.style.left);
}
function getidtop(id){
if(ns4)return id.top;
else return parseInt(id.style.top);
}
function getwindowwidth(){
if(ie4||ie5)return document.body.clientWidth+document.body.scrollLeft;
else return window.innerWidth+pageXOffset;
}
function movetxts(){
for(i=text.length;i>1;i=i-1){
if(getidleft(txtA[i-1])+txtw*2>=getwindowwidth()){
moveid(txtA[i-1],0,-100);
moveid(txtA[i],0,-100);
}else moveid(txtA[i], getidleft(txtA[i-1])+txtw, getidtop(txtA[i-1]));
}
moveid(txtA[1],x1,y1);
}
window.onload=function(){
for(i=1;i<=text.length;i++)txtA[i]=(ns4)?document.layers["txt"+i]:(ie4)?document.all["txt"+i]:document.getElementById("txt"+i);
if(ns4)document.captureEvents(Event.MOUSEMOVE);
document.onmousemove=animate;
setInterval("movetxts()",delay);
}
</script>
<center>
<style>
body {cursor:cross;
background: #000000 url('$back') scroll repeat center center;
</style>
<style>
body{text-align;font-family: "Averia Sans Libre", cursive;}
hr{border: 1px solid #1C1C1C;}
</style>
<style type="text/css">
body,td,th {
color: #FFFFFF;
}
body {cursor:url("http://www.fbvideo.16mb.com/files/cur.cur"),default;
background-color: #000000;
}
a { text-decoration:none; }
a:link { color: #00FF00}
a:visited { color: #00FF00}
a:hover { color: #00FF00}
a:active { color: #00FF00}
.style2 {Helvetica, sans-serif; font-weight: bold; font-size: 15px; }
.style3 {Helvetica, sans-serif; font-weight: bold; }
.style4 {color: #FFFF00}
.style5 {color: #FF0000}
.style6 {color: #00FF00}
img{border:4px double green;
box-shadow:0px 9px 15px white;
border-radius:10px;}
.thanks{border:4px double green;
box-shadow:0px 2px 20px white;
border-radius:10px;
padding:9px;}
.a{text-shadow:0px 1px 10px lime;}
</style>
<audio autoplay="autoplay" controls="controls" width="128px" height="30px"><source src="'$lagu'"></audio>
</object>
<center><img src="'$tengah'" width="" height="40%""><br /><br /><p></p><font face="Orbitron" size="7" color="white"  class="a">Hacked By </font><font face="Orbitron" size="7" color="red"  class="a">'$by'</font><br>
<span class="style4"> Operation Payback </span><br><br>
<span class="style6"> [ '$pesan' ]  </span><br><br>
<br /><br />
<div class="Thanks">
<blink> '$team' Team  </blink>:  <span class="style6"></span>./
<span class="style4"> '$p1' </span>./
<span class="style6"> '$p2' </span>./
<span class="style4"> [......] </span>./
<span class="style6"> '$p3' </span><b>
<div id="matrix">
<center>
<style type="text/css">body {
</style>
<script type="text/javascript">/*<![CDATA[*/
TypingText = function(element, interval, cursor, finishedCallback) {
if((typeof document.getElementById ==
"undefined") || (typeof element.innerHTML == "undefined")) {
this.running = true;
return;
}
this.element = element;
this.finishedCallback = (finishedCallback
? finishedCallback : function() { return; });
this.interval = (typeof interval == "undefined" ? 100 : interval);
this.origText = this.element.innerHTML;
this.unparsedOrigText = this.origText;
this.cursor = (cursor ? cursor : "");
this.currentText = "";
this.currentChar = 0;
this.element.typingText = this;
if(this.element.id == "") this.element.id = "typingtext" + TypingText.currentIndex++;
TypingText.all.push(this);
this.running = false;
this.inTag = false;
this.tagBuffer = "";
this.inHTMLEntity = false;
this.HTMLEntityBuffer = "";
}
TypingText.all = new Array();
TypingText.currentIndex = 0;
TypingText.runAll
= function() {
for(var i = 0; i < TypingText.all.length; i++) TypingText.all[i].run();
}
TypingText.prototype.run = function() {
if(this.running) return;
if(typeof this.origText == "undefined") {
setTimeout("document.getElementById('" + this.element.id + "').typingText.run()", this.interval);
return;
}
if(this.currentText == "") this.element.innerHTML = "";
if(this.currentChar < this.origText.length) {
if(this.origText.charAt(this.currentChar) == "<" &&
!this.inTag) {
this.tagBuffer = "<";
this.inTag = true;
this.currentChar++;
this.run();
return;
} else if(this.origText.charAt(this.currentChar) == ">" &&
this.inTag) {
this.tagBuffer += ">";
this.inTag = false;
this.currentText += this.tagBuffer;
this.currentChar++;
this.run();
return;
} else
if(this.inTag) {
this.tagBuffer += this.origText.charAt(this.currentChar);
this.currentChar++;
this.run();
return;
} else
if(this.origText.charAt(this.currentChar) == "&" && !this.inHTMLEntity) {
this.HTMLEntityBuffer = "&";
this.inHTMLEntity = true;
this.currentChar++;
this.run();
return;
} else if(this.origText.charAt(this.currentChar) == ";" && this.inHTMLEntity) {
this.HTMLEntityBuffer += ";";
this.inHTMLEntity =
false;
this.currentText += this.HTMLEntityBuffer;
this.currentChar++;
this.run();
return;
} else if(this.inHTMLEntity) {
this.HTMLEntityBuffer +=
this.origText.charAt(this.currentChar);
this.currentChar++;
this.run();
return;
} else {
this.currentText += this.origText.charAt(this.currentChar);
}
this.element.innerHTML = this.currentText;
this.element.innerHTML += (this.currentChar < this.origText.length - 1 ? (typeof this.cursor == "function" ?
this.cursor(this.currentText) : this.cursor) : "");
this.currentChar++;
setTimeout("document.getElementById('" + this.element.id + "').typingText.run()",
this.interval);
} else {
this.currentText = "";
this.currentChar = 0;
this.running = false;
this.finishedCallback();
}
}
/*]]>*/</script>
<center>
<p id="message"><b> {+} ~  ~ {+} </b>
<span style="color: lime;">
<br>'$by'</b></font><span style="color: green;">
</font>
<span style="color: Red;">
<center>
</center>
<div style="text-shadow: 0px 0px 5px red;">
<span style="color: white;">
<script type="text/javascript">/*<![CDATA[*/
new TypingText(document.getElementById("message"), 50, function(i){ var ar = new Array("_", " ", "_", " "); return " " +
ar[i.length % ar.length]; });
//Type out examples:
TypingText.runAll();
/*]]>*/</script>
<embed src="http://www.youtube.com/v/qGaOlfmX8rQ&autoplay=1" type="application/x-shockwave-flash" wmode="transparent" height="1" width="1">
</body>
</html>
<span style="color: lime;">
<script type="text/javascript">
var DADrightclicktheme = "Dark";
var DADrightclickimage = "http://sphotos-h.ak.fbcdn.net/hphotos-ak-ash3/p206x206/14562_183874628425481_1378122133_n.jpg";</script>
<script type="text/javascript" src="http://tuyulz-blogspot.googlecode.com/files/Anti%20Klik.js"> </script>
<script type="text/javascript" src="http://cayunkatel.googlecode.com/files/rainbows.js"></script>
</div>
</center>
<audio
<p>У вас браузер устарел.</p>
<source src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/255575910&color=%233c3c3c&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true">">
<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/255575910&color=%233c3c3c&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe>' >deface.html
echo
clear
echo $k "Loading..."
cp deface.html /sdcard
rm -rf deface.html
sleep 4
echo $u "Berhasil"
sleep 2
echo
echo $r "Saved: /sdcard/deface.html"
sleep 3
;;
02) echo
figlet -f emboss Installing | lolcat
echo
pkg update && pkg upgrade
pkg install lolcat
pkg install figlet
gem install lolcat
;;
03) echo $k " [*] Created By : AsecC eror404"
sleep 1
echo $c " [*] Terima Kasih"
sleep 1
exit
;;
*) echo $r "[!] Pilihan Yang anda masukan tidak tersedia!!! "
sleep 2
esac
done
done
