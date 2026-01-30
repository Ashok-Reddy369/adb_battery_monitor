pipeline {
  agent {
    docker {
      image 'python:3.10-slim'
      args '-u root:root'
    }
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install dependencies') {
      steps {
        sh 'python -m pip install --upgrade pip setuptools'
        sh 'if [ -f requirements.txt ]; then pip install -r requirements.txt || true; fi'
      }
    }

    stage('Run tests') {
      steps {
        sh 'pytest tests/ -v --html=reports/html/battery_report.html --self-contained-html'
      }
    }

    stage('Archive report') {
      steps {
        archiveArtifacts artifacts: 'reports/html/**', fingerprint: true
        publishHTML (target: [reportName: 'Battery Report', reportDir: 'reports/html', reportFiles: 'battery_report.html'])
      }
    }
  }

  post {
    always {
      echo 'Pipeline finished.'
    }
  }
}
