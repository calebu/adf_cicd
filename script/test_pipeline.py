import sys, json

class PipelineTester:
    STOP_DEPLOYMENT_ON_TEST_FAILURE = None

    REQUIRED_COMPONENTS = None
    jsonObj = None

    def __init__(self, STOP_DEPLOYMENT_ON_TEST_FAILURE, REQUIRED_COMPONENTS):
        self.STOP_DEPLOYMENT_ON_TEST_FAILURE = STOP_DEPLOYMENT_ON_TEST_FAILURE
        self.REQUIRED_COMPONENTS = REQUIRED_COMPONENTS

    def runChecks(self):
        try:
          self.jsonObj = json.loads(self.REQUIRED_COMPONENTS)
        except Exception as e:
          return False
    def requiredComponentsPresent(self):

    def runPipelineChecks(self):


"""
{
	"pipelines":
		[
			{ "name": "Data_Archival_Org_LookUp", "activities": [] }
		]
	"triggers": [],
	"integrationRuntimes": [],
	"linkedServices": [],
	"datasets": []
}
"""

pipelineTester = PipelineTester(sys.argv[1], sys.argv[2])
if pipelineTester.STOP_DEPLOYMENT_ON_TEST_FAILURE == True:
  return pipelineTester.runChecks()
return True



