#!/usr/local/bin/python

path = "C:/Users/Kai/Desktop"

# Somalogic
in_file = open(path + "/Raw_data/Somalogic/JRD_14-001_CAL_20140114_data.txt", "r")
out_file = open(path + "/Outputs/Somalogic_raw_kai.txt", "w")

first_line = in_file.readline().replace("\n", "")
feature_IDs = first_line.split("\t")[1:len(first_line.split("\t"))]

sample_IDs = []
array_data = []
for line in in_file:
	new_line = line.replace("\n", "")
	sample_id = new_line.split("\t")[0]
	data = new_line.split("\t")[1:len(new_line.split("\t"))]
	sample_IDs.append(sample_id)
	array_data.append(data)
in_file.close()

outline = "feature_ID"
for i in range(len(sample_IDs)):
	outline += "\t" + sample_IDs[i]
outline += "\n"
out_file.write(outline)
	
for i in range(len(feature_IDs)):
	outline = feature_IDs[i]
	for j in range(len(sample_IDs)):
		outline += "\t" + array_data[j][i]
	outline += "\n"
	out_file.write(outline)
	
out_file.close()