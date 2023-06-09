import sys, json
prev_commit = sys.argv[1].replace(sys.argv[3], '').split('\n')
new_commit = sys.argv[2].replace(sys.argv[4], '').split('\n')

compulsory_components = sys.argv[5].replace('\\"', '"')
s = compulsory_components.replace("{" ,"")
finalstring = s.replace("}" , "")

#Splitting the string based on , we get key value pairs
list = finalstring.split(",")

vars_ ={}
for i in list:
    #Get Key Value pairs separately to store in dictionary
    keyvalue = i.split(":")

    #Replacing the single quotes in the leading.
    m= keyvalue[0].strip().strip('\'')
    m = m.replace("\"", "")
    vars_[m] = keyvalue[1].strip().strip('\'').strip('\"').strip('"\'')

vars_ = json.loads(sys.argv[5])
pipeline_pattern = vars_['pipelines'] if 'pipelines' in vars_ else []
ir_pattern = vars_['integrationRuntimes'] if 'integrationRuntimes' in vars_ else []
triggers_pattern = vars_['triggers'] if 'triggers' in vars_ else []
linkedServices_pattern = vars_['linkedServices'] if 'linkedServices' in vars_ else []
datasets_pattern = vars_['datasets'] if 'datasets' in vars_ else []

s = set(new_commit)

dropped_pipelines = [x for x in prev_commit if x not in s and x.startswith(f'/pipeline/{pipeline_pattern}')]
dropped_IR = [x for x in prev_commit if x not in s and x.startswith(f'/integrationRuntime/{ir_pattern}')]
dropped_datasets = [x for x in prev_commit if x not in s and x.startswith(f'/datasets/{datasets_pattern}')]
dropped_linkedServices = [x for x in prev_commit if x not in s and x.startswith(f'/linkedService/{linkedServices_pattern}')]
dropped_triggers = [x for x in prev_commit if x not in s and x.startswith(f'/trigger/{triggers_pattern}')]

if len(dropped_pipelines) > 0:
  print(f'Merge blocked, the following compulsory pipelines were deleted {dropped_pipelines}')
if len(dropped_IR) > 0:
  print(f'Merge blocked, the following compulsory Integration Runtimes were deleted {dropped_IR}')
if len(dropped_datasets) > 0:
  print(f'Merge blocked, the following compulsory datasets were deleted {dropped_datasets}')
if len(dropped_linkedServices) > 0:
  print(f'Merge blocked, the following compulsory LinkedServices were deleted {dropped_linkedServices}')
if len(dropped_triggers) > 0:
  print(f'Merge blocked, the following compulsory triggers were deleted {dropped_triggers}')
