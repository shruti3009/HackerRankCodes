nested_lst = []
seq = "apples, banana, oranges, grapes, blueberry"
lst1 = (seq.split(','))
seq2 = "red, yellow, orange, green, blue"
lst2 = (seq2.split(','))

#for i in lst1: This will store the elements of lst1 in i. It will not store the index
for i in range(0, len(lst1)):
        temp_list=[]
        temp_list.append(lst1[i])
        temp_list.append(lst2[i])
        nested_lst.append(temp_list)
print(nested_lst)
