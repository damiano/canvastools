# canvas2sparkplus
A set of Python3 scripts to generate student and group lists from Canvas that can be easily uploaded to SPARPLUS.

**IMPORTANT: A valid Canvas access token is required to use the scripts.**

**NOTE:** This scripts have been tested using `Python 3.7.2`. Use `pip install -r requirements.txt` to install required packages.

# Obtaining an access token:
You can create a Canvas access tokens from your profile's *Settings* on Canvas, e.g., [https://rmit.instructure.com/profile/settings](https://rmit.instructure.com/profile/settings).

For more information, check out [this link](https://community.canvaslms.com/docs/DOC-10806-4214724194).

# Extracting list of enrolled (active) students:

```python src/get_students.py my_access_token.txt COURSE_ID > students.txt```

where:
- `my_access_token.txt`: Text file including your Canvas API access token.
- `COURSE_ID`: Course ID of the course you want to extract the student list from. You can find the Course ID in the URL of your Canvas course.
- `students.txt`: Output file. This is the file with the list of students you would upload to SPARKPLUS.


# Extracting group set IDs in a course

```python src/get_group_sets.py my_access_token.txt COURSE_ID > group_sets.txt```

where:
- `my_access_token.txt`: Text file including your Canvas API access token.
- `COURSE_ID`: Course ID of the course you want to extract the student list from. You can find the Course ID in the URL of your Canvas course.
- `group_sets.txt`: Output file. Each line correspond to one group set, and contains the group set ID, the name of the group set as shown on Canvas, and the role (if any) of the group set.


# Extracting list of groups

```python src/get_groups.py my_access_token.txt GROUP_SET_ID > groups.txt```

where:
- `my_access_token.txt`: Text file including your Canvas API access token.
- `GROUP_SET_ID`: Group set ID from which you want to extract the groups. You can find the Group Set ID in the Canvas URL of the group set.
- `groups.txt`: Output file. This is the file with the groups you would upload to SPARKPLUS.


# Canvas API Documentation
https://canvas.instructure.com/doc/api/


# Disclaimer

I wrote these scripts for personal use, and there is no guarantee that are free of bugs. However, I thought are worth sharing, as other people at RMIT may find it useful. Please feel free to contribute and create pull requests to improve/extend these scripts!


# Things to improve
 - Remove hardcoded RMIT links/email suffix.
 - Improve error handling.
