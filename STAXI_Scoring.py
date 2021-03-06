# This program will take raw scores from NEO-PI3 and write raw scores and t-scores in an excel file
import csv
import os
def get_accepted_value(prompt, scale, scale_score):
	incorrect_response = True
	while incorrect_response == True:
		while True:
			try: 
				scale_score = int(input(prompt))
			except ValueError:
				print('Sorry, that was an invalid response. Please input a number.')
				continue
			else:
				break
		if scale == "S_Ang":
			if scale_score < 15 or scale_score > 60:
				print ('Invalid response. Please make sure value inputed is between 15-60.')
				incorrect_response = True
			elif scale_score >= 15 and scale_score <= 60:
				incorrect_response = False
				Raw_scores.append(str(scale_score))
		elif scale == "S_Ang_F" or scale == "S_Ang_V" or scale == "S_Ang_P":
			if scale_score < 5 or scale_score > 20:
				print ('Invalid response. Please make sure value inputed is between 5-20.')
				incorrect_response = True
			elif scale_score >= 5 and scale_score <= 60:
				incorrect_response = False
				Raw_scores.append(str(scale_score))
		elif scale == "T_Ang":
			if scale_score < 10 or scale_score > 40:
				print ('Invalid response. Please make sure value inputed is between 10-40.')
				incorrect_response = True
			elif scale_score >= 10 and scale_score <= 40:
				incorrect_response = False
				Raw_scores.append(str(scale_score))
		elif scale == "T_Ang_T" or scale == "T_Ang_R":
			if scale_score < 4 or scale_score > 16:
				print ('Invalid response. Please make sure value inputed is between 4-16.')
				incorrect_response = True
			elif scale_score >= 4 and scale_score <= 16:
				incorrect_response = False
				Raw_scores.append(str(scale_score))
		elif scale == "AX_O" or scale == "AX_I" or scale == "AC_O" or scale == "AC_I":
			if scale_score < 8 or scale_score > 32:
				print ('Invalid response. Please make sure value inputed is between 8-32.')
				incorrect_response = True
			elif scale_score >= 8 and scale_score <= 32:
				incorrect_response = False
				Raw_scores.append(str(scale_score))
		elif scale == "AX_Index":
			if scale_score < 0 or scale_score > 96:
				print ('Invalid response. Please make sure value inputed is between 0-96.')
				incorrect_response = True
			elif scale_score >= 0 and scale_score <= 96:
				incorrect_response = False
				Raw_scores.append(str(scale_score))
	

def find_t_value(name, value, gender, age, filepath):
	if age == 19:
		with open(filepath+name+'_16_19.csv', 'r') as csvfile:
			readCSV = csv.reader(csvfile, delimiter=',')
			for row in readCSV:
				if row[0] == str(value):
					if gender == 'Male' or gender == 'male' or gender == 'm' or gender == 'M':
						T_Scores.append(row[1])
					elif gender == 'Female' or gender == 'female' or gender == 'F' or gender == 'f':
						T_Scores.append(row[2])
	elif age > 19 and age < 30:
		with open(filepath+name+'_20_29.csv', 'r') as csvfile:
			readCSV = csv.reader(csvfile, delimiter=',')
			for row in readCSV:
				if row[0] == str(value):
					if gender == 'Male' or gender == 'male' or gender == 'm' or gender == 'M':
						T_Scores.append(row[1])
					elif gender == 'Female' or gender == 'female' or gender == 'F' or gender == 'f':
						T_Scores.append(row[2])
	elif age > 29:
		with open('/Users/mplazar/Desktop/Python/STAXI_Scoring_Files/'+name+'_30.csv', 'r') as csvfile:
			readCSV = csv.reader(csvfile, delimiter=',')
			for row in readCSV:
				if row[0] == str(value):
					if gender == 'Male' or gender == 'male' or gender == 'm' or gender == 'M':
						T_Scores.append(row[1])
					elif gender == 'Female' or gender == 'female' or gender == 'F' or gender == 'f':
						T_Scores.append(row[2])


def write_csv(value):
	with open('Test.csv', 'r') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for line in readCSV:
			list_to_append.append(line)
		csvfile.close()
	list_to_append.append(value)
	if list_to_append[0] != header_labels:
		list_to_append.insert(0, header_labels)
	with open('Test.csv', 'w', newline='\n') as csvfile:
		writeCSV = csv.writer(csvfile, delimiter=',')
		for list in list_to_append:
			writeCSV.writerow(list)
		csvfile.close()



file_path = os.path.expanduser("~/Desktop/Python/STAXI_Scoring_Files/")
correct_age = False
correct_gender = False
print ('Welcome to STAXI-2 scoring program')
while correct_gender == False:
	Gender = input('Is the participant male or female:		')
	if Gender == 'M' or Gender == 'F' or Gender == 'm' or Gender == 'f' or Gender == 'Male' or Gender == 'Female' or Gender == 'male' or Gender == 'female':
		correct_gender = True
	else:
		print('Invalid response. Please input the participants gender.')
		correct_gender = False
		continue

while correct_age == False:
	while True:
		try: 
			Age = int(input('How old is the participant:	'))
		except ValueError:
			print('Sorry, that was an invalid response. Please input a number.')
			continue
		else:
			break
	if Age < 19 or Age > 30:
		print('The participant is to old or too young for the study.')
		correct_age = False
		continue
	else:
		correct_age = True

file_name = 'Test.csv'
Raw_scores = []
T_Scores = []
Total_Scores = []
list_to_append = []
x = float('nan')

header_labels = ['Participant ID', 'S_Ang', 'S_Ang_F', 'S_Ang_V', 'S_Ang_P', 'T_Ang', 'T_Ang_T', 'T_Ang_R', 'AX_O', 'AX_I', 'AC_O', 'AC_I', 'AX_Index','S_Ang_tscore', 'S_Ang_F_tscore', 'S_Ang_V_tscore', 'S_Ang_P_tscore', 'T_Ang_tscore', 'T_Ang_T_tscore', 'T_Ang_R_tscore', 'AX_O_tscore', 'AX_I_tscore', 'AC_O_tscore', 'AC_I_tscore', 'AX_Index_tscore']
Score_Categories = ['S_Ang', 'S_Ang_F', 'S_Ang_V', 'S_Ang_P', 'T_Ang', 'T_Ang_T', 'T_Ang_R', 'AX_O', 'AX_I', 'AC_O', 'AC_I', 'AX_Index']
ID = input('Particiapnt ID:	')
Total_Scores.append(ID)
with open(file_name, 'r', newline='') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for line in readCSV:
			if line[0] == Total_Scores[0]:
				print('Participant data has all ready been inputted. Do you want to continue?')
				answer = input('y/n:	')
				if answer == 'n':
					quit()
				else:
					csvfile.close()
					break

for i in range(len(Score_Categories)):
	get_accepted_value('Please input raw ' + str(Score_Categories[i])+ 'score:    ', Score_Categories[i], x)

for i in range(len(Score_Categories)):
	find_t_value(Score_Categories[i], Raw_scores[i], Gender, Age, file_path)

Total_Scores = Total_Scores + Raw_scores + T_Scores

write_csv(Total_Scores)



