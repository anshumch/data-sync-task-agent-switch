import json
import boto3

clientDS = boto3.client('datasync')


def lambda_handler(event, context):
    print(event)
    
    responseObjectList = []
    
    taskArn = None
    sourceLocationArn = None
    agentArn = None
    
    inputBody = json.loads(event.get("body"))
    
    tasks = inputBody.get("tasks")
    agentName = inputBody.get("agentName")
    
    responseTaskList = clientDS.list_tasks()
    print(responseTaskList)
    
    for taskName in tasks:
        for task in responseTaskList.get("Tasks"):
            if(task.get("Name") == taskName):
                taskArn = task.get("TaskArn")
                responseTaskDetails = clientDS.describe_task(
                        TaskArn=taskArn
                    )
                print(responseTaskDetails)
                sourceLocationArn = responseTaskDetails.get("SourceLocationArn")
                print(sourceLocationArn)
                
        responseAgentList = clientDS.list_agents()
        print(responseAgentList)
        
        for agent in responseAgentList.get("Agents"):
            if(agent.get("Name") == agentName):
                agentArn = agent.get("AgentArn")
        
        print(sourceLocationArn)
        print(agentArn)
        
        response = clientDS.update_location_nfs(
                LocationArn=sourceLocationArn,
                OnPremConfig={
                    'AgentArns': [
                        agentArn,
                    ]
                }
            )
        
        responseSourceLocationDetails = clientDS.describe_location_nfs(
                LocationArn=sourceLocationArn
            )
        print(responseSourceLocationDetails)
        
        responseAgentDetails = clientDS.describe_agent(
                AgentArn=agentArn
            )
        print(responseAgentDetails)
        
        responseTaskDetails = clientDS.describe_task(
                TaskArn=taskArn
            )
        print(responseTaskDetails)
        
        responseObject = {}
        responseObject["sourceLocationDetails"] = responseSourceLocationDetails
        responseObject["agentDetails"] = responseAgentDetails
        responseObject["taskDetails"] = responseTaskDetails
        
        responseObjectList.append(responseObject)
        
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(responseObjectList, default=str)
    }
