# docker 安装nacos

```
docker run -d -p 8848:8848 \
-e MODE=standalone \
-e PREFER_HOST_MODE=hostname \
-v /home/nacos/init.d/custom.properties \
-v /home/nacos/logs \
--restart always --name nacos nacos/nacos-server
```

