pipeline {
    agent any

    stages {
        stage('Clone repo') {
            steps {
                git credentialsId: 'github-creds', url: 'https://github.com/swayanp/automationexercise-tests.git'
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
                    automationexercise-tests
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/**/*.*', allowEmptyArchive: true
        }
    }
}
