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

