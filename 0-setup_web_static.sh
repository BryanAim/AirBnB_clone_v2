#!/usr/bin/env bash
# set up web servers for the deployment of web_static
if [ ! -x /usr/sbin/nginx ];then
    sudo apt-get update -y
    sudo apt-get install nginx -y
fi
# Create directories
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

# Create html file
echo "<html>
<head>
</head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Set-up the content of /data/web_static/current/ to redirect
# to domain.tech/hbnb_static
sudo sed -i '37a\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/hbnb_static;\n\t}' /etc/nginx/sites-enabled/default

# Restart nginx
sudo service nginx restart
