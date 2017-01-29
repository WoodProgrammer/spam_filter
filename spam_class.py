import re
file_name2="spam_data.csv"

import csv

def to_write_file(word_dict):
    f = open('spam_data.csv','a+')
    w = csv.DictWriter(f,word_dict.keys())
    w.writerow(word_dict)
    f.close()

def dict_creator_miner(file_url):
    default_word_dict={'free': 0, 'subscribe': 0, 'money': 0,'guaranteed':0,'girl':0}
    word_dict={'free': 0, 'subscribe': 0, 'money': 0,'guaranteed':0,'girl':0}
    with open(file_name) as f:
        content = f.readlines()

    for line in content:
        for key in word_dict:
            money_match=re.search( r"{0}".format(key), line, re.M|re.I)
            if money_match:
                word_dict[key]+=1
            else:
                continue

    to_write_file(word_dict)
    word_dict=default_word_dict


for i in range(1,4326):
    file_name="CSDMC2010_SPAM/CSDMC2010_SPAM/TRAINING/TR_{0}.eml".format(i)
    dict_creator_miner(file_name)
