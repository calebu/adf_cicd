import sys, json
pr_comment = sys.argv[1].strip()
valid_statuses = ['In Progress', 'In Development']

f = open('./main/jira_validator_script/jira_tickets.json')

data = json.load(f)
#Find the ticket and status

for i in data:
    if i['ticket'] in pr_comment and i['status'] in valid_statuses:
        print("")
        exit()
    
f.close()
print(f"JIRA ticket {pr_comment} not found, or JIRA ticket not in Progress/Development state")


