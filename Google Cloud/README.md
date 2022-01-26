# Setting up SP500 database with Google Cloud Platform(GCP)
## Put SP.py file into VM instances
### By Nano editor
Run in SSH
'Nano SP.py'
## Schedule script on GCP
### Basic Setup
Edit VM instances
Go Metadata section -> Startup script
'python3 /home/*Enter your path*/helloworld.py'
It means everytime you startup the VM, the python script will run automatically
