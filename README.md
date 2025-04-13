# RecApp - Personalized Recommendation Engine 

![App Logo](./frontend/public/images/applogo.png) 


A full-stack web application that provides personalized content or product recommendations based on user preferences. The backend is built with Django & Django REST Framework, the frontend with Vue.js & Tailwind CSS, and deployed using free-tier cloud services.

## Live Demo

🚀 **Try the live application here:** [https://recengineapp.netlify.app/](https://recengineapp.netlify.app/)

## Screenshots

**Homepage:**
![Homepage Screenshot](./frontend/public/images/homepage.jpeg) 

**Recommendations Page:**
![Recommendations Screenshot](./frontend/public/images/recommendationspage.jpeg)

## Features Implemented

*   **Backend API:** Built with Django and Django REST Framework.
    *   Endpoints for fetching categories and recommendations.
    *   Basic recommendation logic based on preferred category.
*   **Frontend Interface:** Built with Vue 3 and styled with Tailwind CSS.
    *   Responsive design for desktop, tablet, and mobile.
    *   Homepage with video background hero section.
    *   Form to select preferred category.
    *   Display area for fetched recommendations.
    *   Vue Router for SPA navigation.
    *   Axios for API communication.
*   **Deployment:**
    *   Backend hosted on PythonAnywhere (Free Tier) with MySQL database.
    *   Frontend hosted on Netlify (Free Tier).
    *   Continuous deployment via Git integration.

## Tech Stack

*   **Backend:**
    *   Python 3
    *   Django
    *   Django REST Framework (DRF)
    *   Gunicorn (WSGI Server)
    *   dj-database-url (Database URL parsing)
    *   mysqlclient (MySQL driver)
    *   Whitenoise (Static file serving)
*   **Frontend:**
    *   Vue.js (Vue 3)
    *   Vue Router
    *   Axios
    *   Tailwind CSS
    *   PostCSS / Autoprefixer
*   **Database:**
    *   MySQL (on PythonAnywhere Free Tier)
    *   SQLite3 (for local development)
*   **Deployment:**
    *   **Backend:** PythonAnywhere
    *   **Frontend:** Netlify
    *   **Version Control:** Git & GitHub

## Getting Started (Local Development)

Follow these instructions to set up the project locally for development and testing.

**Prerequisites:**

*   Python 3.8+ and Pip
*   Node.js and npm (or yarn)
*   Git
*   MySQL Client library (optional, only if you want to connect to MySQL locally, otherwise SQLite is used by default)

**Installation & Setup:**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Garbii1/recommendation-engine-project.git
    cd recommendation-engine-project
    ```

2.  **Backend Setup (Django):**
    *   Navigate to the backend directory:
        ```bash
        cd backend
        ```
    *   Create and activate a Python virtual environment:
        ```bash
        python -m venv venv
        # Linux/macOS:
        source venv/bin/activate
        # Windows (cmd/powershell):
        .\venv\Scripts\activate
        ```
    *   Install backend dependencies:
        ```bash
        pip install -r requirements.txt
        ```
    *   Run database migrations (this will create the `db.sqlite3` file by default):
        ```bash
        python manage.py migrate
        ```
    *   Create a superuser for the admin interface (optional):
        ```bash
        python manage.py createsuperuser
        ```
    *   *(Optional: To use MySQL locally, set the `DATABASE_URL` environment variable before running migrations/runserver, e.g., `export DATABASE_URL='mysql://user:pass@host/dbname'`)*

3.  **Frontend Setup (Vue):**
    *   Navigate to the frontend directory (from the project root):
        ```bash
        cd ../frontend
        # Or just `cd frontend` if already in the root
        ```
    *   Install frontend dependencies:
        ```bash
        npm install
        ```
    *   Create a `.env` file in the `frontend` directory:
        ```env
        # frontend/.env
        VUE_APP_API_URL=http://127.0.0.1:8000/api
        ```
        *(This tells the frontend dev server where the local backend API is)*

**Running Locally:**

1.  **Start the Backend Server:**
    *   Open a terminal in the `backend` directory (with the virtualenv activated).
    *   Run:
        ```bash
        python manage.py runserver
        ```
    *   The backend API will be available at `http://127.0.0.1:8000/api/`.

2.  **Start the Frontend Development Server:**
    *   Open a *separate* terminal in the `frontend` directory.
    *   Run:
        ```bash
        npm run serve
        ```
    *   The frontend application will be available at `http://localhost:8080` (or another port if 8080 is busy).

3.  Open `http://localhost:8080` in your browser.

## API Endpoints Overview

*   **`GET /api/categories/`**: Retrieves a list of available item categories.
    *   Response: `{"categories": [{"value": "CategoryValue", "label": "CategoryLabel"}, ...]}`
*   **`GET /api/items/`**: Retrieves a list of all available items (optional endpoint).
    *   Response: `{"items": [{"id": ..., "name": ..., "description": ..., "category": ..., "image_url": ...}, ...]}`
*   **`POST /api/recommendations/`**: Submits user preferences and retrieves recommendations.
    *   Request Body: `{ "preferred_category": "CategoryName" }`
    *   Success Response (200): `{"recommendations": [ {item_object}, {item_object}, ... ]}`
    *   Error Response (400): Validation errors if input is invalid.

## Deployment Notes

*   **Backend (PythonAnywhere):**
    *   Configured via WSGI file (`/var/www/yourusername_pythonanywhere_com_wsgi.py`).
    *   Uses a virtual environment managed by `virtualenvwrapper`.
    *   MySQL database configured via `DATABASE_URL` environment variable set in WSGI file.
    *   Static files are collected using `python manage.py collectstatic` and served via PythonAnywhere's static file mapping configuration (`/static/` mapped to `/home/Garbii/recommendation-engine-project/backend/staticfiles`).
    *   Environment variables (`SECRET_KEY`, `DATABASE_URL`, `ALLOWED_HOSTS`, `FRONTEND_URL`, `DEBUG=False`) set directly in the WSGI file.
*   **Frontend (Netlify):**
    *   Build settings configured for `frontend` base directory, `npm run build` command, and `frontend/dist` publish directory.
    *   Environment variable `VUE_APP_API_URL` set in Netlify UI pointing to the live PythonAnywhere API URL (`https://garbii.pythonanywhere.com/api`).
    *   SPA routing handled by `frontend/public/_redirects` file.

## Challenges Faced & Solutions

*   **Heroku Free Tier Removal:** Migrated backend deployment from Heroku to PythonAnywhere's free tier.
*   **Database Setup (PythonAnywhere):** Switched from PostgreSQL (paid) to MySQL (free tier available). Required changing the DB driver (`psycopg2-binary` -> `mysqlclient`) and updating `DATABASE_URL`.
*   **Environment Variables (PythonAnywhere):** As the free tier lacked a GUI for env vars, they were set directly within the WSGI file using `os.environ`.
*   **Running `manage.py` Commands (PythonAnywhere):** Console commands like `migrate` and `createsuperuser` required prefixing with the `DATABASE_URL` environment variable to connect to MySQL instead of the default SQLite.
*   **Static Files (`collectstatic` & Manifest):** Encountered `Missing staticfiles manifest entry` errors for the admin. This was resolved by ensuring `collectstatic` ran correctly after all installations and configuration changes. A temporary workaround involved switching `STATICFILES_STORAGE` to the non-manifest version (`whitenoise.storage.CompressedStaticFilesStorage`), confirming the base setup worked, before ensuring the manifest version could run `collectstatic` properly (by removing the `staticfiles` dir and running `collectstatic` clean). Ultimately, the non-manifest storage (`CompressedStaticFilesStorage`) was used for stability.
*   **CORS:** Required careful configuration in Django (`settings.py` using `django-cors-headers` and reading `FRONTEND_URL` from env var) and setting the `FRONTEND_URL` in the PythonAnywhere WSGI file.
*   **Vue CLI Environment Variables:** Corrected usage from Vite's `import.meta.env` to Vue CLI's `process.env` (prefixed with `VUE_APP_`).

## Future Improvements

*   **User Authentication:** Implement user registration and login (e.g., using Django Allauth).
*   **Interaction History:** Store user interactions (clicks, ratings, purchases) to improve recommendations.
*   **Advanced Algorithms:** Implement more sophisticated recommendation techniques:
    *   **Collaborative Filtering:** Using user-item interaction data (requires user history).
    *   **Content-Based Filtering:** Using item metadata (descriptions, tags) and user profiles.
*   **UI/UX Enhancements:**
    *   Add loading indicators during API calls.
    *   Improve error handling and display user-friendly messages.
    *   Implement pagination or infinite scrolling for results.
    *   Add item detail pages.
*   **Testing:** Add unit and integration tests for both backend and frontend.
*   **Containerization:** Dockerize the application for easier setup and deployment consistency.
*   **Data Visualization & Dashboards:**
    *   **Admin Dashboard:** Create a section (potentially using the Django Admin or a separate interface) to visualize key metrics:
        *   Most popular items/content.
        *   User engagement rates (e.g., click-through rate on recommendations).
        *   Recommendation algorithm performance (e.g., precision, recall).
        *   User cohort analysis.
 *   **User-Facing Visualization (Optional):** Implement features explaining *why* an item was recommended (e.g., "Because you liked X", "Similar users also liked Y", "Based on your interest in Z category"). Could involve simple tags or more complex visualizations.
    *   Utilize charting libraries (e.g., Chart.js, Plotly, D3.js on the frontend; Matplotlib/Seaborn on the backend for generating static charts/reports).
*   **Integration Capabilities:**
    *   Design the API to be easily integrated into existing e-commerce platforms or content streaming services.
    *   Consider providing embeddable widgets or SDKs.        

## Author

*   **Muhammed Babatunde Garuba**
*   GitHub: [@Garbii1](https://github.com/Garbii1)
*   Feel free to reach out with any questions or feedback!

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

