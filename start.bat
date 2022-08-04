@echo off
echo "INICIANDO..."

timeout 3 
cmd.exe /c "cls"
echo "[!] Checkeando cuenta..."
cmd.exe /c "python Spotify-checker-bs4-selenium.py"

timeout 6

echo "[+] Cerrando Checker"
taskkill /IM Spotify-checker-bs4-selenium.py

exit

