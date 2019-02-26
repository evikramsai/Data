def max_in_list(listname) :
    max = listname[0]
    for i in listname :
        if i > max :
            max = i
    print("Greatest number is ",max)
listnamex = [8,2,7,4,9]
max_in_list(listnamex)
