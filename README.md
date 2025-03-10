# Lambda-Secret-Rotation
 Enable secrets rotation from Lambda function in AWS Secrets Manager

    
Policy:
![image](https://github.com/user-attachments/assets/1b33ef34-62f0-4a09-b88c-4646ea9fe71b)  
![image](https://github.com/user-attachments/assets/557dd15c-b26f-4ac8-bb8b-0cf68e5bc4ae)   

![image](https://github.com/user-attachments/assets/879a6d96-7211-44b5-b870-ce86fb8613c0)
```
{
  "Version": "2012-10-17",
  "Id": "default",
  "Statement": [
    {
      "Sid": "ws-01",
      "Effect": "Allow",
      "Principal": {
        "Service": "secretsmanager.amazonaws.com"
      },
      "Action": "lambda:InvokeFunction",
      "Resource": "arn:aws:lambda:us-east-1:255945442255:function:Lambda-SM"
    }
  ]
}
```   
![image](https://github.com/user-attachments/assets/d9d74196-2980-4adf-a6d9-4627df79c8b8)   




