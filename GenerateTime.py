

Time_code = []
def takeTime():
    start = int(input("Enter Start time in 24 hour format\n"))
    end  = int(input("Enter End time in 24 hour format\n"))



    for x in range(start,end,1):

        for y in range(0,45,15):

            Time_code.append([x,y])



    Time_code.append([end,0])
    return Time_code


