import sys, json
branch_name = sys.argv[1].strip()
valid_statuses = ['In Progress', 'In Development']

f = open('./json-file-repo/jira_tickets.json')

data = json.load(f)
#Find the ticket and status

for i in data:
    if i['ticket'] in branch_name and i['status'] in valid_statuses:
        print("")
        exit()
    
f.close()
print(f"JIRA ticket {branch_name} not found, or JIRA ticket not in Progress/Development state")


