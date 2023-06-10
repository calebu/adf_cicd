import sys, json, os, logging

log = logging.getLogger(__name__)

class PipelineTester:
    BASE_DIR = None
    STOP_DEPLOYMENT_ON_TEST_FAILURE = None
    REQUIRED_COMPONENTS = None
    MOCK_DATASETS = None
    jsonObj = None

    def __init__(self, STOP_DEPLOYMENT_ON_TEST_FAILURE, REQUIRED_COMPONENTS, BASE_DIR = './', MOCK_DATASETS = None):
        self.STOP_DEPLOYMENT_ON_TEST_FAILURE = STOP_DEPLOYMENT_ON_TEST_FAILURE
        self.REQUIRED_COMPONENTS = REQUIRED_COMPONENTS
        self.MOCK_DATASETS = MOCK_DATASETS
        self.BASE_DIR = BASE_DIR

    def runChecks(self):
        try:
          self.jsonObj = json.loads(self.REQUIRED_COMPONENTS)
        except Exception as e:
          return False
    def areActivitiesPresent(self, requiredActivities, ADFjsonObj):
        for aRequiredActivity in requiredActivities:
            if ADFjsonObj['properties'] and ADFjsonObj['properties']['activities']:
                activityFound = False
                for anActivity in ADFjsonObj['properties']['activities']:
                    if aRequiredActivity == ADFjsonObj['name']: activityFound = True
                if activityFound == False: 
                    log.error("Activity %s not found" % aRequiredActivity)
                    return False
            else:
                log.error("No pipelines/activities found in json file")
                return False
            
        
    def areJsonfilesPresent(self, componentType):
        # Check if required component type is in place
        for aComponent in self.jsonObj[componentType]:
            componentName = aComponent['name'] if componentType == 'pipeline' else aComponent
            if not os.path.exists(self.BASE_DIR + f"{componentType}/" + componentName + '.json'):    # If component file doesnt exist
                log.error("%s %s does not exist, test failed" % (componentType, componentName))
                return False
            # If this is a pipeline, check if activities are present
            if componentType == 'pipeline':
                pipelineJson = None
                with open(self.BASE_DIR + 'pipeline/' + aPipeline['name'] + '.json') as file:
                    pipelineJson = f.read()
                ADFjsonObj = json.loads(pipelineJson)
                areActivitiesPresent(aComponent['activities'], ADFjsonObj)
            
        
    def requiredComponentsPresent(self):
        # Check if required pipelines, activities are in place
        if self.jsonObj['pipelines']:
            areJsonfilesPresent('pipelines')
        # Check if triggers are in place
        if self.jsonObj['triggers']:
            areJsonfilesPresent('triggers')
        # Check if integrationRuntimes are in place
        if self.jsonObj['integrationRuntimes']:
            areJsonfilesPresent('integrationRuntimes')
        # Check if linkedServices are in place
        if self.jsonObj['linkedServices']:
            areJsonfilesPresent('linkedServices')
        # Check if datasets are in place
        if self.jsonObj['datasets']:
            areJsonfilesPresent('datasets')
        
    def stubDBCalls(self):
        if not MOCK_DATASETS == None:
            for aMock in requiredActivities:
                try:
                    objToReplace = None
                    with open(self.BASE_DIR + aMock['type'] + '/' + aMock['type'] + '.json') as file:
                        objToReplace = f.read()
                    objToReplace = json.loads(objToReplace)
                    stubPath = aMock['type'].split('/')
                    for pathItem in stubPath:
                        if '[' in y: y = int(y.replace('[', '').replace(']', ''))   #Extract integer indices
                    
                    
                except Exception as e:
                
            # end for
        # end if

    def runPipelineChecks(self):


pipelineTester = PipelineTester(False, '{"pipelines":[{"name":"Data_Archival_Org_LookUp","activities":[]}]"triggers":[],"integrationRuntimes":[],"linkedServices":[],"datasets":[]}')
if pipelineTester.STOP_DEPLOYMENT_ON_TEST_FAILURE == True:
  return pipelineTester.runChecks()
return True



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

stub: [
        {"type" : "pipeline", "name" : "Data_Archival_Org_LookUp", "path" : "resources/properties/activities/[1]/typeProperties/items/value", "replacement_variable" : ""},
        {},
    
    ]


Must not be deleted:
data_archival
global parameters
IR, linkeservices and datasets 
"""
