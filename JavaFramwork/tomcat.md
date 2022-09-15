# docker部署tomcat

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

# tomcat 部署项目乱码问题

原因:各个模块编码不一致(假设全部都统一为utf-8)

1、前端页面是否为utf-8格式。例如html文件head标签下可以设置utf-8格式

```
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
```

2、进入tomcat内部容器，使用locale查看是否为utf-8格式

