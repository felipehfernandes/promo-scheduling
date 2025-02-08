#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install

# Return to root directory
cd ..
