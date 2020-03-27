# Defining the linked list and function to print it
class Node:
    def __init__(self,data):
        self.data = data  # Assign data to node
        self.next = None  # Initialize next to NULL
class LL:
    def __init__(self):
        self.head = None   # Initialize head to NULL. Empty linked list

    def showList(self):
        temp = self.head   # Point temporary pointer to HEAD
        while temp:        # while temp is not NULL, i.e, linked list has not ended, i.e, node->next != NULL
            print(temp.data,"->")
            temp = temp.next

# Main
if __name__ == '__main__':
    s1,s2,s3 = [],[],[]      # Stacks
    # Input : Default
    num1,num2 = 200,80000   # Sum we've to find out : 200 + 8000
    print("Numbers : {} and {}".format(num1,num2))
    n1 = list("200")
    n2 = list("8000")

    ll1,ll2 = LL(),LL()
    # Linked list 1:
    ll1.head = Node(n1[0])
    second1 = Node(n1[1])
    third1 = Node(n1[2])
    # Link the nodes
    ll1.head.next = second1
    second1.next = third1

    # Linked list 2:
    ll2.head = Node(n2[0])
    second2 = Node(n2[1])
    third2 = Node(n2[2])
    fourth2 = Node(n2[3])
    # Link the nodes
    ll2.head.next = second2
    second2.next = third2
    third2.next = fourth2

    # Print list 1 and list 2
    print("The numbers in linked list : ")
    print("Number 1 : ")
    ll1.showList()
    print("Number 2 : ")
    ll2.showList()

    # Pushing the numbers to stacks in reverse order
    # Number 1:
    s1.append(n1[2])
    s1.append(n1[1])
    s1.append(n1[0])

    # Number 2:
    s2.append(n2[3])
    s2.append(n2[2])
    s2.append(n2[1])
    s2.append(n2[0])

    # Test : print(s1,"\n",s2)

    # Check conditions
    if len(n2) > len(n1):
        zeroes = len(n2)-len(n1)
        for i in range(zeroes):
            s1.append(0)
    elif len(n2) < len(n1):
        zeroes = len(n1)-len(n2)
        for i in range(zeroes):
            s2.append(0)
    else:
        pass

    # Test 2: print(s1,"\n",s2)

    for i in range(len(s1)):
        # Initialize carry
        c = [0]*len(s1)             # Initialize the carry array.
        if len(list(str(int(s1[i]) + int(s2[i])))) == 1:     # No carry
            s3.append(str(int(s1[i]) + int(s2[i]) + int(c[i])))
        else:                                                # Carry exists
            c[i] = list(str(s1[i] + s2[i]))[0]                  # The tenth's digit
            s3.append(str(int(s1[i]) + int(s2[i]) + int(c[i])))
    
    # Printing the result
    final = reversed(s3)
    final_res = ""
    print("\nSum of {} and {} is = {}".format(num1,num2,final_res.join(final)))

    
