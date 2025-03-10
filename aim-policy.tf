{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "lambda:InvokeFunction",
            "Resource": "arn:aws:lambda:us-east-1:123456789012:function:YourRotationLambda",
            "Principal": {
                "Service": "secretsmanager.amazonaws.com"
            },
            "Condition": {
                "ArnLike": {
                    "AWS:SourceArn": "arn:aws:secretsmanager:us-east-1:123456789012:secret:dev/wsrdsdb/secret-*"
                }
            }
        }
    ]
}
