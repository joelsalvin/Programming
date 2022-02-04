class Person:
  def __init__(self,name='Joel',roll=10):
      self.__name = name
      self.rollno = roll

  def display(self):

     print('Name : ',self.__name)
     print('Rollno: ',self.rollno)
     

class Mark:

  def __init__(self,m=85,c=25):

    self.maths = m
    self.computer=c

  def display(self):

    print('maths mark: ',self.maths)
    print('computer mark: ',self.computer)
    t= self.maths +self.computer
    if(t>=50):
           print('total=',t)

class Student(Person,Mark):

   def __init__(self,name,roll,m,c):

       super().__init__(name,roll)

       Mark.__init__(self,m,c)

       

   def display(self):

       super().display()

       Mark.display(self)
       

S=Student("Jeff",120,25,50)
S.display()
           
    
