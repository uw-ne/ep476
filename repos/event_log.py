"""
This homework is based on the concept of an event log in a Monte Carlo
radiation transport application. In this kind of application, a particle moves
around a system colliding with the atoms in that system, losing energy, and
changing direction. Each of these collisions is an event and it is often
necessary to keep a log of these events.
"""

import math

# Q 3.ii) A dictionary is the best container to store an event because it
#         allows semantic information to be attached to the different kinds of
#         data.  It is also true that there is no implied order between the
#         different items, so that benefit of a list is not useful.
single_event = {
    'particleID' : 43,
    'loc'        : (3,4,5),
    'prev_loc'   : (8,1,2),
    'energy'     : 2.3,
    'target'     : {'Z' : 1, 'A' : 2},
    'rxn_code'   : 102
}

def distance(pos_A, pos_B):
    dist = 0
    for dim in len(pos_A):
        dist += (pos_A[dim] - pos_B[dim])**2
    return math.sqrt(dist)

def direction(pos_i, pos_f):
    dir = []
    dist = distance(pos_i,pos_f)
    for dim in len(pos_i):
        dir.append((pos_f[dim] - pos_i[dim])/dist)
    return dir

def convert_mev_ev(energy):
    return energy * 1e6


print("The particle traveled " + 
      str(distance(single_event['prev_loc'],single_event['loc'])) +
      " between collisions.")

print("The particle was traveling in the direction (u,v,w) = " + 
      str(direction(single_event['prev_loc'],single_event['loc'])) +
      " between collisions.")

print("The particle had energy " + 
      str(convert_mev_ev(single_event['energy'])) + 
      " eV prior to the collision.")


# Q 3.iii) A list is the best container to store a sequence of events because
#          each event is identical in structure and the order is usually
#          important.
event_log = []
# here is an example of a log with three identical events
event_log.append(single_event)
event_log.append(single_event)
event_log.append(single_event)

# assuming that we have an event_log with many entries....

# Q 3.iv.a
delta_E = event_log[5]['energy'] - event_log[4]['energy']

# Q 3.iv.b
dist = distance(event_log[7]['loc'], event_log[6]['loc'])

# Q 4.iv.c
if ( direction(event_log[3]['loc'],event_log[3]['prev_loc'])[2] >
     direction(event_log[8]['loc'],event_log[8]['prev_loc'])[2]   ):
    sort_by_alignment = (4,9)
else
    sort_by_alignment = (9,4)

print("The path to collision " + 
      str(sort_by_alignment[0]) + 
      " is more aligned with the z-axis than the path to collision " + 
      str(sort_by_alignment[2]))

