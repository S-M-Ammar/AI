import  datetime

import random
#
#
# x_start = datetime.time(8,5,0)
# x_end = datetime.time(9,30,0)
#
# testClass_start = datetime.time(8,0,0)
# testClass_end = datetime.time(9,25,0)
#
# # start time clash
#
# if(testClass_start>=x_start and testClass_start<=x_end):
#     print("test start time is in between x class")
#
# if(testClass_end>=x_start and testClass_end<=x_end):
#     print("test end time is in between x class")
#
# num = random.random()
#
# print(num)

x_start = datetime.time(8,5,0)
x_end = datetime.time(9,30,0)

testClass_start = datetime.time(8,0,0)
testClass_end = datetime.time(9,30,0)

if(x_start==testClass_start and x_end==testClass_end):
    print("True")