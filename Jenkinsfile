pipeline {
    agent {
        docker { image 'python:3' }
    }
    stages{
        stage('version') {
            steps{
                sh 'python3 --version'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 selenium-login.py'
            }
        }
    }
}