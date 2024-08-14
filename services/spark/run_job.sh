docker-compose up --scale spark-worker=3 -d

docker exec da-spark-master ./opt/spark/apps/run_all.sh
