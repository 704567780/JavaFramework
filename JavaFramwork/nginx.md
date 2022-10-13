# docker 安装nginx

```
docker run -p 80:80 --name nginx \
-v /home/dahuang/Documents/docker/volume/nginx/html:/usr/share/nginx/html \
-v /home/dahuang/Documents/docker/volume/nginx/logs:/var/log/nginx  \
-d nginx:1.22

docker container cp nginx:/etc/nginx /home/dahuang/Documents/docker/volume/nginx/


docker run -p 8000:80 --name nginx \
-v /home/dahuang/Documents/docker/volume/nginx/html:/usr/share/nginx/html \
-v /home/dahuang/Documents/docker/volume/nginx/logs:/var/log/nginx  \
-v /home/dahuang/Documents/docker/volume/nginx/conf:/etc/nginx \
-d nginx:1.22

```