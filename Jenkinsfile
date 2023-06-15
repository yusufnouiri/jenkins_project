pipeline {
    agent {
        docker {
            // Specify the Docker image to use
            image 'python:latest'
            // Specify any additional Docker configuration options, if needed
            // ...
        }
    }
    
    stages {
        stage('Build') {
            steps {
                sh 'echo building stage'
            }
        }
        
        stage ('Test') {
            steps {
                // Install any required dependencies
                sh 'apt update && apt install -y python'
                
                // Execute your tests
                sh 'python *.py'
            }
        }
    }
}
