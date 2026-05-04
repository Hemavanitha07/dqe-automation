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
               sh 'podman-compose up -d'
           }
       }
       stage('Wait for services') {
           steps {
               sh 'sleep 20'
           }
       }
       stage('Verify Containers') {
           steps {
               sh 'podman ps'
           }
       }
   }
}
