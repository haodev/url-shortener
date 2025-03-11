# url-shortener
 
superuser
admin
admin123

curl -X POST http://localhost:8000/shorten/ \
-H "Content-Type: application/json" \
-d '{
    "url": "https://www.wikipedia.org"
}'

# simple GET /original/<short-url> request
curl -X GET http://localhost:8000/original/<short-url>/