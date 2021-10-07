import numpy as np
import pandas as pd
import google_play_scraper
from google_play_scraper import Sort, reviews_all

# =com.posindonesia.cob&hl=in&gl=US

print("memulai mining")
reviews = reviews_all(
    'id.tiki.tikiapp',
    sleep_milliseconds=0,
    lang='id',
    country='id',
    sort=Sort.NEWEST,
)


df = pd.DataFrame(np.array(reviews), columns=['review'])

df = df.join(pd.DataFrame(df.pop('review').tolist()))

print("selesai mining")



