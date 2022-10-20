# dubbo

## dubbo使用docker安装  

```
docker run -d \
-p 8080:8080 \
-e dubbo.registry.address=zookeeper://ip:2181 \
-e dubbo.admin.root.password=root \
-e dubbo.admin.guest.password=guest \
chenchuxin/dubbo-admin
```

密码root/root guest/guest

## 访问dubbo

http://localhost:8080/

## dubbo入门案例

https://github.com/apache/dubbo-sample



# MYSQL

```
docker run -p 3306:3306 --name mysql \
-v /mydata/mysql/log:/var/log/mysql \
-v /mydata/mysql/data:/var/lib/mysql \
-v /mydata/mysql/conf/my.cnf:/etc/mysql/my.cnf \
-v /mydata/mysql/mydata/:/mydata/ \
-e MYSQL_ROOT_PASSWORD=root  \
--restart=always \
-d mysql:8.0
```

# NACOS

## docker 安装nacos

```
docker run -d -p 8848:8848 \
-e MODE=standalone \
-e PREFER_HOST_MODE=hostname \
-v /home/nacos/init.d/custom.properties \
-v /home/nacos/logs \
--restart always --name nacos nacos/nacos-server


```



# NGINX

## docker 安装nginx

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

# RabbitMQ

## docker 运行RabbitMQ

```
docker run --name rabbitmq -p 5672:5672 -p 15672:15672 -d rabbitmq:3.8-management
```

# REDIS

## docker 安装Redis

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

# zookeeper

## 使用docker进行安装

```
docker pull zookeeper:3.5.8 
docker run --name zookeeper -p 2181:2181 -d zookeeper
```

# EUREKA

```
docker pull springcloud/eureka
```

# tomcat

## docker部署tomcat

```
#先运行容器1
docker run -d -p 8080:8080 --name tomcat tomcat
#复制文件
docker container cp tomcat:/usr/local/tomcat/conf /home/dahuang/Documents/docker/volume/tomcat/conf
docker container cp tomcat:/usr/local/tomcat/bin /home/dahuang/Documents/docker/volume/tomcat/bin
#删除容器1

#重新运行容器
docker run -d -p 8080:8080 --name tomcat \
-e LANG="C.UTF-8" \
-v /home/dahuang/Documents/docker/volume/tomcat/webapps/bookshop:/usr/local/tomcat/webapps/bookshop \
-v /home/dahuang/Documents/docker/volume/tomcat/conf:/usr/local/tomcat/conf \
-v /home/dahuang/Documents/docker/volume/tomcat/bin:/usr/local/tomcat/bin \
-v /home/dahuang/Documents/docker/volume/tomcat/webapps/logs:/usr/local/tomcat/logs tomcat


```

## tomcat 部署项目乱码问题

原因:各个模块编码不一致(假设全部都统一为utf-8)

1、前端页面是否为utf-8格式。例如html文件head标签下可以设置utf-8格式

```
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
```

2、进入tomcat内部容器，使用locale查看是否为utf-8格式

