#!/usr/local/bin/python

path = "C:/Users/Kai/Desktop"

# get sample to subject mappings (adults)
sample2subject_mapping = {}
in_mapping_file1 = open(path + "./Raw_data/adult_key_mapping_SK.txt", "r")
lines = in_mapping_file1.readline().split("\r")

for i in range(1, len(lines)):
	subject_id = lines[i].split("\t")[0]
	sample_id_1 = lines[i].split("\t")[1]
	sample_id_2 = lines[i].split("\t")[2]
	
	if sample_id_1 != "not available":
		sample2subject_mapping[sample_id_1] = subject_id
	if sample_id_2 != "not available":
		sample2subject_mapping[sample_id_2] = subject_id		
in_mapping_file1.close()
		
in_mapping_file2 = open(path + "./Raw_data/paed_key_mapping_SK.txt", "r")
lines = in_mapping_file2.readline().split("\r")

# get sample to subject mappings (children)
for i in range(1, len(lines)):
	subject_id = lines[i].split("\t")[0]
	sample_id_1 = lines[i].split("\t")[1]
	sample_id_2 = lines[i].split("\t")[2]
	
	if sample_id_1 != "not available":
		sample2subject_mapping[sample_id_1] = subject_id
	if sample_id_2 != "not available":
		sample2subject_mapping[sample_id_2] = subject_id	
in_mapping_file2.close()

# split array file
in_array_file = open(path + "/Outputs/GC-MS_raw_kai.txt", "r")
out_array_file_A = open(path + "/Outputs/adult_GC-MS_raw_kai.txt", "w")
out_array_file_P = open(path + "/Outputs/paed_GC-MS_raw_kai.txt", "w")

first_line =  in_array_file.readline().replace("\n", "")
kit_IDs_in_array = first_line.split("\t")[1:len(first_line.split("\t"))]

# 'n' for 'na', 'a' for 'adult', 'p' for 'paed'
check_list = ['n'] * len(kit_IDs_in_array)

for i in range(len(kit_IDs_in_array)):
	if kit_IDs_in_array[i] in sample2subject_mapping:
		subject = sample2subject_mapping[kit_IDs_in_array[i]]
		check_list[i] = subject[0]
	else:
		print "sample can not be mapped to subject: %s" %kit_IDs_in_array[i]

outline_A = first_line.split("\t")[0]
outline_P = first_line.split("\t")[0]

for i in range(len(check_list)):
	if check_list[i] == "A":
		outline_A += "\t" + kit_IDs_in_array[i]
	if check_list[i] == "P":
		outline_P += "\t" + kit_IDs_in_array[i]
outline_A += "\n"
outline_P += "\n"
out_array_file_A.write(outline_A)
out_array_file_P.write(outline_P)

for line in in_array_file:
	data_in_array = line.split("\t")[1:len(first_line.split("\t"))]
	outline_A = line.split("\t")[0]
	outline_P = line.split("\t")[0]

	for i in range(len(check_list)):
		if check_list[i] == "A":
			outline_A += "\t" + data_in_array[i]
		if check_list[i] == "P":
			outline_P += "\t" + data_in_array[i]
	outline_A += "\n"
	outline_P += "\n"
	out_array_file_A.write(outline_A)
	out_array_file_P.write(outline_P)
	
in_array_file.close()
out_array_file_A.close()
out_array_file_P.close()