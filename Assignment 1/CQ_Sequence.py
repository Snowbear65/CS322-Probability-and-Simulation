def num_seq(m, n):
    def next_num(x):
        result = []
        i = 0
        length = len(x)
        while i < length:
            count = 1
            while i + 1 < length and x[i] == x[i + 1]:
                i += 1
                count += 1
            result.append(str(count) + x[i])
            i += 1
        return ''.join(result)

    if not isinstance(m, int) or m < 1:
        raise ValueError("m must be an positive integer")
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a integer")

    z = []
    curr = str(m)
    for _ in range(n):
        curr = next_num(curr)
        z.append(int(curr))
    return z

print(num_seq(1, 4))   
print(num_seq(11, 3)) 
print(num_seq(5, 4))   
print(num_seq(2, 5)) 
