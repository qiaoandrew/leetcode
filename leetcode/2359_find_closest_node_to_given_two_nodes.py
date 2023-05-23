from collections import deque


# traverse the graph from node1, keeping track of each node and its distance from node1 in a hashmap
# traverse the graph from node2, keeping track of each node and its distance from node2 in a hashmap
# loop through all nodes,
def closest_meeting_node(edges, node1, node2):

    def get_distances(start_node):
        distance_from_start = {}

        cur_node = start_node
        cur_distance = 0

        while cur_node != -1 and cur_node not in distance_from_start:
            distance_from_start[cur_node] = cur_distance
            cur_node = edges[cur_node]
            cur_distance += 1

        return distance_from_start

    distance_from_node1 = get_distances(node1)
    distance_from_node2 = get_distances(node2)

    closest_distance = float('inf')
    closest_meeting_node = -1

    for node in range(len(edges)):
        if node in distance_from_node1 and node in distance_from_node2 and max(
                distance_from_node1[node],
                distance_from_node2[node]) < closest_distance:
            closest_distance = max(distance_from_node1[node],
                                   distance_from_node2[node])
            closest_meeting_node = node

    return closest_meeting_node


print(closest_meeting_node([2, 2, 3, -1], 0, 1))
print(closest_meeting_node([1, 2, -1], 0, 2))
print(closest_meeting_node([4, 4, 4, 5, 1, 2, 2], 1, 1))
