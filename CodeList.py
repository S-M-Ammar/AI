
# setting codes
code_Teacher = {0 : "Sir Adeel",
                1 : "Sir Rafi",
                2 : "Sir Ghufran",
                3 : "Sir Yousaf",
                4 : "Sir Rehman",
                5 : "Mam Samina",
                6 : "Mam Hira",
                7 : "Dr Amanullah",
                8 : "Mr Mubashir",
                9 : "Sir Waqas",
                10: "Sir Danish",
                11: "Mam Saira",
                12: "Mam Sidra",
                13: "Mam Maria",
                14: "Sir Saeed"}

code_Subject = {0 : "Artificial Intelligence",
                1 : "Web-Engineering",
                2 : "System Programming",
                3 : "Software Development Artitechure",
                4 : "Engineering Economics",
                5 : "LAB-AI",
                6 : "LAB-SP",
                7 : "Network Security",
                8 : "Entrepreneurship",
                9 : "Human Computer Interaction",
                10: "Data Mining",
                11: "Ethics",
                12: "OS",
                13: "OS LAB",
                14: "Software Eng",
                15: "Software Eng LAB",
                16: "Probability",
                17: "Automata"}

class_type = {0:'Class' , 1:'Lab'}

Section = {0 : "Section A",
           1 : "Section B"}

Batch = {0 : "Batch-16",
         1 : "Batch-15",
         2 : "Batch-17"}

Room = {0 : 'System Lab',
        1 : 'Computer Lab',
        2 : 'F-02',
        3 : 'F-01',
        4 : 'G-03',
        5 : 'G-04',
        6 : 'G-05',
        7:  'G-01'}

Day = {0: 'Monday',
       1: 'Tuesday',
       2: 'Wednesday',
       3: 'Thursday',
       4: 'Friday',}

Time = []


#prototype of data source
# course_database = {key : [courseID,teacher,type,section,batch,] }
# it will be define by user and will be fixed for whole process
course_database = {

                   0:  [0,0,0,0,0],
                   1:  [1,3,0,1,0],
                   2:  [2,2,0,0,0],
                   3:  [3,4,0,1,0],
                   4:  [4,1,0,0,0],
                   5:  [5,6,1,1,0],
                   6:  [6,5,1,0,0],

                   7: [0,0,0,0,0],
                   8: [1,3,0,1,0],
                   9: [2,2,0,0,0],
                   10: [3,4,0,1,0],
                   11: [4,1,0,0,0],

                   12: [0,0,0,1,0],
                   13: [1,3,0,0,0],
                   14: [2,2,0,1,0],
                   15: [3,4,0,0,0],
                   16: [4,1,0,1,0],
                   17: [5,6,1,0,0],
                   18: [6,5,1,1,0],




                   19: [0,0,0,1,0],
                   20: [1,3,0,0,0],
                   21: [2,2,0,1,0],
                   22: [3,4,0,0,0],
                   23: [4,1,0,1,0],

# batch-15 Subjects

                   24: [7,0,0,1,1],
                   25: [8,8,0,1,1],
                   26: [9,7,0,1,1],
                   27: [10,7,0,1,1],

                   28: [7,0,0,1,1],
                   29: [8,8,0,1,1],
                   30: [9,7,0,1,1],
                   31: [10,7,0,1,1],

# batch-17 Subjects

                   32: [12,9,0,0,2],
                   33: [12,9,0,0,2],
                   34: [13,5,1,0,2],
                   35: [14,10,0,0,2],
                   36: [14,10,0,0,2],
                   37: [15,12,1,0,2],
                   38: [16,11,0,0,2],
                   39: [16,11,0,0,2],
                   40: [17,13,0,0,2],
                   41: [17,13,0,0,2],
                   42: [11,14,0,0,2],
                   43: [11,14,0,0,2],

                   44: [12,9,0,1,2],
                   45: [12,9,0,1,2],
                   46: [13,9,1,1,2],
                   47: [14,10,0,1,2],
                   48: [14,10,0,1,2],
                   49: [15,6,1,1,2],
                   50: [16,11,0,1,2],
                   51: [16,11,0,1,2],
                   52: [17,13,0,1,2],
                   53: [17,13,0,1,2],
                   54: [11,14,0,1,2],
                   55: [11,14,0,1,2]



                   }





