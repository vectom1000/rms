# Create and start Exposee-Container, and create link with other containers
docker build -t rmsimage .
echo -n "Building RMS"
echo 'done'
docker run --name rmsapp -p 8001:8000 -d rmsimage
echo -n "makemigrations... "
docker exec -d rmsapp python manage.py makemigrations
echo "done"
echo -n "migrate"
docker exec -i rmsapp python manage.py migrate
echo 'done'
#echo -n "init_db... "
sleep 1
docker exec -i rmsapp python manage.py shell < init_db2.py
#python manage.py migrate --run-syncdb
#python manage.py makemigrations rms_app
echo "RMS is now ready!"
#python manage.py migrate --run-syncdb

