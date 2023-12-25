# 电类工程导论（B类）第六组大作业

## 运行环境:

测试所用各工具版本：

```
node: v20.10.0
npm: 10.2.3
vue3: @vue/cli 5.0.8
docker: 24.0.5
python >= 3.11
```

## 使用说明: 

1. 安装上述所需工具
2. 在``service/frontend/``目录执行: 
    ```shell
    npm install
    ```
3. 返回项目根目录, 执行:
    ```shell
    sh start_services.sh
    ```
    执行结束后应显示当前docker容器情况, 可以看到有四个本项目相关容器, 如:
    ```shell
    CONTAINER ID   IMAGE                            COMMAND                  CREATED          STATUS          PORTS                                                                                  NAMES
    32769d889dea   dgd-b-6-websitesource_backend    "uvicorn src.main:ap…"   16 minutes ago   Up 16 minutes   0.0.0.0:82->82/tcp, :::82->82/tcp                                                      dgd-b-6-websitesource_backend_1
    0590d332a28b   dgd-b-6-websitesource_frontend   "docker-entrypoint.s…"   2 hours ago      Up 2 hours      0.0.0.0:8080->8080/tcp, :::8080->8080/tcp                                              dgd-b-6-websitesource_frontend_1
    c920368501d5   elasticsearch:7.17.1             "/bin/tini -- /usr/l…"   2 hours ago      Up 2 hours      0.0.0.0:9200->9200/tcp, :::9200->9200/tcp, 0.0.0.0:9300->9300/tcp, :::9300->9300/tcp   dgd-b-6-websitesource_elasticsearch_1
    8cd3905827ad   mysql:8.2.0                      "docker-entrypoint.s…"   2 hours ago      Up 2 hours      0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp                                   dgd-b-6-websitesource_db_1
    ```
4. 仍在项目根目录, 执行:
    ```shell
    sh setup.sh
    ```
    等待下载和数据库迁移完成后, 访问对应端口(``http://localhost:8080``)即可看到效果!

> 在上述3, 4步执行出现错误中止时, 可在项目根目录执行: ``sh clear.sh``, 这将清空数据库, aerich和elasticsearch的数据. 之后再从第三步开始即可.

## 项目简介

上海交通大学2023秋电类工程导论(B类)大作业项目, 以构建一个具有基本功能的学术搜索网站为目标.

已实现的功能:

- 爬取和储存PDF论文及其元数据, 储存并处理后允许搜索
    - 提供多种搜索方法, 自动选用模糊搜索
    - 支持论文PDF在网页预览和下载
- 用户注册, 登录和为库中的论文撰写笔记
    - 笔记支持Markdown格式, 网页支持在线编辑实时渲染
    - 用户登录使用OAuth2加密验证
- 网页:
    - 论文搜索结果可视化, 库中论文数据可视化
    - 


### 项目实现

分别使用四个docker容器挂载前后端, mysql数据库和elasticsearch. 前后端使用FastAPI/Vue3分离开发, 数据库和elasticsearch数据在docker外储存

后端:
使用tortoise-orm和aerich实现数据库对象映射和数据迁移, 导入数据时使用asyncio管理协程

前端:
- 使用axios与后端交互
- 网页元素组件化
- 使用element-ui实现较为美观现代的界面
- 使用echarts, D3进行数据可视化
- 使用pdf-object, v-md-editor分别实现PDF预览和Markdown实时渲染


