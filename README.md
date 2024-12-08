# Ollama Structured Outputs Demonstration

This repository showcases how to leverage the `ollama` and `pydantic` libraries to perform tasks such as fetching structured data, extracting information, and analyzing images. Each example is designed to be self-contained, making it an excellent resource for learners to understand and experiment with these powerful Python libraries.

## Table of Contents

- [Introduction](#introduction)
- [Pre-requisites](#pre-requisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running the Examples](#running-the-examples)
  - [Run JSON Output Demo](#run-json-output-demo)
  - [Run Data Extraction Demo](#run-data-extraction-demo)
  - [Run Image Description Demo](#run-image-description-demo)
  - [Run All Examples](#run-all-examples)
- [Clean Up](#clean-up)
- [References](#references)
- [License](#license)

## Introduction

The **Ollama Structured Outputs Demonstration** project is an educational resource aimed at illustrating how to use the `ollama` library in conjunction with `pydantic` to generate, validate, and manage structured data. Through a series of focused examples, users can learn to:

- Fetch and validate structured information about specific topics.
- Extract and organize data from unstructured inputs.
- Analyze and describe image content programmatically.

Each example is encapsulated in its own script, ensuring clarity and ease of understanding. Whether you're a beginner looking to grasp the basics or an experienced developer seeking to refine your skills, this project provides valuable insights and practical applications.

## Pre-requisites

Before setting up and running the project, ensure you have the following prerequisites:

1. **Ollama Installed**

   - **Installation Guide:** Follow the official [Ollama Download Instructions](https://ollama.com/download) to install the `ollama` CLI on your system.

2. **Ollama Server Running**

   - **Start the Server:** Ensure the Ollama server is running. You can start it using the command:

     ```bash
     ollama serve
     ```

   - **Verification:** After starting, verify that the server is running by accessing the Ollama dashboard or using appropriate CLI commands.

3. **Required Models Pulled**

   - **Llama 3.2 Model:**

     ```bash
     ollama pull llama3.2
     ```

   - **Llava Model:**

     ```bash
     ollama pull llava
     ```

   - **Ensure Models Are Available:** Confirm that both `llama3.2` and `llava` models are successfully pulled and available in your local Ollama setup.

## Project Structure

```
ollama-structured-outputs/
│
├── Makefile
├── README.md
├── requirements.txt
├── .gitignore.txt
├── LICENSE
├── src/
│   ├── all_examples.py
│   ├── data_extraction.py
│   ├── image_description.py
│   ├── json_output.py
│   └── images/
│       └── image-01.png
│
└── venv/
```

- **Makefile**: Automates setup and execution tasks.
- **requirements.txt**: Lists Python dependencies.
- **src/**: Contains all example scripts and resources.
  - **json_output.py**: Fetches and validates book details.
  - **data_extraction.py**: Generates and validates a recipe.
  - **image_description.py**: Analyzes and describes image content.
  - **all_examples.py**: Runs all demos sequentially.
  - **images/**: Stores image files used in demonstrations.
- **venv/**: Python virtual environment directory (created automatically).

## Setup Instructions

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**

   ```bash
   git clone <your_repository_url>
   cd ollama-structured-outputs
   ```

   _Replace `<your_repository_url>` with the actual URL of your repository._

2. **Install Dependencies**

   The project utilizes a `Makefile` to streamline setup and execution. Use the following command to create a virtual environment and install all necessary dependencies:

   ```bash
   make install
   ```

   **What It Does:**

   - **Creates a Virtual Environment**: If one doesn't already exist.
   - **Activates the Virtual Environment**: Ensures dependencies are installed in an isolated environment.
   - **Upgrades `pip`**: Ensures the latest package installer is used.
   - **Installs Dependencies**: Based on `requirements.txt`.
   - **Updates the `ollama` Library**: Ensures you have the latest version.

## Running the Examples

Each example script demonstrates a specific functionality. You can run them individually using the provided Makefile targets.

### Run JSON Output Demo

**Script:** `json_output.py`

**Purpose:** Fetches details about the book "1984" by George Orwell using the `ollama` chat service and validates the response using `pydantic`.

**Command:**

```bash
make run-json_output
```

**What It Does:**

- Sends a request to the `ollama` model to retrieve information about the specified book.
- Validates the received JSON response against a predefined `Book` model.
- Prints the validated book information to the console.

### Run Data Extraction Demo

**Script:** `data_extraction.py`

**Purpose:** Generates a detailed spaghetti carbonara recipe based on provided instructions using `ollama` and validates the structured data with `pydantic`.

**Command:**

```bash
make run-data_extraction
```

**What It Does:**

- Sends a recipe request to the `ollama` model.
- Extracts ingredients, steps, and timing from the generated recipe.
- Validates the structured recipe data using the `Recipe` model.
- Prints the validated recipe details to the console.

### Run Image Description Demo

**Script:** `image_description.py`

**Purpose:** Analyzes an image to describe its content, including objects, scene, colors, and text, using `ollama` and `pydantic`.

**Command:**

```bash
make run-image_description
```

**What It Does:**

- Sends the specified image (`image-01.png`) to the `ollama` model for analysis.
- Extracts details such as detected objects, scene description, colors, time of day, setting, and any text present.
- Validates the structured image description using the `ImageDescription` model.
- Prints the validated image description to the console.

### Run All Examples

**Script:** `all_examples.py` _(Optional)_

**Purpose:** Executes all demonstration scripts sequentially, providing a comprehensive overview of the project's capabilities.

**Command:**

```bash
make run-all_examples
```

**What It Does:**

- Runs `json_output.py`, `data_extraction.py`, and `image_description.py` in sequence.
- Prints outputs of each demo with clear separators for readability.

_Note: The `all_examples.py` script is optional. Use it if you want to run all demos in one go._

## Clean Up

To remove the virtual environment and all installed dependencies, use the following command:

```bash
make clean
```

**What It Does:**

- Deletes the `venv/` directory, effectively removing the virtual environment and all installed packages.
- Useful for resetting the project environment or freeing up disk space.

_Note: Running `make clean` does not delete your source code or images._

## References

- **Source:** [Ollama Structured Outputs](https://ollama.com/blog/structured-outputs)
- **Article:** [A Practical Guide to Using Ollama Structured JSON Output](https://lucianoayres.github.io/blog/2024/12/08/A-Practical-Guide-to-Using-Ollama-Structured-JSON-Output.html)

## License

This project is licensed under the [MIT License](LICENSE).
