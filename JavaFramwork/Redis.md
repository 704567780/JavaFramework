# docker 安装Redis

```
docker pull redis:5.0.9
mkdir /root/docker/redis
vim /root/docker/redis/redis.conf
    port 6379
    requirepass xxxx
    appendonly yes
docker run -p 6379:6379 --name redis \
        -v /root/docker/redis/data:/data \
        -v /root/docker/redis/redis.conf:/etc/redis/redis.conf \
        -d redis:5.0.9 redis-server /etc/redis/redis.conf
```