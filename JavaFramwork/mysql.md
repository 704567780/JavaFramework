# docker 安装 mysql

```
docker pull mysql:8.0

# 运行容器
docker run -p 3306:3306 --name mysql  \
-v /var/log/mysql \
-v /var/lib/mysql \
-v /etc/mysql/conf.d \
-e MYSQL_ROOT_PASSWORD=root \
-d mysql:8.0
```