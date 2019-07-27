class Population:
     chromosomeList = []
     populationLimit = 0
     def __init__(self):
          self.chromosomeList = []




class Chromosome:
     geneList = []
     fitness = 0
     def __init__(self):
          self.geneList = []
          self.fitness = 0





class ChromosomeGene:
     CourseID = 0
     Teacher = 0
     Section = 0
     Type = 0
     Batch = 0
     Room = 0
     start_time = []
     end_time = []
     Day = 0

     def __init__(self,CourseID,Teacher,Section,Type,Batch,Room,start_time,end_time,Day):
          self.Batch = Batch
          self.CourseID = CourseID
          self.Section = Section
          self.Type = Type
          self.Teacher = Teacher
          self.Day = Day
          self.Room = Room
          self.end_time = end_time
          self.start_time = start_time






