# double ended queue, menu driven program
class DQ:
    def __init__(self):
        self.dq=[]
    def isEmpty(self):
        return len(self.dq)==0
    
    def insert_at_start(self, e):
        self.dq.insert(0,e)

    def insert_at_back(self, e):
        self.dq.append(e)

    def  delete_from_front(self):
        if not self.isEmpty():
            return self.dq.pop()
        else:
            print('Underflow')

    def delete_from_back(self):
        if not self.isEmpty():
            return  self.dq.pop(0)
        else:
            print('Underflow')
    def  display(self):
        print(self.dq)

d = DQ()
def menu():
    print( "\n1.Insert at Start")
    print("2.Insert at End/Back")
    print("3.Delete from Front")
    print("4.Delete from Back")
    print("5.Display")
    print("6.Exit\n")

while True:
    try:
        menu()
        x=int(input("\nEnter the choice : "))
        if x ==1:
            e = int(input('Enter the  element to be inserted : '))
            d.insert_at_start(e)
        elif  x ==2:
            e = int(input('Enter the element to be inserted : '))
            d.insert_at_back(e)
        elif x ==3:
            d.delete_from_front()
        elif x==4:
            d.delete_from_back()
        elif x==5:
            d.display()
        elif x==6:
            print("Exiting...")
            break
    except:
        print("Please enter a valid choice!")    
