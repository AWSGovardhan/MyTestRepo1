class MyStud:
    def __init__(self,rno,sna,mks):
        self.rno = rno
        self.sna = sna
        self.mks = mks

    def __str__(self):
        print(self.rno,',',self.sna)
        if(len(self.mks) != 0):
            print('Details of marks scored is as follows... ')
            for subj in self.mks.items():
                print(subj[0],' ',subj[1])

    
    # def dispStudDtls(self):
    #     print()

def main():
    s1 = MyStud1(101,'James',mks={'s1':20,'s2':56})


if __name__ == "__main__":
    main()