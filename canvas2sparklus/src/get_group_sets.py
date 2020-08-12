import json
import requests
import click 

#live API: https://rmit.instructure.com/doc/api/live
URL = "https://rmit.instructure.com:443/api/v1"

def handleResponse(group_sets, access_token):
    for group_set in group_sets.json():
        group_set_id = group_set.get('id')
        group_set_name = group_set.get('name')
        group_set_role = group_set.get("role")
        print(*[group_set_id, group_set_name, group_set_role], sep="\t")
        

@click.command()
@click.argument('access_token_file', type=click.File('r'))
@click.argument('course_id')
def run(access_token_file, course_id):
    
 
    access_token = access_token_file.readline()
    
    get_group_sets = URL+"/courses/"+str(course_id)+"/group_categories?access_token="+access_token +"&per_page=50"
    # print(get_group_sets)
    group_sets=requests.get(get_group_sets)
    if (group_sets.status_code==200):
        header = ["GroupSetID", "GroupSetName", "GroupSetRole"]
        print(*header, sep="\t")
    
        # First page:
        handleResponse(group_sets, access_token)

        # Subsequent pages
        while 'next' in group_sets.links:
            group_sets = requests.get("{}&access_token={}".format(group_sets.links['next']['url'], access_token))
            handleResponse(group_sets, access_token)

if __name__ == '__main__':
    run()
