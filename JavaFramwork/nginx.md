# docker 安装nginx

```
mkdir /root/docker/nginx
mkdir /root/docker/nginx/conf
# 由于我们现在没有配置文件，也不知道配置什么。可以先启动一个nginx，讲他的配置文件拷贝出来
# 再作为映射，启动真正的nginx
docker pull nginx:1.17.4
docker run --name some-nginx -d nginx:1.17.4
docker container cp some-nginx:/etc/nginx /root/docker/nginx/conf
# 然后就可以删除这个容器了
docker docker rm -f some-nginx
# 启动nginx
docker run --name nginx -p 80:80 \
        -v /root/docker/nginx/conf:/etc/nginx \
        -v /root/docker/nginx/html:/usr/share/nginx/html \
        -d nginx:1.17.4
```