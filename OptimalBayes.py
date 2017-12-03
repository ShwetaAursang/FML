V=["positive","negative"]
PjGivenh=[[1,0],[0,1],[0,1]]
PhGivenD=[0.4,0.3,0.3] 

argmax=0 #index of Value
maxsum=0 #argument in V with max sum of probabilities
for j in range(len(V)):
	sum=0
	for h in range(len(PhGivenD)):
		sum=sum+(PjGivenh[h][j]*PhGivenD[h])
	if sum>maxsum:
		maxsum=sum
		argmax=j
		
print(V[argmax])
print(maxsum)