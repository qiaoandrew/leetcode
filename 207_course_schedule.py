def can_finish(num_courses, prerequisites):
    course_to_prereqs = {course: [] for course in range(num_courses)}

    for course, prereq in prerequisites:
        course_to_prereqs[course].append(prereq)

    visiting = set()

    def dfs(course):
        if course in visiting:
            return False

        if len(course_to_prereqs[course]) == 0:
            return True

        visiting.add(course)

        for prereq in course_to_prereqs[course]:
            if not dfs(prereq):
                return False

        visiting.remove(course)

        course_to_prereqs[course] = []

        return True

    for course in range(num_courses):
        if not dfs(course):
            return False

    return True


print(can_finish(2, [[1, 0]]))
