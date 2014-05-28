#!/usr/local/bin/python

path = "C:/Users/Kai/Desktop"

# Biopsy
#in_file = open(path + "/Raw_data/Biopsy/UBIOPRED.Biopsy.PassQC.RMA2.txt", "r")
#out_file = open(path + "/Outputs/Biopsy_raw_kai.txt", "w")

# Blood
#in_file = open(path + "/Raw_data/Blood/expression.txt", "r")
#out_file = open(path + "/Outputs/Blood_raw_kai.txt", "w")

# BrBrush
in_file = open(path + "/Raw_data/BrBrush/mloza.P101327.RMA.PostQC_ES_18-Oct-2013.txt", "r")
out_file = open(path + "/Outputs/BrBrush_raw_kai.txt", "w")

first_line = in_file.readline()
out_file.write(first_line)

for line in in_file:
	entries = line.replace("\n", "").split("\t")
	outline = entries[0]
	for i in range(1, len(entries)):
		data = float(entries[i])
		converted_data = 2**data
		outline += "\t" + str(converted_data)
	outline += "\n"
	out_file.write(outline)	

in_file.close()
out_file.close()