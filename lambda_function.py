import json
import boto3

#################
# Sample code
# Please modify to meet your usecase and security best practices
#################

def lambda_handler(event, context):
    sub =  event["detail"]["eventName"]
    domainName = event["detail"]["requestParameters"]["domainName"]
    userName = event["detail"]["userIdentity"]["sessionContext"]["sessionIssuer"]["userName"]
    accountId = event["detail"]["userIdentity"]["sessionContext"]["sessionIssuer"]["accountId"]    
    endWithDomain1 = domainName.endswith("yourdomain1.yourdomain2.org")
    endWithDomain2 = domainName.endswith("yourdomain.com")
    if not (endWithDomain2 or endWithDomain1):
        print("cert name invalid, sending notification")
        message = "Alert: "+ sub + " event from Amazon Certficate Manager has be been detected with an invalid domain name " + domainName + " by user "+ userName + " from account id " + accountId
        email("Invalid Certificate Request",message)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


def email(sub,content):
    # send the email to topic.
   notification = "Here is the SNS notification for Lambda function tutorial."
   client = boto3.client('sns')
   response = client.publish (
      TargetArn = "arn:aws:sns:us-east-1:111222333444555:test-topic",
      Message = content,
      Subject = sub
   )
   return {
      'statusCode': 200,
      'body': json.dumps(response)
   }
