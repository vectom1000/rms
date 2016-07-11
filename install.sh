# Create common network
docker network create simple-network

# Create and start PostgreSQL-Container
#docker run --name db --net=simple-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=12345 -v /#var/lib/postgresql/data -d postgres

# Create and start Mail-Container
#docker pull djfarrelly/maildev
#docker tag djfarrelly/maildev maildev
#docker run --name mail --net=simple-network -d -p 1080:80 -p 1025:25 maildev

# Create and start Exposee-Container, and create link with other containers
cd ..
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
#docker exec -i exposeeapp python manage.py shell < init_db.py
echo "Exposee is now ready!"

