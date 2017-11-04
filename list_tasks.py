if __name__ == '__main__':
    n = int(raw_input())

mylist=[]

for i in range(n):
    command = raw_input()
    things = command.split()
    #print things
    if things[0] == "insert":
        #mylist[int(things[1])] = int(things[2]) this is replacing the value and not inserting
        mylist.insert(int(things[1]),int(things[2]))
    elif things[0] == "print":
        print mylist
    elif things[0] == "remove":
        mylist.remove(int(things[1]))
    elif things[0] == "append":
        mylist.append(int(things[1]))
    elif things[0] == "sort":
        mylist.sort()
    elif things[0] == "pop":
        mylist.pop()
    elif things[0] == "reverse":
        mylist.reverse()
        
