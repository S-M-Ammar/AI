import CodeList
import random

def set_timing_for_lab():
    st = [0,0]
    et = [0,0]

    while ((et[0] - st[0]) != 3 or (et[1] - st[1] != 0)):
        et = random.choice(CodeList.Time)
        st = random.choice(CodeList.Time)

    return [st, et]

def set_timing_for_class():
    st = [0,0]
    et = [0,0]

    while ((et[0] - st[0]) != 1 or (et[1] - st[1] != 30)):
        et = random.choice(CodeList.Time)
        st = random.choice(CodeList.Time)

    return [st,et]