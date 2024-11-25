import json
import requests

print('Loading function')


def lambda_handler(event, context):
    d = json.loads(event['body'])
    API_KEY='PUT API KEY HERE'
    r = requests.post(
            'https://connect.mailerlite.com/api/subscribers',
            json={
                "email": d['email']
            },
            headers= {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}",
            }
        )
    r.raise_for_status()
    return {
        'statusCode': 200,
        'body': json.dumps(d)
    }