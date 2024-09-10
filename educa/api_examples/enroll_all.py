import requests

username = 'a'  # Replace with your actual username
password = '1'  # Replace with your actual password

base_url = 'http://127.0.0.1:8000/api/'
url = f'{base_url}courses/'
available_courses = []
courses = []  # Initialize courses outside the loop

while url is not None:
    print(f'Loading courses from {url}')
    try:
        # Ensure the get request uses authentication
        r = requests.get(url, auth=(username, password))
        r.raise_for_status()  # Raise an error for bad responses
        response = r.json()

        # Check if 'next' and 'results' are present in the response
        url = response.get('next')
        new_courses = response.get('results', [])
        courses.extend(new_courses)  # Store all courses data
        available_courses += [course['title'] for course in new_courses]

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        break  # Stop the loop in case of an error

print(f'Available courses: {", ".join(available_courses)}')

# Iterate over courses for enrollment
for course in courses:
    course_id = course['id']
    course_title = course['title']
    try:
        # Make a post request to enroll in the course
        r = requests.post(
            f'{base_url}courses/{course_id}/enroll/',
            auth=(username, password)
        )
        if r.status_code == 200:
            print(f'Successfully enrolled in {course_title}')
        else:
            print(f'Failed to enroll in {course_title}: {r.status_code} {r.text}')

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while enrolling in {course_title}: {e}")
