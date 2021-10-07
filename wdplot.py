import platformdirs

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

df = pd.read_excel('wahana.xlsx')
df1 = df.copy()
df1 = df.astype(str)

df1['content'] = df1['content'].replace({'"': '',
                             '\d+': '',
                             ':': '',
                             ';': '',
                             '#': '',
                             '@': '',
                             '_': '',
                             ',': '',
                             "'": '',
                             }, regex=True)
df1['content'] = df1['content'].str.replace(r'["\n"]+[https]+[?://]+[^\s<>"]+|www\.[^\s<>"]+[@?()]+[(??)]+[)*]+[(\xa0]+[-&gt...]', "",regex=True)
df1['content'] = df1['content'].str.replace('\n','',regex=True)
df1['content'] = df1['content'].str.replace('https//','',regex=True)
df1['content'] = df1['content'].str.replace('.','',regex=True)
df1['content'] = df1['content'].str.lstrip()
df1['content'] = df1['content'].replace({'WTS':'','PT':'','RT':'','xa0PT':''},regex=True)
df1['content'] = df1['content'].replace({'/':''},regex =True)

stopword = stopwords.words("indonesian")
allwords = ''.join([twts for twts in df1['content']])
wordCloud = WordCloud(width=1000,height=800,random_state=100,max_font_size=150,background_color='white',max_words=150,stopwords=stopword,colormap='Paired').generate(allwords)
plt.imshow(wordCloud,interpolation='bilinear')
plt.axis('off')
plt.show()

