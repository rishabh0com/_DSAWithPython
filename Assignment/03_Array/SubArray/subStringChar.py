def subStrUnderCond(s):
    pattern = "";
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            pattern = ""
            for k in range(i,j+1):
                pattern += s[k];
            # print(pattern);
            if pattern[0] == pattern[len(pattern)-1]:
                print(pattern)

subStrUnderCond("abcab")
