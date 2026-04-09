pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                bat 'py --version'
            }
        }

        stage('STAGE2') {
            steps {
                bat "py python.py %X_VALUE% %Y_VALUE%"
            }
        }
    }
}
