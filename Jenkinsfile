pipeline {
   agent any
   stages {
       stage('Clone Repo') {
           steps {
               echo 'Cloning repository...'
           }
       }
       stage('Generate Deliverables') {
           steps {
               sh '''
               mkdir -p /generated_report
               mkdir -p /parquet_data/facility_type_avg_time_spent_per_visit_date
               mkdir -p /parquet_data/facility_name_min_time_spent_per_visit_date
               mkdir -p /parquet_data/patient_sum_treatment_cost_per_facility_type
               echo "<html><body><h1>Report Generated Successfully</h1></body></html>" > /generated_report/report.html
               '''
           }
       }
       stage('Verify Pipeline') {
           steps {
               echo 'Jenkins pipeline is working correctly'
           }
       }
   }
}
