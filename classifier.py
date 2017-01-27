import sklearn
import pandas as pd
import re
mail_data_url="CSDMC2010_SPAM/CSDMC2010_SPAM/TRAINING/TRAIN_00000.eml"

data=0
with open(mail_data_url) as f:
    content = f.readlines()

for line in content :
    if (re.match("FREE",line)):
        print line    
