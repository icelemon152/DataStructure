# using list as array

data = [1,2,3,4,5]

data.append(6)
data.insert(0,0)
data.remove(4)


data.index(2)

def find(arr, num):
    i = -1
    for n in arr:
        i +=1
        if num == n:
            return i
    else:
        return -1


print(find(data, 2))
print(find(data,4))
print(data)
