from collections import defaultdict


# map course to list of prerequisites
# loop through each course and dfs on it
# dfs returns whether or not a course is reachable
def find_order(num_courses, prerequisites):
    course_to_prereq = defaultdict(list)

    for course, prereq in prerequisites:
        course_to_prereq[course].append(prereq)

    order = []
    visited = set()
    path = set()

    def dfs(course):
        if course in visited:
            return True
        elif course in path:
            return False

        path.add(course)

        for prereq in course_to_prereq[course]:
            if not dfs(prereq):
                return False

        order.append(course)
        path.remove(course)
        visited.add(course)

        return True

    for course in range(num_courses):
        if not dfs(course):
            return []

    return order