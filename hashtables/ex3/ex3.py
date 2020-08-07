def intersection(arrays):
'''
Finding duplicated, KVP =+ 1 on each occurence
'''
    hash_table = {}
    results = []
    
    for array in arrays:
        for i in array:
            num = i
            if num not in hash_table:
                hash_table[num] = 1
            else:
                '''
                if already in, gets incremented..
                '''
                hash_table[num] += 1
                
    for i in hash_table:
        if hash_table[i] > 1:
            '''
            send the duplicates
            '''
            results.append(i)

    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
