echo -ne "Waiting for database to boot up...\n"
echo -ne "-----------------------------------\n\n"
until nc -z -v -w30 db 3306
do
  echo "MYSQL not running yet"
  sleep 5
done

sleep 20

echo -ne "Upgrading database...\n"
echo -ne "-----------------------------------\n\n"
make upgrade

echo -ne "Running app...\n"
echo -ne "-----------------------------------\n\n"
make run