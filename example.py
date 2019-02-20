import json

def OpenJson():
    with open('dict.json', 'r') as f:
            dictionary = json.load(f)
    return dictionary

def OpenJson_translite():
    with open('dict_translite.json', 'r') as f:
            dict_translite = json.load(f)
    return dict_translite

def main():
    dictionary = OpenJson()
    dict_translite = OpenJson_translite()

    print(dictionary[1000])
    #>> шалопайничества

    print(dict_translite[1000])
    #>> shalopajnichestva

if __name__ == '__main__':
    main()