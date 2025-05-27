# Stock Trading FAQ Assistant

This project implements a Stock Trading FAQ Assistant using RAG (Retrieval Augmented Generation) with a PostgreSQL database and pgvector for storing and querying vector embeddings. It allows users to search for frequently asked questions related to stock trading using natural language and retrieves the most relevant answers based on semantic similarity. Search results include the question and answer, along with metadata such as category, creation date, and similarity score.

## Streamlit Application
![Streamlit App GUI 1](images/app_1.png)
![Streamlit App GUI 2](images/app_2.png)
This project includes a user-friendly web interface built with Streamlit for the Stock Trading FAQ Assistant. You can interact with the search functionality through this application.

## Database Structure (TablePlus Example)
![TablePlus Embeddings Table](images/tableplus.png)
The project uses a PostgreSQL database with the `pgvector` extension to store vector embeddings for the FAQ data. Below is an example view of the `embeddings` table in TablePlus:



## Getting Started

Follow these steps to set up and run the Stock Trading FAQ Assistant locally:

1.  **Clone your repository:**

    ```bash
    git clone https://github.com/seonokkim/rag-pgvector.git
    cd rag-pgvector
    ```

2.  **Set up environment variables:**

    Create a `.env.local` file in the root directory of the project. Copy the contents from `.env.example` (if it exists) and update the variables, especially the database connection string and any API keys (e.g., `OPENAI_API_KEY`).

    ```dotenv
    # Example variables (adjust as needed)
    DATABASE_URL="postgresql://user:password@localhost:5432/mydatabase"
    OPENAI_API_KEY="your_openai_api_key"
    ```

3.  **Start Docker containers:**

    Use Docker Compose to start the PostgreSQL database container.

    ```bash
    docker-compose up -d
    ```

    Wait a few moments for the database to initialize.

4.  **Install dependencies:**

    Install the project dependencies using npm.

    ```bash
    npm install
    ```

5.  **Set up the database schema and run migrations:**

    Apply the database schema and run any pending migrations using Prisma.

    ```bash
    npx prisma migrate dev
    ```

6.  **Ingest FAQ data:**

    Run the data ingestion script to load FAQ data into the database. This step might vary depending on where the ingestion script is located and how it's run.

    ```bash
    # Example: Assuming an ingest script in the 'scripts' directory
    npx ts-node scripts/ingest.ts
    ```
    *Note: The exact command for data ingestion might differ based on the project structure.*

7.  **Run the application:**

    Start the development server.

    ```bash
    npm run dev
    ```

    The application should now be running and accessible, likely at `http://localhost:3000` or similar.

## Running the Streamlit Application

To run the Streamlit application, follow these steps:

1.  **Install Streamlit:**

    If you haven't already, install Streamlit using pip.

    ```bash
    pip install streamlit
    ```

2.  **Run the Streamlit app:**

    Navigate to the directory containing the Streamlit app file (e.g., `app.py`) and run the following command:

    ```bash
    streamlit run app.py
    ```

    The Streamlit app should now be running and accessible in your web browser, typically at `http://localhost:8501`.


## License

This project is licensed under the MIT License - see the [LICENCE](LICENCE) file for details.


## Acknowledgments

This project is based on the code from [daveebbelaar/pgvectorscale-rag-solution](https://github.com/daveebbelaar/pgvectorscale-rag-solution).