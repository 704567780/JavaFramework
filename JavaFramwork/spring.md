# IOC原理

1、生产Bean工厂

org.springframework.context.support.AbstractRefreshableApplicationContext#createBeanFactory

2、解析Bean信息

org.springframework.context.support.AbstractXmlApplicationContext#loadBeanDefinitions(DefaultListableBeanFactory)

3、初始化、拓展工厂

4、反射生产Bean

org.springframework.beans.BeanUtils#instantiateClass(java.lang.reflect.Constructor<T>, java.lang.Object...)

5、填充Bean信息

org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory#populateBean