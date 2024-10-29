# FastAPI Scaffold with Request Limiter and Testing Utilities

This repository provides a scaffold to set up FastAPI with a request limiter and testing utilities using Locust to simulate the performance of your API.

## Getting Started

### Prerequisites

- Python 3.8 - 3.12
- Docker (optional, for using the devcontainer)

### Setup

You can set up the project using a development container or a virtual environment.

#### Using Devcontainer

1. Open the project in Visual Studio Code.
2. Use the container configuration in [`.devcontainer/devcontainer.json`](fastapi_scaffold/.devcontainer/devcontainer.json).
3. The container will automatically install the required dependencies specified in `requirements.txt`.

#### Using Virtual Environment:

1. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
2. Activate the virtual environment:
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

You can use the Makefile to start the FastAPI server and the Locust web interface.

- To start the FastAPI server:
    ```sh
    make start_fastapi
    ```
- To start the Locust web interface:
    ```sh
    make start_locust
    ```

### Project Structure
