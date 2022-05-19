# data-sync-task-agent-switch

## The tool enables an user to switch DataSync tasks between agents

Steps to deploy:
- Clone the repo
````bash
git clone https://github.com/anshumch/data-sync-task-agent-switch.git
````
- Run the following command:
````bash
sam deploy --guided
````
- Pass the following values:
![image](https://user-images.githubusercontent.com/100800132/168938651-e38dcafc-cae6-4057-9da6-5345521c6aac.png)

- Once the stack is deployed, you will receive an output with stack successful creation message. Note the API output value. We will call this API endpoint to execute the lambda to switch DataSync tasks between DataSync agents.
![image](https://user-images.githubusercontent.com/100800132/169391553-f003e402-4b5e-422d-a80e-f1d2f48bdf2b.png)

- To run it:
![image](https://user-images.githubusercontent.com/100800132/169392222-9b2f5f18-646c-4cf0-ad20-776868181118.png)
