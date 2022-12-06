'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.  
    social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}
    
    fromMember_following = social_graph.get(from_member, {}).get('following')
    toMember_following = social_graph.get(to_member, {}).get('following')
    print(fromMember_following)
    print(toMember_following)

    if to_member in fromMember_following:
        status = "Follower"
        if from_member in toMember_following:
           status = "Followed by"
           if to_member in fromMember_following and from_member in toMember_following:
              status = "Friends"
        print(status)
        return status

    
    elif from_member in toMember_following:
        status = "Followed by"
        if to_member in fromMember_following and from_member in toMember_following:
           status = "Friends"
        print(status)
        return status
    
    elif to_member in fromMember_following and from_member in toMember_following:
        status = "Friends"
        print(status)
        return status
        
    
    else:
        status = "No relationship"
        print(status)
        return status
    

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    lengthlist=board[0]
    k=len(lengthlist)
    i=0
    j=0
    issame='false'
    for i in range(k):
        prevval=board[i][j]
        for j in range (1,k):
            curval=board[i][j]
            if prevval == curval:
                issame='true'
            else:
                issame='false'
                break
            prevval=curval
        if issame=='true':
            print('WINNER')
            return

        j=0

    i=0
    j=0
    issame='false'
    for j in range (k):
        prevval=board[i][j]
        for i in range (1,k):
            curval=board[i][j]
            if prevval == curval:
                issame='true'
            else:
                issame='false'
                break
            prevval=curval
        if issame=='true':
            print('WINNER')
            return
        j=0    

    i=0
    j=0
    issame='false'
    prevval=board[i][j]
    for i in range (k):
        if i != k:
            i=i+1
        else:
            break
        if i == k:
            break
        curval=board[i][i]
        if prevval == curval:
                issame='true'
        else:
                issame='false'
                break
        prevval=curval
    if issame=='true':
        print('WINNER')
        return

    i=0
    j=k-1
    issame='false'
    prevval=board[i][j]
    while  j != 0 :
        j=j-1
        i=i+1
        curval=board[i][j]
        if prevval == curval:
                issame='true'
        else:
                issame='false'
                break
        prevval=curval
    if issame=='true':
        print('WINNER')
        return
    else:
        issame=='false'
        print('NO WINNER')

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','','X'],
]

board3 = [
['X','X','O'],
['','O','X'],
['O','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]


def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    totaltime = 0
    quest = (first_stop, second_stop)
    Fstop = 'no'
    Sstop = 'no'
    if quest in route_map:
        legtime = route_map.get(quest)
        legitem = legtime.get('travel_time_mins')
        print (legitem)
    else:
       
        tkeylist = list(route_map.keys())
        tkeylisttype = type(tkeylist)
       
        noKeys = len(tkeylist)
        for i in range(noKeys):
            tkeysubtup = tkeylist[i]
            toneval = tkeysubtup[0]
            tsecval = tkeysubtup[1]
            tquest = (toneval, tsecval)
            legtime = route_map.get(tquest)
            legitem = legtime.get('travel_time_mins')
            mintime = list(legtime)
            mintype = type(mintime)
            if toneval == first_stop :
                Fstop = 'yes'
                totaltime = totaltime + legitem
            if tsecval == second_stop :
                Sstop = 'yes'
                totaltime = totaltime + legitem
            if Fstop == 'yes'and Sstop == 'yes' :
                break
    
        print(totaltime)
        return(totaltime)
UNILEGS = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

GENLEGS = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}

