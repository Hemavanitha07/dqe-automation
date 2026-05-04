pipeline {
   agent any
   stages {
       stage('Clone Repo') {
           steps {
               echo 'Cloning repository...'
           }
       }
       stage('Run Containers') {
           steps {
               bat 'python -m podman_compose up -d'
           }
       }
       stage('Verify') {
           steps {
               bat 'podman ps'
           }
       }
   }
}
