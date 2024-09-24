# Java Project Metrics Analyzer for GitHub Repositories
This tool analyzes GitHub repositories to extract various metrics for Java projects. <br>
It uses a Java-based analyzer to retrieve key metrics such as the number of files, blank lines, comment lines, code lines, classes, and methods in a repository.

## Features
- **Java-only project analysis**: Designed specifically for analyzing Java projects hosted on GitHub.
- **Key metrics extracted**: The tool retrieves information such as:
  - Number of files
  - Blank lines
  - Comment lines
  - Code lines
  - Classes
  - Method declarations
  - Method invocations
  - Javadoc counts (methods and overall)

## Requirements
- **Docker**: Ensure that Docker and Docker Compose are installed on your machine.<br>
  - Docker: https://docs.docker.com/get-docker/ <br>
  - Docker Compose: https://docs.docker.com/compose/install/ <br>
- **Python 3.x**: The Flask app runs on Python, and dependencies are managed using requirements.txt.

## Setup Instructions
1. **Clone the repository**:
    ```
    git clone https://github.com/ibu00024/java-project-metrics-analyzer.git
    cd java-project-metrics-analyzer
    ```

2. **Build and start the Docker containers**:<br>
    The application uses Docker Compose to set up two services:
    - **web**: The Flask-based frontend that allows users to input GitHub repository URLs.
    - **java-analyzer**: A Java service that performs the metrics analysis using [cmajava](https://github.com/ibu00024/cmajava).
    
    To build and run the containers:
    ```
    docker-compose up --build
    ```
    This command builds the images for both the web and java-analyzer services and starts the application. <br>
    The web interface will be available on http://localhost:5001.

3. **Access the Web Interface**:<br>
    Once the containers are running, visit http://localhost:5001 in your browser. <br>
    Enter the GitHub repository URL of a Java project and click the "Analyze" button to retrieve metrics.

## Usage
1. **Enter GitHub repository URL**:
   - Go to the web interface (http://localhost:5001).
   - Input the GitHub repository URL (Java-only).
   - Click the "Analyze" button.
2. **View the metrics**:
   - The tool will display the various metrics for the analyzed repository.

## Dependencies
- **Flask**: The web framework used for the frontend.
- **GitPython**: Used for cloning GitHub repositories.
- **Java Runtime**: Required for running the Java-based analyzer.

All dependencies are managed via Docker, so no need to install them manually.