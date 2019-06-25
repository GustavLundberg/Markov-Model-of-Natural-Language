import numpy as np
import glob
import pandas as pd

# List of paths to files
path_list = glob.glob('C:/Python_devenv/Data/BBC_sport/bbcsport-fulltext/bbcsport/athletics/[0-9]*.txt')

#ref = open('C:/Python_devenv/Data/BBC_sport/bbcsport-fulltext/bbcsport/athletics/001.txt', 'r')

#df = pd.read_csv('C:/Users/Gustav.K.Lundberg/Downloads/transaction_data.csv')
#print(df.head(n=5))
#for line in ref:
#	print(line)
#	print('-----')

glob_word = ''
arr = np.array()
print(arr)

for path in path_list:
	with open(path, 'r') as file:
		next(file) # Skip first line, i.e. the header
		file_bread = file.read()
		print(file_bread)

		#for line in file:
		#	if line in ['\n', '\r\n', '\r']:
		#		continue	
		#	print(line)
		break

