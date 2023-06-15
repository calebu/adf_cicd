import sys, json
prev_commit = sys.argv[1].replace(sys.argv[3], '').split('\n')
new_commit = sys.argv[2].replace(sys.argv[4], '').split('\n')

print(sys.argv[5])
print(sys.argv[5].replace('\\"', "'").replace('"', ""))
vars_ = json.loads(sys.argv[5].replace('\\"', "'").replace('"', ""))
print(vars_)
#print(vars_["pipelines"])

"""
print(json.dumps(vars_))
print(vars_['pipelines'])

pipeline_pattern = vars_['pipelines'] if 'pipelines' in vars_ else []
ir_pattern = vars_['integrationRuntimes'] if 'integrationRuntimes' in vars_ else []
triggers_pattern = vars_['triggers'] if 'triggers' in vars_ else []
linkedServices_pattern = vars_['linkedServices'] if 'linkedServices' in vars_ else []
datasets_pattern = vars_['datasets'] if 'datasets' in vars_ else []

print(pipeline_pattern, ir_pattern, triggers_pattern, linkedServices_pattern, linkedServices_pattern)

s = set(new_commit)

dropped_pipelines = []
for a_pattern in pipeline_pattern:
  dropped_pipelines = dropped_pipelines + [x for x in prev_commit if x not in s and x.startswith("/pipeline/" + a_pattern)]

dropped_IR = []
for a_pattern in pipeline_pattern:
  dropped_IR = dropped_IR + [x for x in prev_commit if x not in s and x.startswith("/integrationRuntime/" + a_pattern)]

dropped_triggers = []
for a_pattern in pipeline_pattern:
  dropped_triggers = dropped_triggers + [x for x in prev_commit if x not in s and x.startswith("/triggers/" + a_pattern)]

dropped_datasets = []
for a_pattern in pipeline_pattern:
  dropped_datasets = dropped_datasets + [x for x in prev_commit if x not in s and x.startswith("/datasets/" + a_pattern)]

dropped_linkedServices = []
for a_pattern in pipeline_pattern:
  dropped_linkedServices = dropped_linkedServices + [x for x in prev_commit if x not in s and x.startswith("/linkedService/" + a_pattern)]


print(dropped_IR, dropped_datasets, dropped_linkedServices, dropped_factory)

#dropped_IR = [x for x in prev_commit if x not in s and x.startswith("/integrationRuntime/")]
#dropped_datasets = [x for x in prev_commit if x not in s and x.startswith("/datasets/")]
#dropped_linkedServices = [x for x in prev_commit if x not in s and x.startswith("/linkedService")]
#dropped_factory = [x for x in prev_commit if x not in s and x.startswith("/factory/")]


if len(dropped_pipelines) > 0:
  print(f'Merge blocked, the following compulsory pipelines were deleted {dropped_pipelines}')
if len(dropped_IR) > 0:
  print(f'Merge blocked, the following compulsory Integration Runtimes were deleted {dropped_IR}')
if len(dropped_datasets) > 0:
  print(f'Merge blocked, the following compulsory datasets were deleted {dropped_datasets}')
if len(dropped_linkedServices) > 0:
  print(f'Merge blocked, the following compulsory LinkedServices were deleted {dropped_linkedServices}')
if len(dropped_factory) > 0:
  print(f'Merge blocked, the following compulsory Data Factory resource were deleted {dropped_factory}')
"""
