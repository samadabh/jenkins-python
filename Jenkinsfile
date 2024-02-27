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
        catchError {
          bat 'python -m pytest test_app.py -s --junitxml=C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\checking_ise_partner_portal\\target\\report.xml'
        }
      }
    }  
    stage('copy-test-results-file'){
      steps{
        bat 'copy "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\checking_ise_partner_portal\\target\\report.xml" "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\checking_ise_partner_portal\\perftest.xml" /Y'
      }
    }
  }
  post {
    always {
        junit skipPublishingChecks: true, allowEmptyResults: true, skipMarkingBuildUnstable: true, testResults: 'perftest.xml'
    }
    failure {  
        mail bcc: '', body: "<b>Feed Portal access is failing, check on priority</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "Feed portal access not working -> ${env.JOB_NAME}", to: "swathrao@cisco.com";  
    } 
}
}
