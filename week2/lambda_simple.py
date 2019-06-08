def lambda_handler(event, context):
     return {
        "sessionAttributes": {},
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
            "contentType": "PlainText",
            "content": "return msg"
        }
      }
    }
