# data-archival

### ADF CI/CD Process

+ Workflow overview
  ![ADF github connection](https://github.com/calebu/adf_cicd/blob/main/documentation/workflow.png)
+ Initial setup (connecting the dev instance to the github repo)
  ![ADF Authoring](https://github.com/pointclickcare/data-archival/blob/main/documentation/adf-authoring.png)
+ ADF authoring
  ![ADF Authoring](https://github.com/pointclickcare/data-archival/blob/main/documentation/adf-authoring.png)
  - *feature branch creation*
  ![ADF Authoring](https://github.com/pointclickcare/data-archival/blob/main/documentation/adf-authoring.png)
  - *global parameters*
  ![ADF Authoring](https://github.com/pointclickcare/data-archival/blob/main/documentation/adf-authoring.png)
+ Pull Request
  ![ADF Authoring](https://github.com/pointclickcare/data-archival/blob/main/documentation/adf-authoring.png)
  - *Scenario 1 - PR is approved*
  ![ADF Authoring](https://github.com/pointclickcare/data-archival/blob/main/documentation/adf-authoring.png)
  - *Scenario 2 - Review is requested*
  ![ADF Authoring](https://github.com/pointclickcare/data-archival/blob/main/documentation/adf-authoring.png)
  - *Scenario 3 - PR is rejected*
  ![ADF Authoring](https://github.com/pointclickcare/data-archival/blob/main/documentation/adf-authoring.png)
+ Merge to master branch
  ![ADF Authoring](https://github.com/pointclickcare/data-archival/blob/main/documentation/adf-authoring.png)
  - *what happens in the background - github actions get triggered*
  ![ADF Authoring](https://github.com/pointclickcare/data-archival/blob/main/documentation/adf-authoring.png)
+ Prod Deployment
  ![ADF Authoring](https://github.com/pointclickcare/data-archival/blob/main/documentation/adf-authoring.png)
  - *Github actions listens on the creation of a release branch*
  ![ADF Authoring](https://github.com/pointclickcare/data-archival/blob/main/documentation/adf-authoring.png)


### [Footnotes](https://github.com/pointclickcare/data-archival/)

- All Integration Runtimes must be of the same type, else the deployment will fail link[^first].

[^first]: Valid IR types are: shared, Azure integration runtime, Self-hosted integration runtime, Azure-SQL Server Integration Services (SSIS) integration runtime