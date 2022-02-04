class Book:
    def __init__(self):
        self.title = input("Enter the Title:")
        self.author = input("Enter the Author:")
    def display(self):
        if(hasattr(self,'publisher')):
            print(self.title," written by ",self.author," is published by ",self.publisher)
        else:
            print("Unknown Publisher")
                
B1=Book()
setattr(B1,'publisher','h&c')
B1.display()
