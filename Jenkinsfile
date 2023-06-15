pipeline {
    agent any
    
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
