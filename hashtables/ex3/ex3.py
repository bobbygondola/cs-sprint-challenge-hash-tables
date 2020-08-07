def intersection(arrays):

    hash_table = {}
    results = []
    
    for array in arrays:
        for i in array:
            key = i
            if key not in hash_table:
                hash_table[key] = 1
            else:
                hash_table[key] += 1
                
    for i in hash_table:
        if hash_table[i] > 1:
            results.append(i)

    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
