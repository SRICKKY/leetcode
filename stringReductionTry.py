def stringReduction(string):
    
    count = 0
    while len(string) > 0:

        for i in range(len(string)):
            if i + 1 < len(string) and string[i] != string[i+1]:
                if string[i] == "a":
                    if string[i+1] == "b":
                        string = "c" + string[i+1:]
                    if string[i+1] == "c":
                        string = "b" + string[i+1:]

                if string[i] == "b":
                    if string[i+1] == "a":
                        string = "c" + string[i+1:]
                    if string[i+1] == "c":
                        string = "a" + string[i+1:]

                if string[i] == "c":
                    if string[i+1] == "a":
                        string = "b" + string[i+1:]
                    if string[i+1] == "b":
                        string = "a" + string[i+1:]
            # print(string)
    
    print(len(string))

stringReduction("cab")
stringReduction("bcab")
stringReduction("ccccc")