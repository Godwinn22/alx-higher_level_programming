#!/bin/bash
# This is  a Bash script that makes a request to 0.0.0.0:5000/catch_me and causes the server to respond
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
