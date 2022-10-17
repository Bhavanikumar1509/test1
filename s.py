class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class link():
    def __init__(self):
        self.head=None
    def crea(self,n):
        data=int(input("Enter the number:"))
        self.head=Node(data)
        tmp=self.head
        for i in range(1,n):
            data=int(input("enter the number:"))
            tmp.next=Node(data)
            tmp=tmp.next

    def prin(self):
        tmp=self.head
        while(tmp):
            print(tmp.data,"->",end=" ")
            tmp=tmp.next

if __name__=='__main__':
    n=int(input("enter the size of the linked llist:"))
    l=link()
    l.crea(n)
    l.prin()