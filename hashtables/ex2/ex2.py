#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    hash_table = {}
    route = []

    for ticket in tickets:
        hash_table[ticket.source] = ticket.destination
        # {None:ord,
        #  ord:lga,
        #  lga:pga,
        #  pga, None}

    # set up while loop
    index = 0
    curr_dest = "NONE"

    while index < length:
        curr_dest = hash_table.get(curr_dest) # returns value {None:Value}
        route.append(curr_dest)               # append ^ value
        index += 1

    return route                              # return flight list

    '''
    While Loop makes sure the current is printed inline
    [None, curr_dest, curr_dest, curr_dest, curr_dest, curr_dest, None]
    '''
