#
# problem_id_1.py
# Problem: Multiples of 3 and 5
# Last Modified: 8/14/2017
# Modified By: Andrew Roberts
#

sum = 0
for x in range(1000):
	if (x % 3 == 0) or (x % 5 == 0):
		sum += x

print(sum)
