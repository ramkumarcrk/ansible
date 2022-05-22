#!/usr/bin/python
#Package for REST API CALL and json formatting
import requests
import json
headers = { 'Accept': '*/*',}
url= 'https://jira.company.com/rest/plugins/applications/1.0/installed/jira-software'
#r=requests.get(url=url,headers=headers,auth=("username","password"),verify=False)
r=requests.get(url=url,headers=headers,auth=("username","password"))
if r.status_code == 200:
 data=json.loads(r.text)
 print("JIRA URL is healthy and status code is %d" % (r.status_code))
 activeUsers = data['accessDetails']['activeUserCount']
 licensedUserCount = data['accessDetails']['licensedUserCount']
 print("There are currently %d counted towards JIRA Software License" % (activeUsers))
 print("Total number of License towards JIRA Software is %d" % (licensedUserCount))
 licensedUsers = data['accessDetails']['licensedUserCount']
 remainingLicenses= licensedUsers - activeUsers
 print("There are %d licenses left" % (remainingLicenses))

else:
 print("JIRA URL status code is %d not 200, Please have your insight to check " % (r.status_code))
