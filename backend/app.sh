echo -ne "Waiting for database to boot up...\n"
echo -ne "-----------------------------------\n\n"
sleep 60

echo -ne "Upgrading database...\n"
echo -ne "-----------------------------------\n\n"
make upgrade

echo -ne "Running app...\n"
echo -ne "-----------------------------------\n\n"
make run