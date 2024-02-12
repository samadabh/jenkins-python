pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'py --version'
      }
    }
    stages {
    stage('install-selenium') {
      steps {
        bat 'py -m pip install selenium'
      }
    }
    stage('hello') {
      steps {
        bat 'py app.py'
      }
    }
  }
}
