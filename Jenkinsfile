pipeline {
    agent any
    
    environment {
        FLASK_APP = 'app.py'
        SELENIUM_CHROME_DRIVER_PATH = '/usr/local/bin/chromedriver'
    }
    
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/dishaabhat/flask-docker-ec2.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Flask App') {
            steps {
                sh 'flask run --host=0.0.0.0 &'
                // You may need to add additional configuration for running Flask in the background
            }
            post {
                always {
                    script {
                        // Capture the PID of the Flask process and kill it after tests
                        env.FLASK_PID = sh(script: 'pgrep -f "flask run"', returnStdout: true).trim()
                    }
                }
            }
        }
        
        stage('Run Selenium Tests') {
            steps {
                // Add your Selenium test execution commands here
                // For example:
                // sh 'python Selenium_tests.py'
            }
        }
        
        stage('Deploy') {
            steps {
                // Add deployment steps here
                // For example:
                // sh 'deploy.sh'
            }
        }
    }
    
    post {
        always {
            script {
                // Ensure that the Flask process is stopped after execution
                if (env.FLASK_PID != '') {
                    sh "kill -9 ${env.FLASK_PID}"
                }
            }
        }
    }
}
