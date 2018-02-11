def draw_stars(inptlst):
    for x in range (0, len(inptlst)):
        const = ""
        if type(inptlst[x]) == int:                     #check if list item of input is type == integer
            for y in range (0, inptlst[x]):             #loop through the value of the integer, adding * to const for each iteration
                const += "*"
            print const                                 #print the resulting string
        elif isinstance(inptlst[x], str) == True:       #check if list item of input is type == string
            for z in range (0, len(inptlst[x])):        #loop over the length of the string, adding the first letter in the string to const for each iteration
                ltr = inptlst[x][0]
                const += ltr
            print const                                 #print the resulting string


#lst = [4, 6, 1, 3, 5, 7, 25]                       #test case defined
lst = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"] #test case defined

draw_stars(lst)
