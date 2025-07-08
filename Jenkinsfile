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

        stage('Run Tests in Docker') {
            steps {
                sh '''
                    docker run --rm \
                    -v "${WORKSPACE}/reports:/app/reports" \
                    automationexercise-tests \
                    pytest tests/ --alluredir=/app/reports -v
                '''
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'reports']]
        }
    }
}
