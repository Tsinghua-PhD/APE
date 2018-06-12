# -*- coding -*-

from const import *
from variable import *
from sklearn.feature_extraction.text import TfidfVectorizer

def get_tfidf_feature():
	file_name = "/Abstract/long_abstracts_en.ttl"
	with open(path+file_name, 'r') as rf:
		for line in rf:
			tmp = line.rstrip(" .\n").strip().split(" ", 2)
			if tmp[0].startswith(instance_prefix) and tmp[1] == abstract_relation:
				abstract_str = tmp[2].lstrip('"').rstrip('"@en').strip()
				instance_name = tmp[0].replace(instance_prefix, '').replace(">", '')
				corpus.append(abstract_str)
				instance_list.append(instance_name)

	vectorizer = TfidfVectorizer()
	tfidf = vectorizer.fit_transform(corpus).toarray()

	for i in range(len(instance_list)):
		instance_text[instance_list[i]] = tfidf[i]

	with open("instance-text.dat", 'w') as wf:
		for key in instance_text:
			wf.writelines("%s\t\t%s\n"%(key,instance_text[key]))