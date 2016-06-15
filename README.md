## 糗事百科爬虫

<pre>

    本人是一个web前端开发工程师，python是凭着学习的态度来玩的哈，写的不好请见谅
    
    有问题请联系 {name : 'Hanson', email : '360468937@qq.com'}
    
</pre>

###主要代码 app.py  看注释
###db.py python mysql一个简单的封装类

###mysql 数据表
<pre>
CREATE TABLE `article` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `content` varchar(15000) DEFAULT NULL,
  `pubdate` timestamp NULL DEFAULT NULL,
  `click` int(11) DEFAULT NULL,
  `like` int(11) DEFAULT NULL,
  `zan` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL COMMENT '0正常，1已删除',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;
</pre>
