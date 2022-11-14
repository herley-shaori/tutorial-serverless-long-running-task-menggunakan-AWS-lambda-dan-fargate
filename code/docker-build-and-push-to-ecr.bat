docker build -t randomstringimage:latest .
aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 623127157773.dkr.ecr.ap-southeast-1.amazonaws.com
docker tag randomstringimage:latest 623127157773.dkr.ecr.ap-southeast-1.amazonaws.com/random-string-image:latest
docker push 623127157773.dkr.ecr.ap-southeast-1.amazonaws.com/random-string-image:latest