def reverse_string(s, k):
    toList = list(s)

    for i in range(0,len(toList), 2*k):
        toList[i:i+k] = reversed(toList[i:i+k])
    "".join(toList)
    return toList
    
    
    
print(reverse_string("abcdefg", 2))