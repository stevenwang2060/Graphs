from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Loop until we have visited each node.
visited = {}

# Keeps track of when player goes backwards.
go_backwards = []

# Create a compass of which way to go for each value.
backwards_compass = {
    'n': 's', 
    'e': 'w', 
    's': 'n', 
    'w': 'e'
}

# The player's location.
room_location = player.current_room.id

# Room index starting point, then add to visited.
visited[room_location] = player.current_room.get_exits()

# Loop through rooms that have not been visited.
while len(visited) < len(room_graph):

    # Starting point, not in visited rooms.
    if player.current_room.id not in visited:

        # Add to visited and get the next direction.
        visited[player.current_room.id] = player.current_room.get_exits()

        # After the room is visited, it needs to be removed.
        last_path = go_backwards[-1]
        visited[player.current_room.id].remove(last_path)

    # When all rooms are visited, stop the loop, and continue finding unvisited nodes.
    if len(visited[player.current_room.id]) == 0:

        # Until you find a room not visited.
        last_path = go_backwards[-1]

        # Remove from last PATH.
        go_backwards.pop()

        # Add to the previous.
        traversal_path.append(last_path)

        # Move player to unvisited node.
        player.travel(last_path)

    # Any exit left not taken.
    else:
        direction = visited[player.current_room.id][-1]

        # Take out of visited.
        visited[player.current_room.id].pop()

        # Add to traversal.
        traversal_path.append(direction)

        # Add backwards.
        go_backwards.append(backwards_compass[direction])

        # Move player to new room.
        player.travel(direction)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
