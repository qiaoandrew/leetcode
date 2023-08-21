def can_finish(num_courses, prerequisites):
    adjacency_list = {course: [] for course in range(num_courses)}
    indegrees = {course: 0 for course in range(num_courses)}

    for first, second in prerequisites:
        adjacency_list[first].append(second)
        indegrees[second] += 1
    
    stack = []
    for course in range(num_courses):
        if indegrees[course] == 0:
            stack.append(course)
    
    doable_courses = 0
    while stack:
        course = stack.pop()
        doable_courses += 1
        for neighbor in adjacency_list[course]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                stack.append(neighbor)
    
    return doable_courses == num_courses