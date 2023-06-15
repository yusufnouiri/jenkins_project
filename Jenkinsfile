pipeline {
 agent {
  docker {
    image 'python:3.9-slim'
    args '-u root --privileged'
  }
stages {
    
    stage('build') {
  steps {
    sh 'echo building stage'
  }
}
    stage ('Test'){
        steps {
            sh 'python *.py'
        }
    }
}
}