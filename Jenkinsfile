pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'py --version'
      }
    }
    stage('install-selenium') {
      steps {
        bat 'py -m pip install selenium'
      }
    }
    stage('run-python-selenium-script') {
      steps {
        bat 'py app.py'
      }
    }
  }
}
