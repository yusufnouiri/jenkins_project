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
                script {
                    // Run the Docker container
                    docker.image('python:latest').inside {
                        // Install any required dependencies
                        sh 'apt update && apt install -y python'
                        
                        // Execute your tests inside the Docker container
                        sh 'python *.py'
                    }
                }
            }
        }
    }
}
