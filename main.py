
import re
from collections import defaultdict
import sys


# read the file
file = open("small-artist-list.txt","r")

# initialise a python dictionary to store counts of artist pairs occuring together in a list
total_count = defaultdict(int)

# iterate over every line in the file 
for line in file:
  a = re.split(',',line.strip())
  
  # iterate over all words in a line - a nested for loop is use to exhaust all possible combinations of pairs. 
  for b in a:
    for c in a:
      # add 1 to the count if a particular pair is observed in the list/line   
      total_count[(b,c)] += 1

 # initialise a python dictionary that will be used to exclude pairs already printed to file 
print_test = defaultdict(int)

# initialise a python dictionary that will be used to exclude pairs already output.      
for b,c in total_count:
  # The if condition below ensures that only artist pairs, which appear together in at least 50 list are output. In addition, pairs consisting of the same artist and those already output are excluded.
  if (total_count[(b,c)] > 49) and (print_test[(b,c)] !=1) and (b != c):
    sys.stdout.write("%s,%s \n" % (b,c)) 
    print_test[(c,b)] = 1
  


