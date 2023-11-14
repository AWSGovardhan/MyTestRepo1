class MyCls1:
    def __init__(self,rno,sna):
        self.rno = rno
        self.sna = sna
    def __str__(self):
        return str(self.rno)+','+self.sna
    
    def __gt__(self,pobj):
        if self.rno > pobj.rno:
            return True
        else:
            return False
        
def main():
    s1 = MyCls1(5,'James')
    s2 = MyCls1(2,'Harry')

    print(s1)
    print('====================')
    print(s2)

    if s1>s2:
        print('Student s1 has higher value of roll number than the Student s2')

if __name__ == '__main__':
    main()