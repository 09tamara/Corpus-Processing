import csv 
with open ('testWordBankCorpus.csv') as csvfile: #our dictionary | was 'testWordBankCorpus.csv'
	reader = csv.DictReader(csvfile) 
	for row in reader:
		
		if row['BROWN FREQ'] and row['WORD_CATEGORY']: # ? if not empty then add to lexical 
			print (row ['WORD'], row ['WORD_CATEGORY'])  # store instead of print it into lexical dictionary 



 

 



