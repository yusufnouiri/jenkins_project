pipeline {
agent any
stages {
    stage ('GIT Checkout'){
        steps {
            git changelog: false, poll: false, url: 'https://github.com/yusufnouiri/jenkins_project.git'
        }
    }
    
    stage('build') {
  steps {
    sh 'echo building stage'
  }
}
    stage ('Test'){
        steps {
            sh 'python3 *.py'
        }
    }
}
}