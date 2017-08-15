#
# problem_id_6.py
# Problem: Sum Square Difference
# Last Modified: 8/14/2017
# Modified By: Andrew Roberts
#

def sum_of_squares(n):
	sos = 0
	for i in range(1, n+1):
		sos += (i*i)
	return sos

def square_of_sum(n):
	sos = 0
	for i in range(1, n+1):
		sos += i
	return (sos*sos)

print("Difference = ", square_of_sum(100) - sum_of_squares(100))
