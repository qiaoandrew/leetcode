def find_order(num_courses, prerequisites):
    course_to_prereqs = {course: [] for course in range(num_courses)}

    for course, prereq in prerequisites:
        course_to_prereqs[course].append(prereq)

    order = []
    cur_path = set()
    visited = set()

    def dfs(course):
        if course in cur_path:
            return False
        elif course in visited:
            return True

        cur_path.add(course)

        for prereq in course_to_prereqs[course]:
            if not dfs(prereq):
                return False

        cur_path.remove(course)

        visited.add(course)

        order.append(course)

        return True

    for course in range(num_courses):
        if not dfs(course):
            return []

    return order