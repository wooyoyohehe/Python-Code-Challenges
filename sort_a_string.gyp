def sort_string(str):
    list1 = []
    list1 = str.split( )
    for i in range(0,len(list1)):
        list1[i] =  list1[i].lower() + list1[i]
    list1.sort()
    print list1
    for i in range(0,len(list1)):
        list1[i] = list1[i][len(list1[i])/2:]
        print list1[i]
    print list1

sort_string('Hello you Are a motherfucker')

