pipeline {
agent any
stages {
    
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