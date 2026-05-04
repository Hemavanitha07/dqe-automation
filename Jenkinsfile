pipeline {
   agent any
   stages {
       stage('Clone Repo') {
           steps {
               echo 'Cloning repository...'
           }
       }
       stage('Verify Containers') {
           steps {
               sh 'podman ps'
           }
       }
       stage('Run Tests') {
           steps {
               sh '''
               python3 --version || echo "Python not installed"
               '''
           }
       }
   }
}
