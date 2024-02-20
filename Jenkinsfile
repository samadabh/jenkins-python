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
    stage('install-pytest') {
      steps {
        bat 'py -m pip install pytest'
      }
    }
    stage('check-ise-partner-portal-status') {
      steps {
        bat 'python -m pytest test_app.py'
      }
    }
  }
  post {
    always {
        junit allowEmptyResults: true, testResults: '**/test-results/*.xml'
    }
}
}
