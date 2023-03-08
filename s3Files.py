import boto3

config = {
    'aws_access_key_id': 'AKIAZ6RF4EGJR5SB4J3W',
    'aws_secret_access_key': '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',
    'region_name': 'us-east-1'
}

client = boto3.client('s3', aws_access_key_id=config['aws_access_key_id'], 
                      aws_secret_access_key=config['aws_secret_access_key'], 
                      region_name=config['region_name'])


file_name = "data_file.csv.txt"
file_path = r"C:\Users\Abrah\Desktop\data_file.csv.txt"


with open (file_path, 'rb') as file:
    #ACL='public-read' makes the file public
    client.put_object(Bucket='autentico-corajillo', Key=file_name, Body=file)



