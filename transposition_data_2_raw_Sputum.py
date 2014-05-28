#!/usr/local/bin/python

path = "C:/Users/Kai/Desktop"

# Sputum
in_file = open(path + "/Raw_data/Sputum/UBIO lipidomics sputum B1_B2 QC_fail.txt", "r")
out_file = open(path + "/Outputs/Sputum_raw_kai.txt", "w")

first_line = in_file.readline().replace("\n", "")
feature_IDs = first_line.split("\t")[4:len(first_line.split("\t"))]

kit_IDs = []
array_data = []
for line in in_file:
	new_line = line.replace("\n", "")
	kit_id = new_line.split("\t")[2]
	data = new_line.split("\t")[4:len(new_line.split("\t"))]
	kit_IDs.append(kit_id)
	array_data.append(data)
in_file.close()

outline = "feature_ID"
for i in range(len(kit_IDs)):
	outline += "\t" + kit_IDs[i]
outline += "\n"
out_file.write(outline)
	
for i in range(len(feature_IDs)):
	outline = feature_IDs[i]
	for j in range(len(kit_IDs)):
		outline += "\t" + array_data[j][i]
	outline += "\n"
	out_file.write(outline)
	
out_file.close()