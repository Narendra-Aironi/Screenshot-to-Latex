#!/bin/bash

# Wrapper script for ssToLatex.py to work with Apple Shortcuts
# This script sets up the proper environment and paths

# Set PATH to include common Python locations
export PATH="/Library/Frameworks/Python.framework/Versions/3.13/bin:/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin:$PATH"

# Set the Google API key - REPLACE WITH YOUR ACTUAL API KEY
export GOOGLE_API_KEY="Your API key"

# Change to the script directory
cd "/Users/narendraaironi/projects/ai"

# Run the Python script with full path
/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 ssToLatex.py

# Exit with the same code as the Python script
exit $?
