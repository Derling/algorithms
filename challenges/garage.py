# There is a parking lot with only one empty spot. Given the initial state
# of the parking lot and the final state. Each step we are only allowed to
# move a car
# out of its place and move it into the empty spot.
# The goal is to find out the least movement needed to rearrange
# the parking lot from the initial state to the final state.

# Say the initial state is an array:

# [1,2,3,0,4],
# where 1,2,3,4 are different cars, and 0 is the empty spot.

# And the final state is

# [0,3,2,1,4].
# We can swap 1 with 0 in the initial array to get [0,2,3,1,4] and so on.
# Each step swap with 0 only.

def garage(initial, final):
    steps = 0
    current = 0
    while initial != final:
        if initial[current] != final[current]:
            empty_spot = initial.index(0)
            final_spot = initial.index(final[current])
            
            if final_spot == empty_spot:
                initial[current], initial[empty_spot] = \
                    initial[empty_spot], initial[current]
                steps = steps + 1
            
            else:
                initial[current], initial[empty_spot] = \
                    initial[empty_spot], initial[current]
                initial[current], initial[final_spot] = \
                    initial[final_spot], initial[current]
                steps = steps + 2
        current = current + 1
    return steps

if __name__ == '__main__':
    initial, final = [1, 2, 3, 0, 4], [0, 3, 2, 1, 4]
    print(garage(initial, final))
'''
[1, 2, 3, 0, 4]      [0, 3, 2, 1, 4]
[0, 2, 3, 1, 4]      switch 0 with 3
[2, 0, 3, 1, 4]      switch 0 with 1
[2, 3, 0, 1, 4]      switch 1 with 2
[0, 3, 2, 1, 4]      switch 2 with 0
[0, 3, 2, 1, 4]      DONE!

                                algorithm
check if the ith car is in the correct place, intial[0] == final[0]
find the final position for the current car and the empty position
check if the final position is empty, if so move the car to that position
else make the position empty by moving the car there to the empty position
finally move the current car to its final position
look at the next car and repeat
'''
