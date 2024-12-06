

import dagshub
dagshub.init(repo_owner='MitVinay', repo_name='mlops-part2', mlflow=True)
mlflow.set_tracking_uri("https://dagshub.com/MitVinay/mlops-part2.mlflow")

mlflow.set_experiment("test")
import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)