ab -c 100 -n 500 -r http://ec2-18-188-140-131.us-east-2.compute.amazonaws.com/stress-test/get.php
echo '------------------------------------------------------------------------------------------------------------------'
ab -p data.json -T application/json -c 100 -n 500 -r -l http://ec2-18-188-140-131.us-east-2.compute.amazonaws.com/stress-test/post.php
echo '------------------------------------------------------------------------------------------------------------------'
ab -c 100 -n 500 -r http://ec2-18-188-140-131.us-east-2.compute.amazonaws.com:3010/
echo '------------------------------------------------------------------------------------------------------------------'
ab -p data.json -T application/json -c 100 -n 500 -r -l http://ec2-18-188-140-131.us-east-2.compute.amazonaws.com:3010/