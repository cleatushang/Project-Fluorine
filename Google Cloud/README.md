# Setting up SP500 database with Google Cloud Platform(GCP)
## Put SP.py file into VM instances
### By Nano editor
Run in SSH  
```Nano SP.py```
## Schedule script on GCP
### Basic Setup
Edit VM instances  
Go Metadata section -> Startup script  
```python3 /home/*Enter your path*/helloworld.py```  
It means everytime you startup the VM, the python script will run automatically
```tail -n 100 /var/log/syslog```  
check if the script work properly
### Create funtion
```
def start_vm(request):
    from pprint import pprint
    from googleapiclient import discovery
    from oauth2client.client import GoogleCredentials
    
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('compute', 'v1', credentials=credentials)
    
    # Project ID for this request.
    project = 'usstockalwaysrise' # here you project ID name
    
    # The name of the zone for this request.
    zone = 'asia-east2-a' # put here your zone
    
    # Name of the instance resource to stop.
    instance = 'instance-1' # put here the name of the vm to start
    req = service.instances().start(project=project, zone=zone, instance=instance)
    response = req.execute()
```
```
# Function dependencies, for example: 
# package>=version 
google-api-python-client 
oauth2client
```
