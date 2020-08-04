import click 
import pandas as pd
import sys


@click.command()
@click.argument('student_list', type=click.File('r'))
@click.argument('group_list', type=click.File('r'))
def numGroups(student_list, group_list):
    students = pd.read_csv(student_list, sep ='\t')
    groups = pd.read_csv(group_list, sep = '\t')
    
    #table(student id) in groups
    assigned = groups.AccountId.value_counts().rename_axis('AccountId').reset_index(name='counts')
    #print(assigned)

    #students not in assigned.AccountId
    unassigned = pd.DataFrame(students.AccountId[~students.AccountId.isin(assigned.AccountId)].dropna())
    unassigned['counts'] = 0
    #print(unassigned.columns)
    #unassigned = pd.DataFrame(unassigned)

    all  = pd.concat([assigned, unassigned])
    all.to_csv(sys.stdout,sep='\t',index=False)


if __name__ == "__main__":
    numGroups()


