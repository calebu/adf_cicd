import sys, json
pr_comment = sys.argv[1]
valid_statuses = ['In Progress', 'In Development']

f = open('./main/script/jira_tickets.json')

data = json.load(f)
print(f'Argument is {pr_comment}')
#Find the ticket and status

for i in data:
    if i['ticket'] == pr_comment and i['status'] in valid_statuses:
        print(0)
        exit()
    
f.close()
print(1)
