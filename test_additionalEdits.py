import csv 
import random

def main():
	with open ('testWordBankCorpus.csv') as csvfile: 
		reader = csv.DictReader(csvfile) 
		# initialize an empty dictionary
		lexical_Dict = {}
		for row in reader:
			# check that BROWN_FREQ and WORD_CATEGORY are not empty
			if row['BROWN_FREQ'] != '' and row['WORD_CATEGORY'] != '':
				# if they are both not empty, store 'WORD':'FREQ' as
				# key-value pair in the dictionary 
				lexical_Dict[row['WORD']] = row['BROWN_FREQ']

				# also check that WORD_CATEGORY is not C,R,I,O??? 

		print(lexical_Dict)
		# get the keys of the dictionary in a list
		keys = lexical_Dict.keys()
		# randomize the list
		randomize = random.shuffle(keys)
		print(keys)

main()

 

 



