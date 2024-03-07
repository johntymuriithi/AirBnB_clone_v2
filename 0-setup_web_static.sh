#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary folders
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create fake HTML file
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership
sudo chown -R ubuntu:ubuntu /data/
config_content="
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location / {
        add_header X-Served-By $hostname;
        proxy_pass http://127.0.0.1:5000;
    }

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    $config_content
}"

# Add the configuration to Nginx default site
sudo echo "$config_content" | sudo tee /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart