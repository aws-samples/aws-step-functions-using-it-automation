import json

def lambda_handler(event, context):
    
    data_dict = {
        'resourceId': event['EvaluateRequestOutput'] ['body']['resourceId'],
        'resourceType': event['EvaluateRequestOutput'] ['body']['resourceType'],
        'tickeID': event['TicketCreationResponse'] ['ticketNumber']
    }

    email_message =   email_message = "Hi Operations team, This is an automated message from IT. There was an incident related to resource id {resourceId} and resource type {resourceType}. An incident ticket was raised and closed with ticket id as {tickeID}. For more information click here.".format(**data_dict)

    print (email_message)
    # TODO implement
    return {
        "statusCode": 200,
        "message" : '{"default": "A message.","email":"'+ email_message + '","subject":"AWS Operation Incident Noti"}' 
        
    }
