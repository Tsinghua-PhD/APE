# -*- coding: utf-8 -*-
from const import *
from variable import *
import codecs

count_dict ={}

def sort_dict(dict_words):
	keys = dict_words.keys()
	values = dict_words.values()

	list_one = [(key, val) for key, val in zip(keys, values)]
	list_sort = sorted(list_one, key=lambda x: x[1], reverse=True)

	return list_sort


with codecs.open(path+"/Type/instance_types_en.ttl", 'r', 'utf-8') as rf:
	for line in rf:
		tmp = line.rstrip(" .\n").strip().split(" ", 2)
		if tmp[1] == type_relation:
			type_str = tmp[2].replace(ontology_prefix, '').replace('>', '')
			if not type_str in count_dict:
				count_dict[type_str] = 0
			count_dict[type_str]+=1


sorted_list = sort_dict(count_dict)

with codecs.open("concept_stat.txt", 'w', 'utf-8') as wf:
	for item in sorted_list:
		wf.writelines("%s\t\t%d\n"%(item[0],item[1]))


