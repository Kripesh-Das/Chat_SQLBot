# LangChain: Chat with SQL DB
# Link to the deployed model on streamlit https://sqlbotkd.streamlit.app/
This project demonstrates how to use LangChain to create a chat interface with a SQL database using Streamlit. The application allows users to interact with either a local SQLite database or a remote MySQL database.

## Project Structure

- `app.py`: Main application file that sets up the Streamlit interface and handles user interactions.
- `sqlite.py`: Script to set up and populate the SQLite database.
- `requirements.txt`: List of dependencies required for the project.
- `.gitignore`: Specifies files and directories to be ignored by Git.

1. Run the Streamlit application:

    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Choose the database you want to interact with from the sidebar:
    - **Use SQLLite 3 Database- Student.db**: Interact with the local SQLite database.
    - **Connect to your MySQL Database**: Provide MySQL connection details to interact with a remote MySQL database.

4. Enter your GRoq API Key in the sidebar.

5. Start chatting with the database by entering your queries in the chat input.

## Dependencies

- streamlit
- pathlib
- langchain
- langchain_groq
- sqlalchemy
- langchain_community
- mysql-connector-python
