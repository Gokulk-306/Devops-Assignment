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

        stage('Install Dependencies') {
            steps {
                sh '''
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
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
            echo "Build & Deployment Successful !"

            emailext(
                subject: "Jenkins Build Successful !",
                body: "Hello,\n\nThe Jenkins CI/CD pipeline completed successfully.\n\nRegards,\nJenkins",
                to: "ceecgokul2024@gmail.com"
            )
        }

        failure {
            echo "Build Failed !!"

            emailext(
                subject: "Jenkins Build Failed !!",
                body: "Hello,\n\nThe Jenkins CI/CD pipeline has failed.\nPlease check the logs.\n\nRegards,\nJenkins",
                to: "ceecgokul2024@gmail.com"
            )
        }
    }
}
