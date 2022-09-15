# 使用docker安装  root/root guest/guest

```
docker run -d \
-p 8080:8080 \
-e dubbo.registry.address=zookeeper://ip:2181 \
-e dubbo.admin.root.password=root \
-e dubbo.admin.guest.password=guest \
chenchuxin/dubbo-admin
```



# 访问dubbo
http://localhost:8080/


# dubbo入门案例

https://github.com/apache/dubbo-sample

