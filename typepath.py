# -*- coding -*-

from const import *
from variable import *

def get_instance_typepath():
	file_name = "/Type/instance_types_en.ttl"
	with open(path+file_name, 'r') as rf:
		for line in rf:
			tmp = line.rstrip(" .\n").strip().split(" ", 2)
			if tmp[0].startswith(instance_prefix) and tmp[1] == type_relation and tmp[2].startswith(ontology_prefix):
				instance_name =  tmp[0].replace(instance_prefix, '').replace('>', '')
				type_name = tmp[2].replace(ontology_prefix, '').replace('>', '')
				if not instance_name in instance_type:
					instance_type[instance_name] = type_path[type_name]
				else:
					if len(type_path[type_name]) > len(instance_type[instance_name]):
						instance_type[instance_name] = type_path[type_name]


	count = 0
	file_name = "instance-typepath.dat"
	with open(file_name, 'w') as wf:
		for key in instance_type:
			count += len(instance_type[key])
			path_str = key + split_str + instance_type[key][0]
			for i in range(1,len(instance_type[key])):
				path_str += (split_multi + instance_type[key][i])
			wf.writelines("%s\n"%path_str)

	print ("instance with type-path:", len(instance_type))
	print ("avg path length:", float(count)/len(instance_type))
