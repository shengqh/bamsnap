date_string=`date +%Y%m%d`
docker build -t shengqh/cqs_bamsnap:${date_string} .
docker tag shengqh/cqs_bamsnap:${date_string} shengqh/cqs_bamsnap:latest
