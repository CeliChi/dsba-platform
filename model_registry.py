import os
from datetime import datetime
from get_path import get_logs_dir

def register_model(model_path):
    # Store the registry log as a .txt file
    REGISTRY_FILE = get_logs_dir() / "model_registry.txt"
    version = 1

    # If the file already exists, count lines to get next version number
    if os.path.exists(REGISTRY_FILE):
        with open(REGISTRY_FILE, "r") as f:
            lines = [line for line in f if line.startswith("Version")]
            version = len(lines) + 1

    # Create registry line
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (
        f"Version {version}\n"
        f"Path: {model_path}\n"
        f"Registered at: {timestamp}\n"
        f"{'-'*40}\n"
    )

    # Append to file
    with open(REGISTRY_FILE, "a") as f:
        f.write(log_entry)

    print(f"Registered model version {version}")
    print(f"Log saved to: {REGISTRY_FILE}")
