
# Personal Finance Management Project

An end-to-end personal finance management application built with microservices architecture to help users track expenses, set savings goals, and get personalized financial advice.

## Table of Contents
- Features
- Tech Stack
- Architecture Overview
- Setup Guide
  - Local Environment
  - Docker Setup
- Environment Variables
- API Endpoints
- Development Guidelines
- License

## Features
1. Expense Tracking and Analysis
   - Categorize and analyze expenses over time.
2. Spending Recommendations
   - AI-driven insights to improve spending habits.
3. Savings Goals
   - Set and track progress toward savings targets.
4. Financial Health Reports
   - Alerts and reports based on spending patterns.
5. Personalized Financial Advice
   - Tailored suggestions powered by machine learning.

## Tech Stack
### Backend
- Python 3.9+
- Flask
- PostgreSQL
- Redis (for caching)

### Frontend
- React.js or Vue.js (optional)

### Tools
- Docker, Docker Compose
- RabbitMQ (for asynchronous tasks)
- Kubernetes (for orchestration)

## Architecture Overview
**System Architecture Diagram**
```
   User Interface (React/Vue)
           |
           |--------> API Layer (Flask)
           |
   AI/ML Engine <--- Database (PostgreSQL/MongoDB)
```

**Flowchart** (Example for Expense Analysis)
```
Start
    |
    |---> User Registration/Login
    |       |
    |       |---> Collect basic financial details (income, goals)
    |
    |---> Expense Entry
    |       |
    |       |---> User manually inputs expense OR auto-imports
    |       |
    |       |---> Analyze expense categories, trends
    |
    |---> AI Analysis & Suggestions
            |
            |---> Generate spending report
            |---> Suggest savings adjustments
End
```

## Setup Guide
### 1. Local Environment Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/expense-tracker.git
   cd expense-tracker
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run a service locally:
   ```bash
   cd user-service
   python app.py
   ```

### 2. Docker Setup
1. Build and run services using Docker Compose:
   ```bash
   docker-compose up --build
   ```

2. Stop services:
   ```bash
   docker-compose down
   ```

## Environment Variables
Use a `.env` file to manage sensitive configurations.

### Required Variables
| Variable             | Description                        | Example                                    |
|----------------------|------------------------------------|--------------------------------------------|
| FLASK_ENV            | Flask environment                 | development or production                 |
| SECRET_KEY           | Flask secret key                  | your_secret_key_here                      |
| DATABASE_URL         | PostgreSQL connection URL         | postgresql://user:pass@localhost:5432/db  |
| JWT_SECRET_KEY       | Secret key for JWT token generation| your_jwt_secret_key_here                  |
| REDIS_HOST           | Redis host for caching            | localhost                                 |
| REDIS_PORT           | Redis port for caching            | 6379                                      |

#### Create Your `.env` File
1. Copy the example:
   ```bash
   cp .env.example .env
   ```
2. Fill in the appropriate values.

## API Endpoints
### Auth Service
| Endpoint            | Method   | Description                     |
|---------------------|----------|---------------------------------|
| /auth/register      | POST     | Register a new user (default: user)|
| /auth/login         | POST     | Authenticate user and get a token |
| /auth/logout        | POST     | Logout and invalidate the token   |
| /auth/create_role   | POST     | Admin-only: Create new roles      |

## Development Guidelines
1. Coding Standards:
   - Follow PEP 8 for Python code.
   - Use meaningful variable and function names.

2. Testing:
   - Use `pytest` for testing:
     ```bash
     pytest
     ```

3. Linting:
   - Use `flake8` for linting:
     ```bash
     flake8 .
     ```

4. Version Control:
   - Keep the `.env` file in `.gitignore`.
   - Commit changes to feature branches before merging.

5. Documentation:
   - Add docstrings to all functions and classes.
