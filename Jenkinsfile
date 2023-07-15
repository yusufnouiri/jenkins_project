pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/yusufnouiri/jenkins_project.git']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/yusufnouiri/jenkins_project.git'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m selenium-login.py'
            }
        }
    }
}
