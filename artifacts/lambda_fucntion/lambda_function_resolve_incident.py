import json
import boto3

def lambda_handler(event, context):
    #Get Security Group Object
    ec2 = boto3.resource('ec2')
    resource_id = event['EvaluateRequestOutput']['body']['resourceId']
    security_group = ec2.SecurityGroup(resource_id)
    
    client = boto3.client('ec2')
    response = client.describe_security_groups(GroupIds=[resource_id])
    
    for sgs in response['SecurityGroups']:
        print (sgs)
        for rules in sgs['IpPermissions']:
            if rules['IpProtocol'] == 'tcp' and rules['FromPort'] == 22:
                response = security_group.revoke_ingress(
                GroupId = resource_id,
                IpPermissions=[
                    {
                    'IpProtocol': 'tcp', 
                    'FromPort': 22, 
                    'ToPort': 22, 
                    'IpRanges': rules['IpRanges']
                     }
                ]
                )  
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Security Group rule deleted successfully')
    }
