pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'py --version'
      }
    }
    stage('hello') {
      steps {
        bat 'py app.py'
      }
    }
  }
}
