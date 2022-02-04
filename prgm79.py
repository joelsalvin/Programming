class Rectangle:
    def getmeasurement(self,len,wid):
        self.len=len
        self.wid=wid
class Cuboid(Rectangle):
    def getheight(self,len,wid,ht):
        self.getmeasurement(len,wid)
        self.ht=ht
    def __le__(self,other):
        return((self.len*self.wid*self.ht)<=(other.len*other.wid*other.ht))
try:

c1=Cuboid()
c2=Cuboid()
c1.getheight(7,3,10)
c2.getheight(2,3,4)
if c1<=c2:
    print("c1 is less than or equal to c2")
else:
    print("c1 is greater than c2")
except Expression as e:
    print(e)
    
