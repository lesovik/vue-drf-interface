# Vue-DRF Interface

A dynamic single-page application (SPA) built with Vue 3 and Django REST Framework (DRF) that provides an editable, sortable tabular interface for interacting with RESTful endpoints.

## Features

- **Dynamic Endpoint Discovery**: Automatically detects and integrates exposed endpoints from the DRF backend.
- **CRUD Operations**: Supports creating, reading, updating, and deleting objects with client-side and server-side validation.
- **Pagination**: Efficiently handles large datasets with seamless pagination.
- **Field Handling**: Manages 'choices' fields and foreign key relationships with search-select functionality.
- **Responsive Design**: Utilizes Bootstrap CSS for a clean and responsive user interface.

## Screenshots


![Tabular View](screenshots/main.png)
*Particular endpoint editing*

## Installation

### Prerequisites

- **Backend**: Ensure you have Python and Docker installed.
- **Frontend**: Node.js and npm are required.

### Backend Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/lesovik/vue-drf-interface.git
   cd vue-drf-interface
   ```

2. **Navigate to Backend Directory**:

   ```bash
   cd django-docker
   ```

3. **Build and Run Docker Containers**:

   ```bash
   docker-compose up --build
   ```

   This command sets up the Django application with PostgreSQL.

4. **Apply Migrations**:

   In a new terminal, run:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Create Superuser (Optional)**:

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

6. **Access the Application**:

   The backend API will be available at `http://localhost:8000/`.

### Frontend Setup

1. **Navigate to Frontend Directory**:

   ```bash
   cd ../vue-front-end
   ```

2. **Install Dependencies**:

   ```bash
   npm install
   ```

3. **Configure Environment Variables**:

   Create a `.env` file in the `vue-front-end` directory with the following content:

   ```
   VUE_APP_API_BASE_URL=http://localhost:8000/api/
   ```

4. **Run the Development Server**:

   ```bash
   npm run serve
   ```

5. **Access the Frontend Application**:

   Navigate to `http://localhost:8080/` in your browser.

## Usage

- **Navigating Endpoints**: The application automatically lists available endpoints. Use the navigation menu to access different datasets.
- **Editing Entries**: Click on edit button on any row to edit its details. Fields are dynamically generated based on the backend's OPTIONS response.
- **Adding New Entries**: Use the 'Add New' button to create a new record.
- **Deleting Entries**: Select the delete option corresponding to the entry you wish to remove.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

#### To Do
  
 - complex relationship field editing on the front end
   - unit tests
   - ie. many-to-many, many-to-one and more complex relationship, file fields etc.
   - Token based authentication
   - roles & permissions
   - connection error handling
   
