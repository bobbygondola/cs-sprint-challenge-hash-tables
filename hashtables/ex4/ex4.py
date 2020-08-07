# cache = {}

def has_negatives(a):
    """
    using absolute value to find duplicates,
    level the playing field
    """
    hash_table = {}
    results = []
    
    # if a not in cache:
    #     cache[a] = has_negatives(a)
    
    for i in a:
        absolute = abs(i)
        # print(f"All values absolute -> {absolute}")
        
        if hash_table.get(absolute) is not None: # Value - None to start, will append.
            results.append(absolute)
            # print(f'mid append -> {results}')
        else:
            hash_table[absolute] = absolute
            print(f"hash_table -> {hash_table}")
            
    return results


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    print(has_negatives([5,-5,6,-6,7,8]))
