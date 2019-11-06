def bubblesort(list):
    for x in range(len(list)):
        y = len(list)-1
        while(y>x):
            if list[y] < list[y-1]:
                tmp = list[y]
                list[y] = list[y-1]
                list[y-1] = tmp
            y -= 1
    return list

list = []
list.append(7)
list.append(1)
list.append(4)
list.append(8)
list.append(3)
list.append(2)
list.append(1)
print(list)
bubblesort(list)
print(list)