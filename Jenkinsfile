pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'py --version'
        bat 'export PYTEST_ADDOPTS="--junitxml=/tmp/pytest/report.xml --json-report --json-report-file=/tmp/pytest/report.json"'
        bat 'cp /tmp/pytest/report.xml $WORKSPACE/perftest.xml'
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
        bat 'python -m pytest test_app.py -s'
      }
    }
  }
  post {
    always {
        junit allowEmptyResults: true, testResults: 'perftest.xml'
    }
}
}
