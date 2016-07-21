# Create and start Exposee-Container, and create link with other containers
docker build -t rmsimage .
echo -n "Building RMS"
echo 'done'
docker run --name rmsapp -p 8001:8000 -d rmsimage
echo -n "makemigrations... "
docker exec -d rmsapp python manage.py makemigrations
echo "done"
echo -n "migrate"
echo 'done'
#echo -n "init_db... "
#docker exec -i rmsapp python manage.py shell < init_db.py
#python manage.py migrate --run-syncdb
echo "RMS is now ready!"


