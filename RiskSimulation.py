# A two dimensional list in which the outer index represents the number of defending dice minus one,
# and the inner index represents the number of attacking dice minus one. Each element is a 
# dictionary s.t. all the keys are the possible reductions in attacking or defending units, and the
# values are the probabilites of these occuring. These probabilites were brute-force calculated.

resultProbs = [[
				{(0, -1): 21.0/36, (-1, 0): 15.0/36},
				{(0, -1): 91.0/216, (-1, 0): 125.0/216},
				{(0, -1): 441.0/1296, (-1, 0): 855.0/1296}
			  ], [
				{(0, -1): 161.0/216, (-1, 0): 55.0/216}, 
				{(0, -2): 581.0/1296, (-1, -1): 420.0/1296, (-2, 0): 295.0/1296},
				{(0, -2): 2275.0/7776, (-1, -1): 2611.0/7776, (-2, 0): 2890.0/7776}
			  ]]


# This function calculates the probabilities of winning in a single battle.
# 
# inputProbabilites is a list of doubles s.t. the ith element contains the probability that
# there are i attacking units at the beginning of the battle. The defenseSize should be
# a non-negative integer denoting the number of defending units. The code guarentees no specific
# behavior if these conditions are not met.
#
# The function outputs a list of doubles having the same size as inputProbabilites. The ith element
# in the list denotes the probability that the attacker wins with i surviving units. The 0th element
# of the output is always 0.
def simulateBattle(inputProbabilities, defenseSize):
	if(defenseSize == 0):
		return inptuProbabilities

	attackSize = len(inputProbabilities) - 1
	probs = [[0 for i in range(0, attackSize + 1)] for i in range(0, defenseSize + 1)]
	probs[defenseSize] = inputProbabilities

	for i in range(defenseSize, 0, -1):
		for j in range(attackSize, 0, -1):
			combinations = resultProbs[min(2, i) - 1][min(3, j) - 1]
			for tp in combinations:
				probs[i + tp[0]][j + tp[1]] += combinations[tp]*probs[i][j]

	output = probs[0]
	return output

# This function calculates the probability of success in a campaign of successive battles.
# 
# The attackSize input is a positive integer denoting the original number of atacking units.
# defenseSizes is a list of non-negative integers with a length no greater than attackSize. Each
# element in defenseSizes represents a defensive foce the attacking units have to fight, beginning
# with defenseSizes[0]. In risk, when successively fighting defensize forces, the attacker must
# leave one unit behind each time he fights a new force. He may choose to leave more units behind;
# Should the attacker wish to do this, insert an additional 0 between those fights for each extra
# unit left behind. Again, the code makes no guarentees if these conditions are not met.
#
# If minWin is non-negative, the function outputs a double in [0, 1] denoting the probability that
# the attacker wins the campaign with at least minWin surviving units. If minWin is negative the
# code outputs a list similar to the output of simulateBattle.
def simulateCampaign(attackSize, defenseSizes, minWin = 0):
	attackers = [0 for i in range(0, attackSize + 1)]
	attackers[attackSize] = 1
	
	attackers = simulateBattle(attackers, defenseSizes[0])
	for i in defenseSizes[1:]:
		del attackers[0]
		attackers = simulateBattle(attackers, i)

	return attackers if minWin < 0 else sum(attackers[minWin:])