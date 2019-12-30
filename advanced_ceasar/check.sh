sleep_time=1

echo "Скачиваю входной текст"
curl "http://gutenberg.net.au/ebooks01/0100011.txt" > input_file
sleep $sleep_time

echo "Генерирую ключ..."
python3 caesar.py --mode genkey
sleep $sleep_time

echo "Шифрую текст..."
python3 caesar.py --mode encrypt --key key_file --output cipher_text --input input_file
sleep $sleep_time

echo "Расшифровываю получившийся шифртекст, с тем же ключем"
python3 caesar.py --mode decrypt --key key_file --input cipher_text --output decipher
sleep $sleep_time

if cmp decipher input_file; then
    echo "Расшифровка отработала верно";
else
    echo "Шифртекст и расшифрованный текст не совпадают";
fi

echo "Скачиваю большой текстовый пул"
curl "http://gutenberg.net.au/ebooks01/0100021.txt" > pool_file
sleep $sleep_time

echo "Взламываю шифртекст с использованием скачанного пула"
python3 caesar.py --mode break --input cipher_text --pool pool_file --output new_key
sleep $sleep_time


num_diff=$( cmp -l key_file new_key | wc -l )
echo "Количество несовпавших символов в ключах: $num_diff из 256"

rm key_file decipher cipher_text input_file pool_file new_key
