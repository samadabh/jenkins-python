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
        bat 'python -m pytest test_app.py -s --junitxml=C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\checking_ise_partner_portal\\target\\report.xml'
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
}
}
