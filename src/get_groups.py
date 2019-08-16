import json
import requests
import click 

#live API: https://rmit.instructure.com/doc/api/live
URL = "https://rmit.instructure.com:443/api/v1"

def handleResponse(groups, access_token):
    for group in groups.json():
        group_id = group.get('id')
        group_name = group.get('name')
        get_group_users=URL+"/groups/"+str(group_id)+"/users?access_token="+access_token
        users = requests.get(get_group_users)
        
        for user in users.json():
            user_id = user.get('id')
            get_profile = URL+"/users/"+str(user_id)+"/profile?access_token="+access_token
            profile = requests.get(get_profile).json()
            user_name = profile.get('sortable_name')
            login_id = profile.get('login_id').lower()
            try:
                print(*[login_id, group_name], sep="\t")
            except TypeError:
                continue


@click.command()
@click.argument('access_token_file', type=click.File('r'))
@click.argument('group_set_id')
def run(access_token_file, group_set_id):
    
 
    access_token = access_token_file.readline()
    
    get_groups = URL+"/group_categories/"+str(group_set_id)+"/groups?access_token="+access_token +"&per_page=50"
    groups=requests.get(get_groups)
    if (groups.status_code==200):
        header = ["AccountId","GroupName"]
        print(*header, sep="\t")
    
        # First page:
        handleResponse(groups, access_token)

        # Subsequent pages
        while 'next' in groups.links:
            groups = requests.get("{}&access_token={}".format(groups.links['next']['url'], access_token))
            handleResponse(groups, access_token)

if __name__ == '__main__':
    run()