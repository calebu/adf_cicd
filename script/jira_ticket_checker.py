import sys, json
pr_comment = sys.argv[1]
valid_statuses = ['In Progress', 'In Development']

f = open('jira_tickets.json')

data = json.load(f)

for i in data:
	if i['ticket'] == pr_comment and i['status'] in valid_statuses:
		print(0)
	
	if i['ticket'] == pr_comment:
		print(f'Status: {i["status"]}')
	
f.close()
print(1)
