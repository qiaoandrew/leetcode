def can_finish(num_courses, prerequisites):
    course_to_prereqs = {course: [] for course in range(num_courses)}

    for course, prereq in prerequisites:
        course_to_prereqs[course].append(prereq)

    cur_path = set()

    def dfs(course):
        if course in cur_path:
            return False
        elif course_to_prereqs[course] == []:
            return True

        cur_path.add(course)

        for prereq in course_to_prereqs[course]:
            if not dfs(prereq):
                return False

        cur_path.remove(course)

        course_to_prereqs[course] = []

        return True

    for course in range(num_courses):
        if not dfs(course):
            return False

    return True