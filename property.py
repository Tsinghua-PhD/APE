# -*- coding: utf-8 -*-
from const import *
from variable import *

def get_property_list():
	# object property
	filename = "/Property/mapping/mappingbased_objects_en.ttl"
	with open(path+filename, 'r') as rf:
		for line in rf:
			tmp = line.rstrip(" .\n").strip().split(" ", 2)
			if len(tmp) == 3 and tmp[0].startswith(instance_prefix):
				if tmp[1].startswith(ontology_prefix):
					if not tmp[1] in object_property_dict:
						object_property_dict[tmp[1]] = 0
					object_property_dict[tmp[1]] += 1
				else:
					if not tmp[1] in other_property_dict:
						other_property_dict[tmp[1]] = 0
					other_property_dict[tmp[1]] += 1

	# datatype property
	filename = "/Property/mapping/mappingbased_literals_en.ttl"
	with open(path+filename, 'r') as rf:
		for line in rf:
			tmp = line.rstrip(" .\n").strip().split(" ", 2)
			if len(tmp) == 3 and tmp[0].startswith(instance_prefix):
				if tmp[1].startswith(ontology_prefix):
					if not tmp[1] in datatype_property_dict:
						datatype_property_dict[tmp[1]] = 0
					datatype_property_dict[tmp[1]] += 1
				else:
					if not tmp[1] in other_property_dict:
						other_property_dict[tmp[1]] = 0
					other_property_dict[tmp[1]] += 1

	# print some information
	print ("object property:", len(object_property_dict.keys()))
	print ("datatype property:", len(datatype_property_dict.keys()))
	print ("other property:", len(other_property_dict.keys()))

	# get property list (object, datatype and others)
	new_dict = sorted(object_property_dict.items(), key=lambda d:d[1], reverse = True)
	with open("property-object-list.txt", 'w') as wf:
		for item in new_dict:
			wf.writelines("%s\t\t%d\n"%(item[0], item[1]))
	del new_dict

	new_dict = sorted(datatype_property_dict.items(), key=lambda d:d[1], reverse = True)
	with open("property-datatype-list.txt", 'w') as wf:
		for item in new_dict:
			wf.writelines("%s\t\t%d\n"%(item[0], item[1]))
	del new_dict

	new_dict = sorted(other_property_dict.items(), key=lambda d:d[1], reverse = True)
	with open("property-other-list.txt", 'w') as wf:
		for item in new_dict:
			wf.writelines("%s\t\t%d\n"%(item[0], item[1]))	
	del new_dict

	return