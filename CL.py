# -*- coding: utf-8 -*-
from const import *
from variable import *

def get_cross_lingual_links():
	
	file = "/Language/interlanguage_links_en.ttl"
	with open(path+file, 'r') as rf:
		for line in rf:
			tmp = line.rstrip(" .\n").strip().split(" ", 2)
			if tmp[1] == sameAs:
				if tmp[0].startswith(category_prefix) and tmp[2].startswith(zh_category_prefix):
					CL_category_pairs[tmp[0].replace(category_prefix, '').replace('>', '')] = tmp[2].replace(zh_category_prefix, '').replace('>', '')
				elif tmp[0].startswith(template_prefix) and tmp[2].startswith(zh_template_prefix):
					CL_template_pairs[tmp[0].replace(template_prefix, '').replace('>', '')] = tmp[2].replace(zh_template_prefix, '').replace('>', '')
				elif tmp[0].startswith(instance_prefix) and tmp[2].startswith(zh_instance_prefix):
					CL_instance_pairs[tmp[0].replace(instance_prefix, '').replace('>', '')] = tmp[2].replace(zh_instance_prefix, '').replace('>', '')
				else:
					pass

	print ("cross-lingual instance links:", len(CL_instance_pairs))
	with open("CL-instance-links.dat", 'w') as wf:
		for key in CL_instance_pairs:
			wf.writelines("%s\t\t%s\n"%(key, CL_instance_pairs[key]))
	
	print ("cross-lingual category links:", len(CL_category_pairs))
	with open("CL-category-links.dat", 'w') as wf:
		for key in CL_category_pairs:
			wf.writelines("%s\t\t%s\n"%(key, CL_category_pairs[key]))
	
	print ("cross-lingual template links:", len(CL_template_pairs))
	with open("CL-template-links.dat", 'w') as wf:
		for key in CL_template_pairs:
			wf.writelines("%s\t\t%s\n"%(key, CL_template_pairs[key]))

	return