# 单实例，无持久化，带管理界面的简单Rabbitmq
##特点
一个rc管理一个pod，无法持久化数据。
通过service对外使用
##启动
执行三个编排文件。注意替换instanceid，以及RABBITMQ_DEFAULT_USER 和RABBITMQ_DEFAULT_PASS两个默认的变量。
##绑定
简单可以直接返回管理员的用户名和密码，或者通过MQ的api创建一个。

