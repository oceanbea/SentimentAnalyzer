
import string
'''rating = int()
reviews = str()
text = open('file.txt',encode('utf-8', 'ignore').decode('utf-8')).read()
lowercasetext = text.lower()
print(lowercasetext)
print(string.punctuation) 
'''

import pandas as pd
data = pd.read_csv("Datasetutf8encoded.csv", dtype={'summary': str})
for index,row in data.iterrows():
    print(row.to_string().encode('utf-8').decode('utf-8'))
#print(data.iloc[9])