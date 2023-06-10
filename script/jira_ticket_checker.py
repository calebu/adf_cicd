import sys, json
pr_comment = sys.argv[1]
valid_statuses = ['In Progress', 'In Development']

f = open('./main/script/jira_tickets.json')

data = json.load(f)

#Find the ticket and status

print(f'Ticket Arg: {pr_comment}')

for i in data:
    print(f'Ticket: {i["ticket"]}, Status: {i["status"]}')
    if i['ticket'] == pr_comment and i['status'] in valid_statuses:
        print(0)
        exit()
    
f.close()
print(1)
