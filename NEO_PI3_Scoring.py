# This program will take raw scores from NEO-PI3 and write raw scores and t-scores in an excel file
import csv
import os
def get_accepted_value(prompt, name):
	incorrect_response = True
	while incorrect_response == True:
		while True:
			try: 
				name = int(input(prompt))
			except ValueError:
				print('Sorry, that was an invalid response. Please input a number.')
				continue
			else:
				break
		if name < 0 or name > 32:
			print ('Invalid response. Please make sure value inputed is between 0-32.')
			incorrect_response = True
		elif name > 0 and name <= 32:
			incorrect_response = False
			Raw_scores.append(str(name))
	

def find_t_value(name, value, gender, filepath):
	with open(filepath+name+'.csv', 'r') as csvfile:
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



file_path = os.path.expanduser("~/Desktop/Python/NEO_Scoring_Files/")
print ('Welcome to NEO-PI3 scoring program')
Gender = input('Is the participant male or female:		')
file_name = 'Test.csv'
Raw_scores = []
T_Scores = []
Total_Scores = []
list_to_append = []

header_labels = ['Participant ID', 'Raw_N1', 'Raw_N2', 'Raw_N3', 'Raw_N4', 'Raw_N5', 'Raw_N6', 'Raw_E1', 'Raw_E2', 'Raw_E3', 'Raw_E4', 'Raw_E5', 'Raw_E6', 'Raw_O1', 'Raw_O2', 'Raw_O3', 'Raw_O4', 'Raw_O5', 'Raw_O6', 'Raw_A1', 'Raw_A2', 'Raw_A3', 'Raw_A4', 'Raw_A5', 'Raw_A6', 'Raw_C1', 'Raw_C2', 'Raw_C3', 'Raw_C4', 'Raw_C5','Raw_C6', 'Raw_N', 'Raw_E','Raw_O', 'Raw_A', 'Raw_C', 'T_Score_N1', 'T_Score_N2', 'T_Score_N3', 'T_Score_N4', 'T_Score_N5', 'T_Score_N6', 'T_Score_E1', 'T_Score_E2', 'T_Score_E3', 'T_Score_E4', 'T_Score_E5', 'T_Score_E6', 'T_Score_O1', 'T_Score_O2', 'T_Score_O3', 'T_Score_O4', 'T_Score_O5', 'T_Score_O6', 'T_Score_A1', 'T_Score_A2', 'T_Score_A3', 'T_Score_A4', 'T_Score_A5', 'T_Score_A6', 'T_Score_C1', 'T_Score_C2', 'T_Score_C3', 'T_Score_C4', 'T_Score_C5','T_Score_C6', 'T_Score_N', 'T_Score_E', 'T_Score_O', 'T_Score_A', 'T_Score_C']
Raw_Score_Categories = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'C1', 'C2', 'C3', 'C4', 'C5','C6']
T_Score_Categories = ['N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'C1', 'C2', 'C3', 'C4', 'C5','C6', 'N', 'E', 'O', 'A', 'C']
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

for i in range(len(Raw_Score_Categories)):
	get_accepted_value('Please input raw ' + str(Raw_Score_Categories[i])+ 'score:    ', Raw_Score_Categories[i])

Raw_scores.append(str(int(Raw_scores[0])+int(Raw_scores[1])+int(Raw_scores[2])+int(Raw_scores[3])+int(Raw_scores[4])+int(Raw_scores[5])))
Raw_scores.append(str(int(Raw_scores[6])+int(Raw_scores[7])+int(Raw_scores[8])+int(Raw_scores[9])+int(Raw_scores[10])+int(Raw_scores[11])))
Raw_scores.append(str(int(Raw_scores[12])+int(Raw_scores[13])+int(Raw_scores[14])+int(Raw_scores[15])+int(Raw_scores[16])+int(Raw_scores[17])))
Raw_scores.append(str(int(Raw_scores[18])+int(Raw_scores[19])+int(Raw_scores[20])+int(Raw_scores[21])+int(Raw_scores[22])+int(Raw_scores[23])))
Raw_scores.append(str(int(Raw_scores[24])+int(Raw_scores[25])+int(Raw_scores[26])+int(Raw_scores[27])+int(Raw_scores[28])+int(Raw_scores[29])))

for i in range(len(T_Score_Categories)):
	find_t_value(T_Score_Categories[i], Raw_scores[i], Gender, file_path)

Total_Scores = Total_Scores+Raw_scores + T_Scores

write_csv(Total_Scores)



