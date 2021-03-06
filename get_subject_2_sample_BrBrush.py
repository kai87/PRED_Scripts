#!/usr/local/bin/python

path = "C:/Users/Kai/Desktop"

out_file_note = open(path + "/Outputs/BrBrush_note.txt", "w")

subjects_for_uploading = []
in_file_subjects_for_uploading = open(path + "/Raw_data/subjects_for_uploading.txt", "r")

# get subjects for uploading
first_line = in_file_subjects_for_uploading.readline()
for line in in_file_subjects_for_uploading:
	subject = line.replace("\n", "")
	subjects_for_uploading.append(subject)
in_file_subjects_for_uploading.close()

print "Size of subjects for uploading: %d" %len(subjects_for_uploading)

# read raw matrix file to get imagefilenames
in_raw_file = open(path + "/Raw_data/BrBrush/mloza.P101327.RMA.PostQC_ES_18-Oct-2013.txt", "r")
first_line =  in_raw_file.readline().replace("\n", "")
imagefilenames_in_raw = first_line.split("\t")[1:len(first_line.split("\t"))]
in_raw_file.close()

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
in_file = open(path + "/Raw_data/BrBrush/P101327.UBIOPRED_BrBrushings.CEL_file_listing.db_A_JAN2014.txt", "r")
out_file = open(path + "/Outputs/BrBrush_sub2sample_kai.txt", "w")

first_line = in_file.readline()

outline = "study_id" + "\t" + "site_id" + "\t" + "subject_id" + "\t" + "SAMPLE_ID" + "\t" + "PLATFORM" + "\t" + "TISSUETYPE" + "\t" + "ATTR1" + "\t" + "ATTR2" + "\t" + "category_cd" + "\n"
out_file.write(outline)

for line in in_file:
	imagefilename = line.split("\t")[0]
	if imagefilename in imagefilenames_in_raw:
		sample_id = line.split("\t")[5]
	
		if sample_id in sample2subject_mapping:
			subject_id = sample2subject_mapping[sample_id]
			original_subject_id = line.split("\t")[6]

			if subject_id in subjects_for_uploading:
				if subject_id != original_subject_id:
					print "subject_id(%s) != original_subject_id(%s)!" %(subject_id, original_subject_id)		
					
				outline = "May2014_UBIO" + "\t" + "\t" + subject_id + "\t" + imagefilename + "\t" + "GPL570" + "\t" + "Blood" + "\t" + "Transcriptomics" + "\t" + "\t" + "OMICS_DATA+ATTR1+Baseline_Visit+TISSUETYPE+PLATFORM" + "\n"
				out_file.write(outline)

			else:
				note_line = subject_id + " is not in subjects for uploading..." + "\n"
				print note_line.replace("\n", "")
				out_file_note.write(note_line)
		else:
			note_line = sample_id + " is not mapping to available subjects..." + "\n"
			print note_line.replace("\n", "")
			out_file_note.write(note_line)
	else:
		note_line = imagefilename + " is not in imagefilenames_in_raw..." + "\n"
		print note_line.replace("\n", "")
		out_file_note.write(note_line)

in_file.close()
out_file.close()
out_file_note.close()


