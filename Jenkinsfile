pipeline {
   agent any
   stages {
       stage('Clone Repo') {
           steps {
               echo 'Cloning repository...'
           }
       }
       stage('Verify Environment') {
           steps {
               sh 'echo "Jenkins is running correctly"'
           }
       }
       stage('Run Tests') {
           steps {
               sh '''
               echo "Run your automation here"
               '''
           }
       }
   }
}
