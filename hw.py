list = [2, 3, 4, 5]
even = []
for i in list:
    if (i*i)%2 == 0:
        list.append(even)
    else:
        continue

print ("All the even square numbers from 2 - 5 are: ",even)