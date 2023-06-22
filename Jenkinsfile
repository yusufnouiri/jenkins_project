pipeline {
    agent any
    stages{
        stage('version') {
            steps{
                sh 'pip --version'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 selenium-login.py'
            }
        }
    }
}