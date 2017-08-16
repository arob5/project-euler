#
# problem_id_17.py
# Problem: Counting Sundays
# Last Modified: 8/16/2017
# Modified By: Andrew Roberts
#

import datetime

start_date = datetime.datetime.strptime("01Jan1901", "%d%b%Y") + datetime.timedelta(days=5)
end_date = datetime.datetime.strptime("31Dec2000", "%d%b%Y")

current_date = start_date

count = 0
while current_date != end_date:
	if current_date.day == 1:
		count += 1
	current_date += datetime.timedelta(days=7)
	
print(count)
