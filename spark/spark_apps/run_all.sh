#!/bin/bash

for script in /opt/spark/apps/*.py; 
do
  echo "Submitting $script"
  spark-submit --master spark://spark-master:7077 --deploy-mode client "$script"
done
