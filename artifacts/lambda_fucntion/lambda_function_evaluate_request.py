import json

automation_allowed_entities =	["AWS::EC2::SecurityGroup"]

def lambda_handler(event, context):
    # TODO implement
    
    print(event)

    #message = event['Records'][0]['Sns']['Message']
    #message_dict = json.loads(event)
    message_details = event['detail']
    resource_id = message_details['resourceId']
    resource_type = message_details['resourceType']
    compliance_type= message_details['newEvaluationResult']['complianceType']
    body = {"resourceId": resource_id,"resourceType": resource_type, "complianceType": compliance_type}

    return {
    'statusCode': 200,
    'body': body
    }