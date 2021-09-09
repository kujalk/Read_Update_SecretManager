Developer - K.Janarthanan
Purpose - To read/update secret from AWS Secret Manager
Requirements - Python > 3.5

Methods
--------------
[1] pip install -r requirements.txt
[2] Read_Value.py -> Fill the parameters inside the script and execute it
                    aws_access_key_id = ""
                    aws_secret_access_key = ""
                    aws_region = ""
                    namespace = "secret name"

[3] Write_Value.py -> Fill the parameters inside the script and execute it
                    aws_access_key_id = ""
                    aws_secret_access_key = ""
                    aws_region = ""
                    namespace = "secret name"
                    secret = '{"book":"potter","film":"bell"}' 

PS - Write_Value.py updates and preserve the existing secret key/value 