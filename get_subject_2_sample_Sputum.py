#!/usr/local/bin/python

path = "C:/Users/Kai/Desktop"

out_file_note = open(path + "/Outputs/Sputum_note.txt", "w")

subjects_for_uploading = []
in_file_subjects_for_uploading = open(path + "/Raw_data/subjects_for_uploading.txt", "r")

# get subjects for uploading
first_line = in_file_subjects_for_uploading.readline()
for line in in_file_subjects_for_uploading:
	subject = line.replace("\n", "")
	subjects_for_uploading.append(subject)
in_file_subjects_for_uploading.close()

print "Size of subjects for uploading: %d" %len(subjects_for_uploading)

# get sample to subject mappings (adults)
sample2subject_mapping = {}
in_mapping_file1 = open(path + "/Raw_data/adult_key_mapping_SK.txt", "r")
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
		
in_mapping_file2 = open(path + "/Raw_data/paed_key_mapping_SK.txt", "r")
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

# generate output file
in_file = open(path + "/Raw_data/Sputum/UBIO lipidomics sputum B1_B2 QC_fail.txt", "r")
out_file = open(path + "/Outputs/Sputum_sub2sample_kai.txt", "w")

first_line = in_file.readline()

outline = "study_id" + "\t" + "site_id" + "\t" + "subject_id" + "\t" + "SAMPLE_ID" + "\t" + "PLATFORM" + "\t" + "TISSUETYPE" + "\t" + "ATTR1" + "\t" + "ATTR2" + "\t" + "category_cd" + "\n"
out_file.write(outline)

for line in in_file:
	sample_id = line.split("\t")[2]
	
	if sample_id in sample2subject_mapping:
		subject_id = sample2subject_mapping[sample_id]
			
		if subject_id in subjects_for_uploading:		
			outline = "May2014_UBIO" + "\t" + "\t" + subject_id + "\t" + sample_id + "\t" + "GPL570" + "\t" + "Sputum" + "\t" + "Lipidomics" + "\t" + "\t" + "OMICS_DATA+ATTR1+Baseline_Visit+TISSUETYPE+PLATFORM" + "\n"
			out_file.write(outline)

		else:
			note_line = subject_id + " is not in subjects for uploading..." + "\n"
			print note_line.replace("\n", "")
			out_file_note.write(note_line)
	else:
		note_line = sample_id + " is not mapping to available subjects..." + "\n"
		print note_line.replace("\n", "")
		out_file_note.write(note_line)

in_file.close()
out_file.close()
out_file_note.close()


