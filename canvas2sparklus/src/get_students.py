import json
import requests
import click


URL = "https://rmit.instructure.com:443/api/v1"
EMAIL_SUFFIX="@student.rmit.edu.au"


def handleResponse(students, seen):
    for student in students.json():  
        try:  
            user = student['user']
            lastname, firstname = user['sortable_name'].split(', ')
            account_id = user['login_id'].lower()
            email = "{}{}".format(account_id, EMAIL_SUFFIX).lower()
            is_active = student['enrollment_state'] == 'active'
            try:
                if account_id not in seen and account_id.startswith('s') and is_active:
                    print(*[firstname, lastname, account_id, email], sep="\t")
                    seen.add(account_id)
            except TypeError:
                continue
        except TypeError:
            continue
    return seen

@click.command()
@click.argument('access_token_file', type=click.File('r'))
@click.argument('course_id')
def run(access_token_file, course_id):
    
    access_token = access_token_file.readline()

    REQUEST = "{}/courses/{}/enrollments?access_token={}&per_page=50".format(URL, course_id,access_token)
    students = requests.get(REQUEST) 

    if (students.status_code==200):
        seen = set()
        head = ["FirstName", 'LastName', 'AccountID', 'Email']

        print(*head, sep="\t")

        # First page:
        seen = handleResponse(students, seen)

    # Subsequent pages
    while 'next' in students.links:
        students = requests.get("{}&access_token={}".format(students.links['next']['url'], access_token))
        seen = handleResponse(students, seen)


if __name__ == '__main__':
    run()
