# application
## AWS Amplify 
- ```create new app```
- ```Deploy your app: GitHub```
- ```next```
- ```Add repository and branch: vorthrak/application and main```
- ```next```
- ```App name: Application```
- ```next```
- ```save and deploy```
---
## DynamoDB
- ```create table```
- ```Table name: Dummytable```
- ```partition key: id```
- ```create table```
---
## Lambda
- ```create two function```
- ```Author from scratch```
- ```Function name: Dummysubmitfunc and Dummygetfun```
- ```Runtime: Python 3.13```
- ```Architecture: x86_64```
- ```Permissions```
- ```Change default execution role```
- ```Use an existing role: LabRole```
- ```taruh source code```
---
## API Gateway
- ```REST API```
- ```build```
- ```New API``` 
- ```API name: Dummymessage```
- ```API endpoint type: Regional```
- ```create api```
- ```create two resource```
- ```Resource name: Submit and Fetch```      
- ```centang CORS```
- ```create resource``` 
- ```create method```
- ```method type: POST and GET```
- ```integration type: Lambda Function```
- ```centang Lambda proxy integration```
- ```lambda function: Dummysubmitfunc and Dummygetfun```
- ```create method```
- ```Deploy API```
- ```stage```
- ```new stage: DummyprodS```
- ```Deploy```
---
## Testing
- ```test web using Domain in aws amplify```
---

