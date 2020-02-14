#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    #insert all tickets onto the ht
    for ticket in tickets:
        hash_table_insert(hashtable, key = ticket.source, value = ticket.destination)

    #Value of Ticket of NONE - ie first ticket's value
    stack = [hash_table_retrieve(hashtable, "NONE")]
    #Used to replace destination in route
    index_count = 0
    while len(stack) > 0:
        current_destination = stack.pop(0)

        #Add first dest to route
        route[index_count] = current_destination
        index_count += 1
        
        next_destination = hash_table_retrieve(hashtable, current_destination)
        #making it so the stack ends when we're at the last dest
        if next_destination is not "NONE":
            stack.append(next_destination)
    
    #exlucindg last None value
    return route[:-1]
