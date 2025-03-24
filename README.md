# URL Shortener

A simple **URL Shortener** built with **Django, PostgreSQL, and Docker**.  
This app allows users to:
- Shorten URLs
  - Uses MD5 hashing and Base62 encoding for deterministic short URL generation.
- Retrieve original URL from a shortened URL
- Redirect shortened URL to the original URL
- Track usage analytics: count how many times a short URL was accessed

## Tech Stack
- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **Containerization**: Docker
- **Frontend**: HTML, CSS, JavaScript

## Getting Started

### 1. Clone the Repository  
```sh
git clone https://github.com/haodev/url-shortener.git
cd url-shortener
```

###  2. Run the App with Docker
```sh
docker-compose up --build
```
This will:
- Build the Django app inside a Docker container
- Set up a PostgreSQL database inside another container
- Run the Django development server on http://localhost:8000/

### 3. Set Up Database
```sh
# Create database migrations
docker-compose exec web python manage.py makemigrations

# Apply migrations
docker-compose exec web python manage.py migrate
```

### 4. Create Superuser
```sh
docker-compose exec web python manage.py createsuperuser
```

## Overview

### User Interface
This project includes a simple user interface at http://localhost:8000/

### Admin Portal
- Visit http://localhost:8000/admin
- Short URLs table stores the original and short URLs and the **click count** for the short URLs.

### API Endpoints
If you prefer, creating short URLs and retrieve original URLs can also be accessed using curl requests or any HTTP client like Postman (see example requests below).

#### Create Short URL
The POST endpoint accepts both JSON body requests and form-data
```sh
curl -X POST http://localhost:8000/shorten/ \
    -H "Content-Type: application/json" \
    -d '{ "url": "https://www.wikipedia.org" }'

OR

curl -X POST http://localhost:8000/shorten/ -d "url=https://www.wikipedia.org"
```

#### Get Original URL
The original endpoint accepts the full short URL using the short-url query parameter:
```sh
curl -X GET "http://localhost:8000/original/?short-url={full_short_url}"

E.g.
curl -X GET "http://localhost:8000/original/?short-url=http://localhost:8000/vHRqrD"
```

### Redirect to Original URL
The easiest way is to visit the short URL directly in a browser. E.g. http://localhost:8000/vHRqrD

Note that `main.js` calls a different API endpoint that works better for Javascript-based implementation:
```http://localhost:8000/redirect/?short-url={full_short_url}```


## Future Improvements
- Build a dashboard to show click analytics for each shortened URL (e.g., time of visits, location distribution, etc.)
- Generate QR code for short URLs
- Before generating a short URL, the server should check if the long URL is reachable and secure to prevent users from shortening broken or malicious URLs
- Add more validation for legal inputs
