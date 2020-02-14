#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    #Add weights to hash table with key = weight and value = index {weight: index}
    for index in range(length):
        item = weights[index]
        hash_table_insert(ht, key = item, value = index)

    #loop through weights
    for index in range(length):
        item = weights[index]
        if item < limit:
            #Finding the "complement"
            item_pair = limit - item
            item_pair_index = hash_table_retrieve(ht, item_pair)
            
            #if index is None, continue
            if item_pair_index is None:
                continue
            elif item_pair_index >= 0 and item_pair_index != index:
                if item_pair_index >= index:
                    return (item_pair_index, index)
                else:
                    return (index, item_pair_index)

    return None


"""
Given a package with a weight limit `limit` and a list `weights` of item weights, implement a function `get_indices_of_item_weights` that finds two items whose sum of weights equals the weight limit `limit`. Your function will return an instance of an `Answer` tuple that has the following form:
```
(zero, one)
```
"""

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
