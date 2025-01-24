#!/usr/bin/env bash
# Script to prepare web servers for deployment of web_static

# Install Nginx if it is not already installed
sudo apt-get update -y
sudo apt-get install nginx -y

# Create the required directories if they don't already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file to test the Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link, delete it if it already exists
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content of /data/web_static/current/ to /hbnb_static
sudo sed -i "/server_name _;/a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
sudo service nginx restart

# Exit successfully
exit 0
