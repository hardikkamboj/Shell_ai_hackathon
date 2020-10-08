import pandas as pd 
import numpy as np 
from itertools import combinations

file_dir = 'scores.csv'
data = pd.read_csv(file_dir,index_col=0)
print(data.head())
scores_dict = data.to_dict()['1']

# print(scores_dict)
# print(scores_dict[2017])
years_combs = list(combinations(scores_dict.keys(),3))
all_combs = list(combinations(scores_dict.values(),3))


comb_dict = {}
for i in range(len(years_combs)):
	comb_dict[years_combs[i]] = sum(list(all_combs[i])) / 3 

data = pd.DataFrame(comb_dict,index = [1]).T	
data.to_csv('comb_data.csv')