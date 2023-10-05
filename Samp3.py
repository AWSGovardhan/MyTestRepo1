class Stud:
    def __init__(self,rno,sna):
        self.rno = rno
        self.sna = sna

    def dispStudDtls(self):
        print("Roll Number :: ",self.rno)
        print("Name of the student :: ",self.sna)

def main():
    s1 = Stud(1,'AAA')
    s1.dispStudDtls()

    slist = [Stud(101,'Sunil'),Stud(102,'Mallik'),Stud(103,'Rehman')]

    for stud in slist:
        stud.dispStudDtls()
        print("================")

if __name__ == '__main__':
    main()