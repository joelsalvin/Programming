class flower:
    def __init__(self,f):
        self.name = f
    def show(self):
        if(hasattr(self,'petalcolor')):
            print(self.petalcolor," ",self.name)
        else:
            print("Unkown Flower!")
                
F1=Flower('rose')
setattr(F1,'petalcolor','red')
F1.show()
