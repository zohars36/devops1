
import sys
import boto3


class EC2handler:

    def __init__(self):
        self.ec2_client = self.connectAWS()

    def read_credentials_file(self, file_path):
        credentials = {}
        with open(file_path, 'r') as file:
            for line in file:
                if (line.find("=") > 0):
                    key, value = line.strip().split(' = ')
                    credentials[key] = value
        return credentials

    def connectAWS(self):
        # Specify the path to your credentials file
        credentials_file_path = '/home/zohar/.aws/credentials'

        # Read the credentials from the file
        credentials = self.read_credentials_file(credentials_file_path)

        # print(credentials)

        # Create a session using the specified credentials
        session = boto3.Session(
            aws_access_key_id=credentials["aws_access_key_id"],
            aws_secret_access_key=credentials["aws_secret_access_key"],
            region_name="eu-central-1"
        )

        ec2_client = session.client('ec2')

        return ec2_client

    def get_instance_list(self):
        response = self.ec2_client.describe_instances()
        instance_list = []
        # Extract instance details from the response
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_tags = instance['Tags'][0]
                instance_id = instance['InstanceId']
                instance_state = instance['State']['Name']
                instance_list.append(
                    {'InstanceTags': instance_tags, 'InstanceId': instance_id, 'State': instance_state})

        return instance_list

    def stop_instances(self, instance_ids):
        response = self.ec2_client.stop_instances(
            InstanceIds=instance_ids
        )
        print("Instances stopped successfully.")
        return response

    def start_instances(self, instance_ids):
        response = self.ec2_client.start_instances(
            InstanceIds=instance_ids
        )
        print("Instances started successfully.")
        return response


def main(args):
    # args = ["stop"]
    ec2_handler = EC2handler()
    instances = ec2_handler.get_instance_list()
    if (args[0] == "show"):
        # Print the instance details
        for instance in instances:
            print(
                f"Instance Tags: {instance['InstanceTags']},Instance ID: {instance['InstanceId']}, State: {instance['State']}")
    elif (args[0] == "stop"):
        instanceIds = []
        for instance in instances:
            instanceIds.append(instance['InstanceId'])
        ec2_handler.stop_instances(instanceIds)
    elif (args[0] == "start"):
        instanceIds = []
        for instance in instances:
            instanceIds.append(instance['InstanceId'])
        ec2_handler.start_instances(instanceIds)
    else:
        print("please select ec2 action start/stop/show")


if __name__ == '__main__':
    arguments = sys.argv[1:]
    main(arguments)
