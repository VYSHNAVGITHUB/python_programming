l=[1,6,2,7,8,9,34,56,78,11,99,21]
def linearSearch(e):
    for i in l:
        if i==e:
            print("present")
            break
    else:
        print("not present")
linearSearch(99)
linearSearch(110)
