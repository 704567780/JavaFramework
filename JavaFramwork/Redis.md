# docker 安装Redis

```
docker run -p 6379:6379 --name redis \
-v /home/dahuang/Documents/docker/volume/redis/data:/data \
-d redis:7 redis-server --appendonly yes \
 --requirepass "redis" \
 --restart=always
```

```
auth  pwd
config get requirepass
```
