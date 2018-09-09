##################################################################################
##################################################################################
## Template file for problem 1. 						##
## First, fill in your answer logic below					##
##################################################################################
#                                LOGIC GOES BELOW                     		#
##################################################################################
#
#
#
#
#
##################################################################################
##################################################################################
## You have to fill in two functions BELOW 					##
## Both take in input n = number of sides in the die 				##
## 										##									##
## 1. findSumDieRoll(n)	: Return expected value of sum 				##
## 2. findNumberOfRolls(n)  : Return expected value of number of rolls 		##
## 										##									##
## For both, you only have to fill in the math function where indicated     	##
## 										##									##
## You can run this template file to see the output of your functions       	##
## for a 6 sided die.								##
## Simply run: `python problem1_template.py`                            	##
## You should see the output printed once your program runs.                	##
##                                                                          	##
## DO NOT CHANGE ANYTHING ELSE BELOW. ONLY FILL IN THE LOGIC.      		##
##                                                                          	##
## Good Luck!                                                               	##
##################################################################################
##################################################################################


def findSumDieRoll(n):
	##################################
	##          FILL ME IN          ##
	##################################
	# n is a float
	sumRolls = n/2 # Replace me with your answer
	  /* there are several posibilities, first if you have n=2, then first 1 is followed by 2 or 3 or 4 or 5 or 6, or 2 is followed by (3 or 4 or 5 or 6) and so on.
	     so the sequence would be (1,2)(1,3)(1,4)(1,5)(1,6),(2,3)(2,4)(2,5)(2,6) and same for 3,4,5,6.	
         */
	return round(sumRolls, 2)

def findNumberOfRolls(n):
	##################################
	##          FILL ME IN          ##
	##################################
	# n is a float
	numRolls = n/2	# Replace me with your answer
	/* If you have an M sided die and you run N trials, the probability they are increasing is just (MCN)/M^N.
This is simply because there are (MCN) ways to get increasing die rolls (all of which are equally likely) and there are M^N possible ways to roll the dice (again, all of which are equally likely).
	
	
   */
	return round(numRolls, 2)

if __name__ == "__main__":
	numberOfSides = 6.0
	sumOfRolls = findSumDieRoll(numberOfSides)
	numberOfRolls = findNumberOfRolls(numberOfSides)
	print('For a %i-sided die, expected value of sum: %.2f and number of rolls: %.2f'%(numberOfSides, sumOfRolls, numberOfRolls))
