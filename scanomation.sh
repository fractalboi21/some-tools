ipaddress=$1

sudo nmap -V -O -A -T4 -p- -V --open --osscan-guess -sV $ipaddress >> result.txt

echo -n "[+] Open ports...\n"

cat result.txt | grep "open "

echo -n "[+] OS detection...\n"

cat result.txt | grep "OS details"