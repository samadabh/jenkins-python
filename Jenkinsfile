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
        bat 'set PYTEST_ADDOPTS="--junitxml=C:/ProgramData/Jenkins/.jenkins/workspace/checking ise partner portal/target/report.xml --json-report --json-report-file=C:/ProgramData/Jenkins/.jenkins/workspace/checking ise partner portal/target/report.json"'
        bat 'python -m pytest test_app.py -s'
        bat 'copy C:/ProgramData/Jenkins/.jenkins/workspace/checking ise partner portal/target/report.xml C:/ProgramData/Jenkins/.jenkins/workspace/checking ise partner portal/perftest.xml'
      }
    }
  }
  post {
    always {
        junit skipPublishingChecks: true, allowEmptyResults: true, skipMarkingBuildUnstable: true, testResults: 'perftest.xml'
    }
    failure {  
             mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "saaketh89@gmail.com";  
    } 
}
}
