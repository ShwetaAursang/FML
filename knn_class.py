import pandas as pd
import math as ma
from scipy.stats import rankdata

class Knn_Class:
	frame = pd.read_csv('knn.csv')
	def __init__(self,a,s,k):
		self.acid_durablity = a
		self.strength = s
		self.K = k
		self.good = 0
		self.bad = 0
		
	def find_edistance(self):
		self.lis = []
		length = Knn_Class.frame.Name.count()
		#print(length)
		for i in range(0,length):
			ad = Knn_Class.frame.iloc[i,1]
			ad = ad - self.acid_durablity
			ad = ad * ad
			s = Knn_Class.frame.iloc[i,2]
			s = s - self.strength
			s = s * s
			ans = ad + s
			ans = ma.sqrt(ans)
			self.lis.append(ans)
			rank_lis = rankdata(self.lis)
		#print(rank_lis)
		#print(lis)
		self.lis1 = list(Knn_Class.frame.Name)
		self.lis2 = list(Knn_Class.frame.Acid_durablity)
		self.lis3 = list(Knn_Class.frame.Strength)
		self.lis4 = list(Knn_Class.frame.Class)
		self.dic = {'Name' : self.lis1,
				'Acid_durablity' : self.lis2,
				'Strength' : self.lis3,
				'Class' : self.lis4,
				'e_distance' : self.lis,
				'Rank' : rank_lis}

		#print(dic)
		self.new = pd.DataFrame(self.dic,columns = ['Name','Acid_durablity','Strength','Class','e_distance','Rank'])
		#print(self.new)
		self.df = self.new.sort_values('Rank')
		self.df.reset_index(drop=True, inplace=True)
		#print(self.df)
		self.list1 = []
		for j in range(0,self.K):
			self.value =self.df.iloc[j,3]
			self.list1.append(self.value)
		#print(list1)
		self.leng = len(self.list1)
		for i in range(0,self.leng):
			if self.list1[i] == 'Good':
				self.good = self.good + 1
			else:
				self.bad = self.bad + 1
		result = []
		result.append(self.good)
		result.append(self.bad)
		return result






