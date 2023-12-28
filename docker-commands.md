1. pip freeze > requirements.txt
2. chmod +x ./entrypoint.sh
3. docker-compose build --no-cache (To run docker and also Remove cache from docker)
3. docker-compose up -d --build (To run docker)


#################### PRODUCTION COMMANDS
docker-compose -f docker-compose.prod.yml down -v -> ()   

docker-compose -f docker-compose.prod.yml up -d --build -> (To run a particular docker-compose file, in this case, it is the production docker file)

docker-compose -f docker-compose.prod.yml exec dcelery python manage.py migrate --noinput -> ()

