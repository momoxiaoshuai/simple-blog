# 极简博客

一个使用 Flask 构建的极简风格个人博客系统，采用简笔画风格的设计元素。
![image](https://github.com/user-attachments/assets/941a1e8d-f714-496e-bba6-06c87167504f)


## 特点

- 极简主义设计
- 支持 Markdown 格式写作
- 响应式布局
- 简笔画风格装饰元素
- 无需复杂配置

## 技术栈

- Python 3.8+
- Flask
- SQLite
- HTML5
- CSS3
- 原生 JavaScript

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/momoxiaoshuai/simple-blog.git
cd blog
```

2. 创建虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

## 运行

1. 启动应用：
```bash
python app.py
```

2. 在浏览器中访问：
```
http://localhost:8081
```

## 使用说明

- 访问首页查看所有文章
- 点击"写文章"创建新的博客文章
- 支持 Markdown 格式编写文章内容
- 文章自动按时间倒序排列
- 笔记内容是我随机生成的,具体使用可以自行修改

## 注意事项

- 数据库文件 `blog.db` 会在首次运行时自动创建
- 建议定期备份数据库文件
- 生产环境部署时请修改相应的安全配置 
