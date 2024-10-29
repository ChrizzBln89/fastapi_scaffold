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

. ├── .devcontainer/ │ └── devcontainer.json ├── .github/ │ └── dependabot.yml ├── .pytest_cache/ │ ├── CACHEDIR.TAG │ ├── README.md │ └── v/ │ └── cache/ │ ├── lastfailed │ ├── nodeids │ └── stepwise ├── pycache/ ├── Dockerfile ├── gradie ├── locustfile.py ├── main.py ├── Makefile ├── readme.md ├── requirements.txt ├── routers/ │ ├── pycache/ │ ├── limiter.py │ └── router.py └── test_api.py


### Configuration

The devcontainer is configured in `.devcontainer/devcontainer.json`. It uses the [`mcr.microsoft.com/devcontainers/python:1-3.10-bullseye`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2Ffastapi_scaffold%2F.devcontainer%2Fdevcontainer.json%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A11%7D%7D%5D%2C%227c8db291-4cc5-4e5d-8ffe-ef1537cccf2c%22%5D "Go to definition") image and installs the dependencies listed in [requirements.txt](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fworkspaces%2Ffastapi_scaffold%2Frequirements.txt%22%2C%22scheme%22%3A%22vscode-remote%22%2C%22authority%22%3A%22dev-container%2B7b22686f737450617468223a222f686f6d652f63687269732f636f64652f666173746170695f73636166666f6c64222c226c6f63616c446f636b6572223a66616c73652c2273657474696e6773223a7b22636f6e74657874223a226465736b746f702d6c696e7578227d2c22636f6e66696746696c65223a7b22246d6964223a312c22667350617468223a222f686f6d652f63687269732f636f64652f666173746170695f73636166666f6c642f2e646576636f6e7461696e65722f646576636f6e7461696e65722e6a736f6e222c2265787465726e616c223a2266696c653a2f2f2f686f6d652f63687269732f636f64652f666173746170695f73636166666f6c642f2e646576636f6e7461696e65722f646576636f6e7461696e65722e6a736f6e222c2270617468223a222f686f6d652f63687269732f636f64652f666173746170695f73636166666f6c642f2e646576636f6e7461696e65722f646576636f6e7461696e65722e6a736f6e222c22736368656d65223a2266696c65227d7d%22%7D%7D) after the container is created.

### FastAPI Setup

The FastAPI application is set up in [main.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fworkspaces%2Ffastapi_scaffold%2Fmain.py%22%2C%22scheme%22%3A%22vscode-remote%22%2C%22authority%22%3A%22dev-container%2B7b22686f737450617468223a222f686f6d652f63687269732f636f64652f666173746170695f73636166666f6c64222c226c6f63616c446f636b6572223a66616c73652c2273657474696e6773223a7b22636f6e74657874223a226465736b746f702d6c696e7578227d2c22636f6e66696746696c65223a7b22246d6964223a312c22667350617468223a222f686f6d652f63687269732f636f64652f666173746170695f73636166666f6c642f2e646576636f6e7461696e65722f646576636f6e7461696e65722e6a736f6e222c2265787465726e616c223a2266696c653a2f2f2f686f6d652f63687269732f636f64652f666173746170695f73636166666f6c642f2e646576636f6e7461696e65722f646576636f6e7461696e65722e6a736f6e222c2270617468223a222f686f6d652f63687269732f636f64652f666173746170695f73636166666f6c642f2e646576636f6e7461696e65722f646576636f6e7461696e65722e6a736f6e222c22736368656d65223a2266696c65227d7d%22%7D%7D). It includes:

- CORS middleware configuration
- Request limiter using [`slowapi`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2Ffastapi_scaffold%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A5%7D%7D%5D%2C%227c8db291-4cc5-4e5d-8ffe-ef1537cccf2c%22%5D "Go to definition")
- Example routes with rate limiting

### Testing with Locust

Locust is used to simulate the performance of your API. The configuration for Locust is in [locustfile.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fworkspaces%2Ffastapi_scaffold%2Flocustfile.py%22%2C%22scheme%22%3A%22vscode-remote%22%2C%22authority%22%3A%22dev-container%2B7b22686f737450617468223a222f686f6d652f63687269732f636f64652f666173746170695f73636166666f6c64222c226c6f63616c446f636b6572223a66616c73652c2273657474696e6773223a7b22636f6e74657874223a226465736b746f702d6c696e7578227d2c22636f6e66696746696c65223a7b22246d6964223a312c22667350617468223a222f686f6d652f63687269732f636f64652f666173746170695f73636166666f6c642f2e646576636f6e7461696e65722f646576636f6e7461696e65722e6a736f6e222c2265787465726e616c223a2266696c653a2f2f2f686f6d652f63687269732f636f64652f666173746170695f73636166666f6c642f2e646576636f6e7461696e65722f646576636f6e7461696e65722e6a736f6e222c2270617468223a222f686f6d652f63687269732f636f64652f666173746170695f73636166666f6c642f2e646576636f6e7461696e65722f646576636f6e7461696e65722e6a736f6e222c22736368656d65223a2266696c65227d7d%22%7D%7D).

## License

This project is licensed under the MIT License - see the LICENSE file for details.