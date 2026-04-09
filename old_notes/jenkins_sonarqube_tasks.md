1. SonarQube in pending state when trigger
2. Jenkins is accessible without login
3. parameterize values from jenkins and use credentials wherever possible
4. Standard practices on How to trigger parameterised build on git webhook

    1. fixed by updating correct webhook URL in Sonarqube. 
    SonarQube Administration → webhook → Update Correct Jenkins Sonarqube webhook → Save.

     2. Removed granted access of Anonymous user from Jenkins.
    Jenkins → Global Security Configuration → Matrix based security → update access and Save.

    3. update Jenkinsfile with following paramaters:
    example: 
    parameters { 	
    choice (name: 'env', choices: 'dev\ntest\nprod', description: 'your environment') 
    string(defaultValue: 'cli_creds', description: ' Credentials', name: 'creds_id')
    }
    withCredentials([

    		usernamePassword(credentialsId: ${creds_id}, usernameVariable: 'username', passwordVariable: 'password')]){

    		sh '''#!/bin/bash

    				set +xv

    				Testcmd login --username=${username} --password=${password} 

    				'''

    		}

    4. Updated webhook with credentials in Gitlab and enable build triggers with Build when a change is pushed to GitLab. 
    Webhook in gitlab be like: https://foo:password@jenkins.example.com/github-webhook/ 
