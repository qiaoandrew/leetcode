from collections import defaultdict


# map each course to prerequisites
# loop through each course, dfs through
# dfs function will return whether or not the course can be taken
def can_finish(num_courses, prerequisites):
    course_to_prereqs = defaultdict(list)

    for course, prereq in prerequisites:
        course_to_prereqs[course].append(prereq)

    path = set()

    def dfs(course):
        if course in path:
            return False

        if course_to_prereqs[course] == []:
            return True

        path.add(course)

        for prereq in course_to_prereqs[course]:
            if not dfs(prereq):
                return False

        course_to_prereqs[course] = []

        path.remove(course)

        return True

    for course in range(num_courses):
        if not dfs(course):
            return False

    return True