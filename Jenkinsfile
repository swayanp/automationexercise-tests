pipeline {
    agent any

    stages {
        stage('Clone repo') {
            steps {
                git branch: 'main', credentialsId: 'github-creds', url: 'https://github.com/swayanp/automationexercise-tests.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t automationexercise-tests .'
            }
        }

        stage('Run Tests Inside Docker') {
            steps {
                sh '''
                    docker run --rm \
                    -v "${WORKSPACE}/reports:/app/reports" \
                    automationexercise-tests \
                    pytest tests/ --alluredir=/app/reports -v --capture=tee-sys
                '''
            }
        }
    }

    post {
        always {
            // Publishes Allure results collected inside ${WORKSPACE}/reports
            allure includeProperties: false, jdk: '', results: [[path: 'reports']]
        }
    }
}
