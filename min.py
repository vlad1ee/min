a = [-1, -2, -6]
list1 = []
list2 = []
if max(a)<=0:
    print(1)
else:
    for i in range(min(a), max(a)+1):
        list2.append(i)
        if list2 == a:
            print(max(a) + 1)
        else:
            for i in range(min(a), max(a)):
                if i not in a:
                    list1.append(i)
    try:
        print(min(list1))
    except:
        print('')
