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
    stage('check-ise-partner-portal-status') {
      steps {
        bat 'py app.py'
      }
    }
  }
  post {
    always {
        junit 'seletest.xml'
    }
}
}
