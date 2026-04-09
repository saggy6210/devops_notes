Add following into the /etc/nginx/nginx.conf

```sh

events {
  worker_connections  4096;  ## Default: 1024
}
http
{
upstream tomcat-backend{
	server fm.tomcatserver.local:8080;
	ip_hash;
}
server{
    listen 80;
    listen [::]:80;
    server_name fm.nginxserver.local;
    location / {
            proxy_redirect      off;
            proxy_set_header    X-Real-IP $remote_addr;
            proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header    X-Forwarded-Proto $scheme;
            proxy_set_header    Host $host;
            root   /var/www/Flight-Management;
	          index  index.html index.htm;
	          try_files $uri $uri/ /index.html;
            #proxy_pass          http://fm.tomcatserver.local:8080/; # In case of redirect to Tomcat server
    }
	location /api {

          # rewrite ^/api/(.*) /$1 break;
          proxy_pass http://tomcat-backend;
          proxy_http_version 1.1;

          proxy_set_header Upgrade $http_upgrade;
          proxy_set_header Connection 'upgrade';

          proxy_set_header Host $host;
          proxy_cache_bypass $http_upgrade;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

          proxy_buffering    off;
          proxy_buffer_size  128k;
          proxy_buffers 100  128k;
        }

}
}
include /etc/nginx/site-enabled/*;


```

------------------------------------------------------------------------------------------------------------------
Reverse proxy setup using Nginx:

cat /etc/nginx/sites-available/proxy


server {
        listen 80;
	#root /usr/share/nginx/html;
	#index index.html; 
	location / {
            proxy_pass http://tomcat/targethost-ip/dns:port;
        }
}

cd /etc/nginx/sites-enabled
ls -a /etc/nginx/sites-available/proxy /etc/nginx/sites-enabled/proxy

systemctl status/start/stop nginx
