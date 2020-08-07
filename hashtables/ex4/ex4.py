# cache = {}

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    hash_table = {}
    results = []
    
    # if a not in cache:
    #     cache[a] = has_negatives(a)
    
    for i in a:
        absolute = abs(i)
        print(absolute)
        
        if hash_table.get(absolute) is not None:
            results.append(absolute)
        else:
            hash_table[absolute] = absolute
            
    return results


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    print(has_negatives([5,-5,6,-6,7,8]))
