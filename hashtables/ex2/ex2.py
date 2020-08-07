#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Output an array of strings with the entire route of your trip.
    """
    # Your code here

    route = [None] * length

    cache = {}

    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    nxt = cache['NONE']

    for i in range(0, length):
        route[i] = nxt
        nxt = cache[nxt]

    return route
