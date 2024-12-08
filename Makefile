# Define variables
PYTHON = python3
VENV_DIR = venv
REQUIREMENTS = requirements.txt
SRC_DIR = src

# List of example scripts (without .py extension)
EXAMPLES = json_output data_extraction image_description

# Default target
.PHONY: all
all: install

# Create virtual environment
.PHONY: venv
venv:
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Creating virtual environment..."; \
		$(PYTHON) -m venv $(VENV_DIR); \
	else \
		echo "Virtual environment already exists."; \
	fi

# Install Python requirements and update Ollama library
.PHONY: install
install: venv
	@echo "Activating virtual environment and installing/updating requirements..."
	. $(VENV_DIR)/bin/activate && pip install --upgrade pip && pip install -r $(REQUIREMENTS) && pip install -U ollama

# Run json_output.py
.PHONY: run-json_output
run-json_output: install
	@echo "Running json_output.py..."
	. $(VENV_DIR)/bin/activate && $(PYTHON) $(SRC_DIR)/json_output.py

# Run data_extraction.py
.PHONY: run-data_extraction
run-data_extraction: install
	@echo "Running data_extraction.py..."
	. $(VENV_DIR)/bin/activate && $(PYTHON) $(SRC_DIR)/data_extraction.py

# Run image_description.py
.PHONY: run-image_description
run-image_description: install
	@echo "Running image_description.py..."
	. $(VENV_DIR)/bin/activate && $(PYTHON) $(SRC_DIR)/image_description.py

# Run all_examples.py
.PHONY: run-all_examples
run-all_examples: install
	@echo "Running all_examples.py..."
	. $(VENV_DIR)/bin/activate && $(PYTHON) $(SRC_DIR)/all_examples.py

# Clean up virtual environment
.PHONY: clean
clean:
	@echo "Cleaning up virtual environment..."
	rm -rf $(VENV_DIR)

# Display help information
.PHONY: help
help:
	@echo "Available Makefile targets:"
	@echo "  all                    : Install dependencies."
	@echo "  install                : Create virtual environment and install dependencies."
	@echo "  run-json_output        : Run the json_output.py script."
	@echo "  run-data_extraction    : Run the data_extraction.py script."
	@echo "  run-image_description  : Run the image_description.py script."
	@echo "  run-all_examples       : Run the all_examples.py script."
	@echo "  clean                  : Remove the virtual environment."
	@echo "  help                   : Display this help message."
