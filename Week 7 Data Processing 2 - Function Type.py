def courses_sorted_by_enrollment(student_courses: dict) -> list:
    '''
    Given a dictionary of student roll numbers 
    with the list of courses they chose, 
    find the courses sorted from the 
    most number of enrollments to the least.

    Assume no courses will have the same number of students enrolled.

    Args:
    student_courses (dict): 
        A dictionary where keys are student roll numbers and 
        values are lists of courses they chose.

    Returns:
    list: 
        A list of courses sorted by the number of students enrolled 
        in descending order.
    '''
    # Initialize a dictionary to track the enrollment count for each course
    course_enrollment = {}

    # Iterate through each student and their chosen courses
    for courses in student_courses.values():
        for course in courses:
            if course in course_enrollment:
                course_enrollment[course] += 1
            else:
                course_enrollment[course] = 1

    # Sort courses by enrollment count in descending order
    sorted_courses = sorted(course_enrollment.keys(), key=lambda course: course_enrollment[course], reverse=True)

    return sorted_courses
