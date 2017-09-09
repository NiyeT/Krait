import binascii
import itertools

class enkrypt:
	def __init__(self):
		pass

	target='testing'

	def all_poss(self,target):
		poss=[]
		for groupN in range(len(target)):
			groupN+=1
			group_combos=itertools.combinations(target,groupN)
			for combo in group_combos:
				poss.append(combo)
		return poss

encode=enkrypt()
poss=encode.all_poss('test')
for val in poss:
	print(val)

