def find_order(num_courses, prerequisites):
    adjacency_list = {course: [] for course in range(num_courses)}
    indegrees = {course: 0 for course in range(num_courses)}

    for course1, course2 in prerequisites:
        adjacency_list[course1].append(course2)
        indegrees[course2] += 1

    stack = []
    for course in range(num_courses):
        if indegrees[course] == 0:
            stack.append(course)

    order = []
    while stack:
        course = stack.pop()
        order.append(course)
        for neighbor in adjacency_list[course]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                stack.append(neighbor)
    
    return order if len(order) == num_courses else []