import sys
prev_commit = sys.argv[1].replace(sys.argv[3], '').split('\n')
new_commit = sys.argv[2].replace(sys.argv[4], '').split('\n')

vars_ = json.load(sys.argv[5])
print(json.dumps(vars_))

s = set(new_commit)
dropped_pipelines = [x for x in prev_commit if x not in s and x.startswith("/pipeline/Data_Archival")]
dropped_IR = [x for x in prev_commit if x not in s and x.startswith("/integrationRuntime/")]
dropped_datasets = [x for x in prev_commit if x not in s and x.startswith("/dataset/")]
dropped_linkedServices = [x for x in prev_commit if x not in s and x.startswith("/linkedService")]
dropped_factory = [x for x in prev_commit if x not in s and x.startswith("/factory/")]


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
