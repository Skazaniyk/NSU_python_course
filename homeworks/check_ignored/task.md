## 1. Check ignored
Напишите программу, которой на вход аргументами командной строки передаются путь некоторого репозитория, 
который содержит файл `.gitignore`. 

Считаем, что в `.gitignore` могут находиться только следующие конструкции:

* Конкретные пути до файлов: `path/to/some/file.bin`
* Регулярные выражения, начинающиеся со \* : `*.txt`, `*trash.csv`

### Пример: 

Для такой файловой структуры:

    some_project
       ├── first_folder
       │   ├── first_subfolder
       │   │   ├── file1.dbf
       │   │   ├── file2.shp
       │   │   ├── file3.shx
       │   │   └── file4.pickle
       │   └── file5.csv
       ├── second_folder
       │   ├── sedond_subfolder
       │   │   ├── file1.dbf
       │   │   ├── file10.py
       │   │   ├── not_file.bin
       │   │   └── another_file.txt
       │   └── yet_another_file.yml
       └── .gitignore 
       ├── coverage.html
       ├── run_script.py

И такого содержания файла `.gitignore`:

```
first_folder/first_subfolder/file2.shp
coverage.html
*.dbf
second_folder/useless.py
```

После запуска скрипта из консоли:

``python3 check_ignored.py --project_dir=/path/to/some_project``

Вывод должен быть:

```
Ignored files:
some_project/first_folder/first_subfolder/file2.shp ignored by expression first_folder/first_subfolder/file2.shp
coverage.html ignored by expression coverage.html
some_project/first_folder/first_subfolder/file1.dbf ignored by expression *.dbf
some_project/second_folder/second_subfolder/file1.dbf ignored by expression *.dbf

```
