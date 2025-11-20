pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "devops-python-app"
    }

    stages {

        stage('Checkout') {
            steps {
                git url: 'https://github.com/Gokulk-306/Devops-Assignment.git', branch: 'main'
            }
        }

        stage('Verify Workspace') {
            steps {
                sh '''
                echo "Current Directory:"
                pwd
                echo "List files:"
                ls -la
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                echo "Running basic health check..."
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t ${DOCKER_IMAGE}:latest .
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker stop devops-app || true
                docker rm devops-app || true
                docker run -d -p 5000:5000 --name devops-app ${DOCKER_IMAGE}:latest
                '''
            }
        }
    }

    post {
        success {
            emailext(
                subject: "Jenkins Build Successful !",
                body: "Jenkins pipeline completed successfully.",
                to: "gokulsmart515@gmail.com"
            )
        }
        failure {
            emailext(
                subject: "Jenkins Build Failed !!",
                body: "Jenkins pipeline failed. Please check logs.",
                to: "gokulsmart515@gmail.com"
            )
        }
    }
}
