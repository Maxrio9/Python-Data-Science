#!/bin/bash

# Set variables
DEV_DIR="C:/Users/lasse/Documents/Coding/Git Reposetory/subscriber-pipeline-starter-kit/dev"
PROD_DIR="$DEV_DIR/production"
PYTHON_SCRIPT="$DEV_DIR/script.py"
CHANGELOG="$DEV_DIR/changelog.txt"
ERROR_LOG="$DEV_DIR/error_log.txt"
BASH_LOG="$DEV_DIR/bash_script.log"

# Set the full path to your Python executable
PYTHON_PATH="/c/Users/lasse/AppData/Local/Programs/Python/Python312/python.exe"
# Function to log messages
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$BASH_LOG"
}

# Function to check if an update occurred
check_for_update() {
    if grep -q "Database updated successfully" "$CHANGELOG"; then
        return 0  # Update occurred
    else
        return 1  # No update
    fi
}

# Function to move files
move_files() {
    local files=("analytics_ready.db" "analytics_ready.csv")
    for file in "${files[@]}"; do
        if [ -f "$DEV_DIR/$file" ]; then
            mv "$DEV_DIR/$file" "$PROD_DIR/$file"
            log_message "Moved $file to production directory"
        else
            log_message "Warning: $file not found in dev directory"
        fi
    done
}

# Main execution
log_message "Starting script execution"

# Change to dev directory
cd "$DEV_DIR" || { log_message "Error: Unable to change to dev directory"; exit 1; }

# Run Python script
log_message "Running Python script"
py "$PYTHON_SCRIPT"

# Check for errors in Python script execution
if grep -q "ERROR" "$ERROR_LOG"; then
    log_message "Error detected in Python script execution. Check error_log.txt for details."
    exit 1
fi

# Check if an update occurred
if check_for_update; then
    log_message "Update detected. Moving files to production."
    move_files
else
    log_message "No update detected. No files moved."
fi

log_message "Script execution completed"