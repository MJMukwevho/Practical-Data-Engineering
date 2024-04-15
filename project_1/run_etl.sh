#!/bin/bash

# Build pytest container if not exist
docker build -t pytest:pytest ../images/pytest
# Stop and remove the existing pytest container if it exists
docker-compose rm -f pytest

# Build and start the pytest container
docker-compose up --build -d pytest

# Wait for a moment to allow tests to run
sleep 5

# Display the logs from the pytest container
docker-compose logs pytest

# Remove the pytest container after running tests
docker-compose rm -f pytest
