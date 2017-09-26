import boto.sqs
import json
from boto.sqs.message import Message
import os

class Publisher:
    def __init__(self, aws_region, aws_access_key_id, aws_secret_access_key):
        self.client = boto.sqs.connect_to_region(aws_region,
                                                 aws_access_key_id=aws_access_key_id,
                                                 aws_secret_access_key=aws_secret_access_key)



    def publish_message(self, email, key):
        try:
            q = self.client.create_queue(os.environ['ACCOUNT_KEY_REQUESTED_TOPIC'])

            message_body = json.dumps({"email": str(email), "key": str(key)}, default=lambda o: o.__dict__, sort_keys=True, indent=4)

            m = Message()
            m.set_body(message_body)
            q.write(m)
            return True
        except Exception as e:
            print(e)
            return False;
