# Список русских слов JSON 

### `dict.json`
Json-файл со списком русских слов во всех морфологических формах.  
Содержит **1 601 915** записей.  

### `dict_translite.json`
Это dict.json только слова в транслите.
Использована [эта](https://github.com/opendatakosovo/cyrillic-transliteration) библиотека. Вырезаны "#" и апостроф.

## Файлы симметричны

    print(dictionary[1000])
    #>> шалопайничества

    print(dict_translite[1000])
    #>> shalopajnichestva
    
    #Полный пример есть в example.py


## Powered by

https://github.com/danakt/russian-words

https://github.com/opendatakosovo/cyrillic-transliteration