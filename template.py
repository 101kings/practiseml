import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name="mlproject"
# List of required files and folders to create
list_of_files = [
    ".github/workflows/.gitkeep",  # Keeps GitHub Actions workflows folder in Git
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", 
    "schema.yaml",
    "main.py",
    "app.py",                                                                                                # Main configuration file
    "dvc.yaml",                       # DVC pipeline file
    "params.yaml",                    # Hyperparameters and settings
    "requirements.txt",              # Python dependencies
    "setup.py",                      # For packaging the project
    "research/trial.ipynb",           # Jupyter notebook for experiments
    "templates/index.html"                  
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedr, filename = os.path.split(filepath)

    if filedr != "":
        os.makedirs(filedr, exist_ok=True)
        logging.info(f"Creating directory: {filedr} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create empty file
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")