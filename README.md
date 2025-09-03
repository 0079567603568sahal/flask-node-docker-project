# flask-node-docker-project
flask-node-docker-project

A full-stack Dockerized application with:

Backend: Flask (Python) REST API connected to PostgreSQL

Frontend: Node.js (Express) serving API calls to the backend

Database: PostgreSQL

Container Management: Docker & Docker Compose

Project Structure
flask-node-docker-project/
│
├── backend/
│   ├── app.py               # Flask backend application
│   ├── requirements.txt     # Python dependencies
│   ├── Dockerfile           # Backend container configuration
│
├── frontend/
│   ├── server.js            # Node.js frontend server
│   ├── package.json         # Node.js project metadata & dependencies
│   ├── package-lock.json    # Dependency lock file
│   ├── Dockerfile           # Frontend container configuration
│
├── docker-compose.yml       # Orchestration of backend, frontend, and database
├── .gitignore               # Files/folders to be ignored in Git
├── README.md                # Project documentation

Features

Flask backend with /api/data, /submit, and /db-check routes

Node.js frontend calling backend APIs

PostgreSQL database connection check

Fully containerized using Docker Compose

CORS enabled for frontend-backend communication

Requirements

Docker

Docker Compose

Python 3.x (for local backend development)

Node.js (for local frontend development)

Setup & Run
1. Clone Repository
git clone https://github.com/<your-username>/flask-node-docker-project.git
cd flask-node-docker-project

2. Build & Start Containers
docker-compose up --build


This will:

Build backend and frontend images

Start PostgreSQL container

Link all services via Docker network

Backend Endpoints
Method	Endpoint	Description
GET	/api/data	Returns test JSON from backend
POST	/submit	Accepts JSON { name, email } and returns it
GET	/db-check	Returns PostgreSQL version

Example:

curl http://localhost:5000/api/data
curl -X POST http://localhost:5000/submit -H "Content-Type: application/json" -d '{"name": "Sahal", "email": "sahal@example.com"}'

Frontend

Runs on port 3000.
Calls backend APIs via:

fetch("http://backend:5000/api/data")

Docker Commands Used
Build and Run:
docker-compose up --build

View Logs:
docker-compose logs -f

List Images:
docker images

Tag Image:
docker tag flask-node-docker-project-backend:latest your_dockerhub_username/backend:latest
docker tag flask-node-docker-project-frontend:latest your_dockerhub_username/frontend:latest

Push to Docker Hub:
docker push your_dockerhub_username/backend:latest
docker push your_dockerhub_username/frontend:latest

.gitignore
__pycache__/
node_modules/
.env
*.pyc
*.pyo
.DS_Store

License

MIT License
