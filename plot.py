# -*- coding: utf-8 -*-
from collections import defaultdict
import sys
from os import path
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

# get path to script's directory
currdir = path.dirname(__file__)
clusters = defaultdict(list)

with open('result.csv') as f:
    for line in f:
        if len(line) > 0:
            id_cluster = int(line.split(',')[-1])
            clusters[id_cluster].append(",".join(line.split(',')[:-1]))

def create_wordcloud(name,text):
	# create numpy araay for wordcloud mask image
	mask = np.array(Image.open(path.join(currdir, "cloud.png")))

	# create set of stopwords
	stopwords = set(STOPWORDS)

	# create wordcloud object
	wc = WordCloud(background_color="white",
					max_words=300,
					mask=mask,
	               	stopwords=stopwords)

	# generate wordcloud
	wc.generate(text)

	# save wordcloud
	wc.to_file(path.join(currdir, "cluster{}.png".format(name)))


print(type(clusters.keys()[0]))
for key in clusters.keys():
    create_wordcloud(key,",".join(clusters[key]))
    with open("cluster_{}_news.list".format(key),"w") as w:
        for element in clusters[key]:
            w.write("{}\n".format(element))
