def findCharOccur(string):
    demodict = {}
    maximum = 0
    maxiKey = ""
    for i in range(len(string)):
        if string[i] in demodict:
            demodict[string[i]] = demodict[string[i]]+1;
        else:
            demodict.update({string[i]:1})
    # print(demodict)
    for key in demodict.keys():
        if demodict[key] > maximum:
            maximum = demodict[key];
            maxiKey = key
    return maxiKey;


string = "banana";
result = findCharOccur(string);
print(f"max char in '{string}' :",result);
# findCharOccur(string)
