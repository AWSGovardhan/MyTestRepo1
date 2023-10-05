#Code to manage the contents of a DYNAMIC List
'''
1. Add new item to the end of the list.
2. Search for an item in the list.
3. Insert an item at a given index position.
4. Display the complete list of items.
5. Stop/Exit.
'''

s = []

def menu():
    print('1. Add item at end.')
    print("2. Search Item.")
    print("3. Insert at index.")
    print("4. Display all items.")
    print("5. To Exit/Stop.")


def main():
    ch = int(input("Enter Choice :: "))
    while(ch<=4):
        if ch==1:
            n = int(input("Enter integer element to add to list :: "))
            s.append(n)
            print("Element added to the list!")
        elif ch==2:
            num = int(input("Enter the number you are looking :: "))
            if s.count(num) != 0:
                print("Given number ",num,' is found ',s.count(num),'times in the list')
                print("Given number is found first at index",s.index(num))
            else:
                print("Element ",num,"Doesn\'t exist in the list  ",s)
        elif ch==3:
            idx = int(input("Enter the index where we want to insert the element :: "))
            num = int(input('Enter the integer number we want to insert'))
            s.insert(idx,num)
            print("Given number ",num," added at the given index",idx)
        elif ch==4:
            print("Following are the items in the list ... ")
            print(s)
            # for e in s:
            #     print(e)
        else:
            exit();
        menu()
        ch = int(input("Enter your choice again :: "))

if __name__ == '__main__':
    main()