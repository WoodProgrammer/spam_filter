import csv
label_stat=[]
def get_spam_stat(mail_name):
    with open('spam_label.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["name"]==mail_name:
                print row["stat"]



for i in range(1,4326):
    stat=get_spam_stat("TR_{0}.eml".format(i))
