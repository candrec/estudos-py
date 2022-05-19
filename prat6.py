table_data = [['apples','oranges','cherries','banana'],
              ['Alice','Bob','Carol','David'],
              ['dogs','cats','moose','goose']]

list1 = table_data[0]
list2 = table_data[1]
list3 = table_data[2]

for i in range(len(list1)):
    print(list1[i].rjust(8),list2[i].rjust(8),list3[i].rjust(8))
