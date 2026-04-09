pipeline{
    agent any
         parameters {
        string(name: 'X_VALUE', defaultValue: '5', description: 'Enter X value')
        string(name: 'Y_VALUE', defaultValue: '10', description: 'Enter Y value')
         }
    stages{
        stage('version'){
            steps{
                bat '"c:\\Windows\\System32\\cmd.exe" /c python --version'
            }
        }
        stage('STAGE2'){
            steps{
                bat '"c:\\Windows\\System32\\cmd.exe" /c python python.py %X_VALUE% %Y_VALUE%'
            }
        }
    }
}
