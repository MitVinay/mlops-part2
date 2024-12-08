

import dagshub
import mlflow
mlflow.set_tracking_uri("https://dagshub.com/MitVinay/mlops-part2.mlflow")
dagshub.init(repo_owner='MitVinay', repo_name='mlops-part2', mlflow=True)

mlflow.set_experiment("test1")
# hash
with mlflow.start_run(experiment_id=1):
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)