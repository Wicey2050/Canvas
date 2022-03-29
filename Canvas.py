from canvasapi import Canvas

API_URL = "https://example.com"
API_KEY = "p@$$w0rd"

canvas = Canvas(API_URL, API_KEY)
user = canvas.get_user()
course = canvas.get_course()
courses = user.get_courses(enrollment_state='active')
assignment = course.get_assignment()
assignments = course.get_assignments()

upcomingassignments = 0

for assignment in assignments:
    status = [item.assignment['name'] for item in assignments if
               item.workflow_state == "upcoming" 
               ]
            
