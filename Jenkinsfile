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
            sh 'apt install python'
            sh 'python *.py'
        }
    }
}
}