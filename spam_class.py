import re
import csv
import pandas as pd
def get_spam_stat(mail_name):
    spam_stat=0
    with open('spam_label.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["name"]==mail_name:
                spam_stat=row["stat"]
    return spam_stat


file_name2="spam_data.csv"
def to_write_file(word_dict):
    f = open('spam_data.csv','a+')
    w = csv.DictWriter(f,word_dict.keys())
    w.writerow(word_dict)
    f.close()

def dict_creator_miner(file_url,id,stat):

    default_word_dict={'stat':0,'id':0,'money': 0, 'guaranteed': 0, 'free': 0, 'subscribe': 0, 'girl': 0}
    word_dict={'stat':0,'id':0,'money': 0, 'guaranteed': 0, 'free': 0, 'subscribe': 0, 'girl': 0}
    with open(file_name) as f:
        content = f.readlines()

    for line in content:

        for key in word_dict:
            if key=="id":
                word_dict["id"]=id
            elif key=="stat":
                word_dict["stat"]=stat
            else:
                money_match=re.search( r"{0}".format(key), line, re.M|re.I)
                if money_match:
                    word_dict[key]+=1
                else:
                    pass


    to_write_file(word_dict)
    word_dict=default_word_dict

word_dict={'free': 0, 'subscribe': 0, 'money': 0,'guaranteed':0,'girl':0}
for i in range(1,1000):
    file_name="CSDMC2010_SPAM/CSDMC2010_SPAM/TRAINING/TR_{0}.eml".format(i)
    stat=get_spam_stat("TR_{0}.eml".format(i))
    dict_creator_miner(file_name,i,stat)
