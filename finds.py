import random

attributes=[['sunny','rainy'],['warm','cold'],['normal','high'],['strong','weak'],['warm','cool'],['same','change']]
num_attributes = (len(attributes))
#print num_attributes

def getRandomTrainingExample(target_concept=['?']*num_attributes):
	training_example= [ ]
	classification=True
	for i in xrange(num_attributes):
		training_example.append(attributes[i][random.randint(0,1)])
		if target_concept[i] != ['?'] and target_concept[i] != training_example[i]:
			classification=False

			####print(training_example,classification)
	return training_example,classification

def main():
	target_concepts = ['sunny','warm','?','strong','?','?']
	num_experiments=10
	training_examples=[]

	for i in range(num_experiments):
		training_examples.append(getRandomTrainingExample(target_concepts))
		print(training_examples[i])	

if __name__ == '__main__':
	main()
