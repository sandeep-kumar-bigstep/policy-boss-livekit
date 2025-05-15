#!/bin/bash
# Script to install Docker on Ubuntu

# Check if Docker is already installed
if command -v docker &> /dev/null; then
    echo "Docker is already installed:"
    docker --version
    echo "Docker Compose:"
    docker compose version
    echo "Docker Buildx:"
    docker buildx version
    
    echo "\nDocker is already installed. Do you want to reinstall? (y/N)"
    read -r response
    if [[ "$response" != "y" && "$response" != "Y" ]]; then
        echo "Installation cancelled."
        exit 0
    fi
fi

# Add Docker's official GPG key:
echo "Adding Docker's official GPG key..."
sudo apt-get update
sudo apt-get install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo "Adding Docker repository to Apt sources..."
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# Install Docker Engine, containerd, Docker Compose and Buildx plugins
echo "Installing Docker Engine and related packages..."
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Verify installation
if command -v docker &> /dev/null; then
    echo "\nDocker installed successfully:"
    # Add current user to docker group to avoid permission issues
    echo "Adding user to the docker group..."
    sudo usermod -aG docker $USER
    echo "Log out and log back in for the changes to take effect, or run 'newgrp docker' to apply changes to current session."
    docker --version
    echo "Docker Compose:"
    docker compose version
    echo "Docker Buildx:"
    docker buildx version
    
    # Verify docker service is running
    if systemctl is-active --quiet docker; then
        echo "Docker service is running."
    else
        echo "Docker service is not running. Starting docker service..."
        sudo systemctl start docker
    fi
    
    # Run hello-world to verify installation
    echo "\nRunning test container..."
    sudo docker run hello-world
else
    echo "\nDocker installation failed."
    exit 1
fi
