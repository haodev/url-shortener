# URL Shortener

A simple **URL Shortener** built with **Django, PostgreSQL, and Docker**.  
This app allows users to:
- Shorten URLs
- Retrieve original URL from a shortened URL
- Redirect shortened URL to the original URL
- Count how many times a short URL was accessed

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

## Usage
This project includes:
- A simple web page (visit http://localhost:8000/ in your browser) that allows users to:
    - Shorten long URLs
    - Retrieve the original URL from a shortened URL
    - Redirect to the original URL given a short URL
- All server functionalities and APIs can also be accessed using curl requests or any HTTP client like Postman
- Log into admin portal to see the click count for each short URL

### API Endpoints

#### 1. Create Short URL
The POST endpoint accepts both JSON body requests and form-data
```sh
curl -X POST http://localhost:8000/shorten/ \
    -H "Content-Type: application/json" \
    -d '{ "url": "https://www.wikipedia.org" }'

OR

curl -X POST http://localhost:8000/shorten/ -d "url=https://www.wikipedia.org"
```

#### 2. Get Original URL
The original endpoint accepts the full short URL using the short-url query parameter:
```sh
curl -X GET "http://localhost:8000/original/?short-url={full_short_url}"

curl -X GET "http://localhost:8000/original/?short-url=http://localhost:8000/vHRqrD"
```

#### 3. Redirect to Original URL
Visit ```http://localhost:8000/redirect/?short-url={full_short_url}``` in a browser will direct you to the original URL.
``` E.g. http://localhost:8000/original/?short-url=http://localhost:8000/vHRqrD```

### Admin Portal
- Visit http://localhost:8000/admin
- Short URLs table stores the original and short URLs and the **click count** for the short URLs.

## Future Improvements
- Build a dashboard to show click analytics for each shortened URL (e.g., time of visits, location distribution, etc.)
- Generate QR code for short URLs
- Before generating a short URL, the server should, the server should check if the long URL is reachable and secure to prevent users from shortening broken or malicious URLs
- Update `/original/` and `/redirect/` API to handle inputs as 6 digits short code
- Add more validation for legal inputs
