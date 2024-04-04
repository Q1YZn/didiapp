
## 使用
配置一下恋爱记的token，建议使用抓包工具[proxypin](https://github.com/wanghongenpin/network_proxy_flutter)

修改一下钉钉机器人的token，这里可能需要申请自己的组织，然后在群聊里添加机器人。

linux计划任务每天自己定时发送就好了
`0 1 * * *` 每天凌晨12点1分跑一次
具体语法可以[参考文章](https://zhuanlan.zhihu.com/p/115826993) 


例如 

就是十点和0点的0分提醒一次

```plantuml
0 22,0 * * * root python3 /home/didiapp/main.py
```
每天凌晨十二点跑一次
```plantuml
0 0 * * * root python3 /home/didiapp/main.py
```


## 声明
代码写得比较烂，有意见可以提issue，比如自动在任务结束前几分钟提醒？有空会改进。(都是学习的过程)
项目仅供学习交流，严禁用于商业用途，请于24小时内删除。