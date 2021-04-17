date_string=`date +%Y%m%d`
docker build -t shengqh/cqs_bamsnap:${date_string} .
docker build -t shengqh/cqs_bamsnap:latest .
docker push shengqh/cqs_bamsnap:${date_string}
docker push shengqh/cqs_bamsnap:latest
