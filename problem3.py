#!/usr/bin/env python3

file = open('CO-OPS.csv')
next(file)
max_change = -1.7976931348623517e+308 # arbitrary high float value
date_change = ""
prev_level = -1.7976931348623517e+308 # arbitrary high float value
for line in file:
   column = line.split(",") # splits file to isolate water level column
   curr_level = column[1] 
   datetime = column[0]
   if(curr_level == ""): curr_level = prev_level # accounts for blank value in column
   if(prev_level == -1.7976931348623517e+308):
      prev_level = float(curr_level)
   else:
      if(float(curr_level) - prev_level >= max_change): # goes through file to find max difference between values
         max_change = float(curr_level) - prev_level
         prev_level = float(curr_level)
         date_change = datetime
      else: prev_level = float(curr_level)
print "The maximum change was", max_change, "and occurred on", date_change

