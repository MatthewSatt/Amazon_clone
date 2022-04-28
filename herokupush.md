docker buildx build --platform linux/amd64 -t mattsamazonclone .
docker tag mattsamazonclone registry.heroku.com/mattsamazonclone/web
docker push registry.heroku.com/mattsamazonclone/web
heroku container:release web -a mattsamazonclone
heroku run -a mattsamazonclone flask seed undo
heroku run -a mattsamazonclone flask db upgrade
heroku run -a mattsamazonclone flask seed all
