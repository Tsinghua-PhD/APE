# -*- coding: utf-8 -*-

from const import *
from variable import *

def get_type_father():

	file_name = "/Ontology/dbpedia_2016-10.nt"
	with open(path+file_name, 'r') as rf:
		for line in rf:
			tmp = line.rstrip(" .\n").strip().split(" ", 2)
			if tmp[0].startswith(ontology_prefix) and tmp[1] == subclassof_relation:
				if tmp[2].startswith(ontology_prefix):
					name1 = tmp[0].replace(ontology_prefix, '').rstrip(">")
					name2 = tmp[2].replace(ontology_prefix, '').rstrip(">")
					if not name1 in type_father:
						type_father[name1] = name2
				elif tmp[2] == owl_thing:
					name = tmp[0].replace(ontology_prefix, '').rstrip(">")
					if not name in type_father:
						type_father[name] = "Thing"
				else:
					pass

	# write type_father dict into a file
	with open("type-father.dat", 'w') as wf:
		for key in type_father:
			wf.writelines("%s\t\t%s\n"%(key, type_father[key]))

	return

# get path for each type, total 760 types
def get_type_path():
	for key in type_father:
		type_path[key] = []
		cur_type = key
		while cur_type in type_father:
			type_path[key].append(cur_type)
			cur_type = type_father[cur_type]
		type_path[key].reverse()

	with open("type-path.dat", 'w') as wf:
		for key in type_path:
			path_str = key + split_str + type_path[key][0]
			for i in range(1,len(type_path[key])):
				path_str += (split_multi + type_path[key][i])
			wf.writelines("%s\n"%path_str)

	return

# get summary information about type-hierarchy
def get_taxonomy_info():
	get_type_father()
	get_type_path()
	print("type num:", len(type_father))
	type_depth = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
	for key in type_path:
		length = len(type_path[key])
		type_depth[length] += 1
	count = 0

	for key in sorted(type_depth.keys()):
		count += type_depth[key]
		print ("type-path length = %d : %d"%(key, type_depth[key]))
		print ("type-path length <=%d : %d"%(key, count))
	return

