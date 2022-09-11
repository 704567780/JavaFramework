# JavaFramework
使用docker部署中间件

# zookeeper
docker pull zookeeper:3.5.8 
docker run --name zookeeper -p 2181:2181 -d zookeeper

# zookeeper
docker run -d \
-p 8080:8080 \
-e dubbo.registry.address=zookeeper://192.168.131.137:2181 \
-e dubbo.admin.root.password=root \
-e dubbo.admin.guest.password=guest \
chenchuxin/dubbo-admin 
