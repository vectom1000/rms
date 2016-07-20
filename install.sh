# Create common network
docker network create simple-network

# Create and start Exposee-Container, and create link with other containers
docker build -t rmsimage .
echo -n "Building RMS"
while true;do echo -n .;sleep 1;done &
sleep 1 # or do something else here
kill $!; trap 'kill $!' SIGTERM
echo 'done'
docker run --name rmsapp --net=simple-network  -p 8000:8000 -d rmsimage
echo -n "makemigrations... "
docker exec -d rmsapp python manage.py makemigrations
echo "done"
echo -n "migrate"
docker exec -d rmsapp python manage.py migrate
while true;do echo -n .;sleep 1;done &
sleep 1 # or do something else here
kill $!; trap 'kill $!' SIGTERM
echo 'done'
echo -n "init_db... "
docker exec -i rmsapp python manage.py shell < init_db.py
echo "RMS is now ready!"

