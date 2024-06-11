docker build . -t texte_summarize:latest

docker images
docker run -p 8080:7860 --name text_summarize image_id
docker ps 