#
# problem_id_4.py
# Problem: Largest palindrome product
# Last Modified: 8/14/2017
# Modified By: Andrew Roberts
#

def largest_palindrome():
	largest_product = 0
	palin = None
	for i in range(100, 1000):
		for j in range(100, 1000):
			prod = i * j
			if str(prod) == str(prod)[::-1]:
				if prod > largest_product:
					largest_product=prod 
					palin = prod
	return palin

print("Largest palindrome: ", largest_palindrome())
