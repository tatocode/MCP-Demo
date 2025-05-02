# MCP-Demo

This repository contains a minimal version of an MCP demo. The project is designed to demonstrate the basic functionality of an MCP service and client using the `qwen` API interface.

## Features

- Lightweight and minimal implementation.
- Dependency management using `uv`.
- Integration with the `qwen` API.

## Prerequisites

Before using this repository, ensure you have the following installed:

- Python 3.10 or higher
- `uv` package manager

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/tatocode/MCP-Demo.git
    cd MCP-Demo
    ```

2. Install dependencies using `uv`:
    ```bash
    uv sync
    ```

3. Create a `.env` file in the root directory of the project and add your API key:
    ```
    API-KEY=xxxx
    ```

    Replace `xxxx` with your actual API key for the `qwen` API.

4. Run the project:
    ```bash
    uv run main.py mcp_server.py
    ```

## Notes

- The `.env` file is required to ensure the project runs correctly. Do not share your API key publicly.
- For more information about the `qwen` API, refer to its official documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.
