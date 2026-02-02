def remove_consecutive_duplicates(x):
    if not x:
        return []
        
    result = [x[0]]  
    
    for i in range(1, len(x)):
        if x[i] != x[i - 1]:  
            result.append(x[i])
    
    return result

print(remove_consecutive_duplicates([1, 2, 2, 3, 3, 3, 2, 4]))
print(remove_consecutive_duplicates(["a","a", "c", "c", "a", "b", "b"]))
print(remove_consecutive_duplicates([7, 7, 7, 7]))
print(remove_consecutive_duplicates([]))
print(remove_consecutive_duplicates([1, 2, 3, 4]))