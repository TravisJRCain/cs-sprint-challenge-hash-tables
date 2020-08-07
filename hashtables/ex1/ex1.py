def get_indices_of_item_weights(weights, length, limit):
    """
    Implement a function that finds two items whose sum of weights equals the weight limit.
    """
    # Your code here
    cache = {}

    for i in range(len(weights)):
        cache[weights[i]] = i

    for i in range(len(weights)):
        l_w = limit - weights[i]

        if l_w in cache:
            return(max(i, cache[l_w]), min(i, cache[l_w]))

    return None
