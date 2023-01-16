#demande l'ip
read -p "Enter the server IP address: " server_ip

#scan de tout les port
for port in {1..65535}
do
    (echo >/dev/tcp/$server_ip/$port) &>/dev/null && echo "Port $port is open"
done