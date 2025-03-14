from app import db, app, Profile, Post, Category, Project
from datetime import datetime, timedelta
import random

def init_sample_data():
    with app.app_context():
        # 清除现有数据
        Post.query.delete()
        Project.query.delete()
        Profile.query.delete()
        
        # 保留现有分类或创建新分类
        if not Category.query.first():
            categories = [
                Category(name='技术', description='技术相关文章和笔记'),
                Category(name='生活', description='生活随笔和感悟'),
                Category(name='项目', description='项目经验和总结')
            ]
            db.session.add_all(categories)
            db.session.commit()
        else:
            categories = Category.query.all()
        
        # 创建个人资料
        profile = Profile(
            name='默默',
            avatar='../static/images/me.jpg',  # 使用在线头像生成服务
            bio="""我是一名充满热情的全栈开发者，专注于Web应用和交互设计。

过去5年，我致力于打造优秀的用户体验和高性能的后端系统。我相信技术应该为人所用，而不是让人感到困惑。

喜欢探索新技术，研究设计模式，并乐于分享我的发现。在空闲时间，我喜欢阅读、旅行和摄影，这些经历帮助我从不同角度看待问题。

这个博客是我记录技术心得和生活感悟的地方，希望能与更多志同道合的朋友交流。""",
            skills='JavaScript,Python,React,Vue,Flask,Node.js,UI/UX设计,数据库设计'
        )
        db.session.add(profile)
        
        # 创建博客文章
        blog_posts = [
            {
                'title': '如何设计一个有效的RESTful API',
                'content': """# 如何设计一个有效的RESTful API

RESTful API已经成为现代Web应用程序的标准接口。一个设计良好的API可以提高开发效率，改善用户体验，并简化系统维护。本文将分享设计有效RESTful API的核心原则和最佳实践。

## 核心原则

### 1. 资源导向

REST的核心是将系统功能建模为资源。资源应该使用名词而非动词，例如:

```
/users      # 好
/getUsers   # 不好
```

### 2. HTTP方法的正确使用

* GET: 获取资源
* POST: 创建资源
* PUT: 更新资源(全量更新)
* PATCH: 部分更新资源
* DELETE: 删除资源

### 3. 一致性

保持命名和返回格式的一致性对于API的可用性至关重要。

## 最佳实践

1. **版本控制**: 使用URL路径前缀(如`/api/v1/`)进行版本控制
2. **分页**: 对集合资源实现分页功能
3. **筛选与排序**: 使用查询参数允许客户端筛选和排序
4. **HATEOAS**: 考虑包含相关资源的链接

## 错误处理

返回适当的HTTP状态码和描述性错误消息:

```json
{
  "status": 400,
  "message": "Invalid email format",
  "details": "The provided email 'test' is not in a valid format"
}
```

## 结论

一个优秀的API设计可以大大提高开发效率和系统可用性。通过遵循这些原则和最佳实践，你可以创建出易于使用、维护和扩展的API。

记住，API是产品的界面，它应该像优秀的UI一样，直观且易于使用。""",
                'category_id': next(c.id for c in categories if c.name == '技术'),
                'post_type': 'blog',
                'created_at': datetime.now() - timedelta(days=2)
            },
            {
                'title': '数字极简主义：如何在信息爆炸时代保持专注',
                'content': """# 数字极简主义：如何在信息爆炸时代保持专注

在当今信息过载的时代，我们不断被通知、邮件和社交媒体分散注意力。这篇文章探讨了如何通过数字极简主义重获专注和提高生产力。

## 什么是数字极简主义

数字极简主义是有意识地减少数字干扰，专注于真正重要的内容。它并非完全拒绝技术，而是更明智地使用它。

## 实践步骤

### 1. 审计你的数字生活

花一周时间记录你使用各种应用和设备的情况。问自己：
- 这个应用真的给我带来价值吗？
- 我是否只是出于习惯而使用它？

### 2. 整理通知

关闭所有非必要通知。考虑：
- 只保留来自真人的通知
- 设定固定时间查看邮件和消息
- 使用"请勿打扰"模式

### 3. 精简应用和订阅

删除不常用或不提供真正价值的应用。对于订阅内容：
- 取消大部分电子邮件订阅
- 减少关注的社交媒体账号
- 使用RSS阅读器集中获取重要信息

### 4. 建立健康界限

- 设定使用设备的时间段
- 睡前90分钟避免屏幕使用
- 在工作时关闭社交媒体

## 我的个人实践

实行数字极简主义后，我发现自己的专注力显著提高，焦虑感减轻。现在我每天花更多时间阅读实体书籍，与朋友面对面交流，以及从事深度工作。

虽然偶尔我也会感到"错过一些事情"的焦虑，但这种感觉随着时间推移逐渐减弱。获得的清晰思维和额外时间远远超过了偶尔错过某些信息的代价。

## 结语

在数字世界找到平衡并非一蹴而就。这是一个持续的过程，需要定期反思和调整。重要的是找到适合你个人需求和价值观的平衡点。

数字极简主义不是关于剥夺，而是关于选择。它帮助我们重新掌控自己的注意力和时间，让技术成为我们的工具，而不是主人。""",
                'category_id': next(c.id for c in categories if c.name == '生活'),
                'post_type': 'blog',
                'created_at': datetime.now() - timedelta(days=10)
            },
        ]
        
        # 创建笔记
        notes = [
            {
                'title': 'Python虚拟环境设置笔记',
                'content': """# Python虚拟环境设置笔记

虚拟环境是Python开发的必备工具，它可以为不同项目创建隔离的开发环境。

## 为什么使用虚拟环境

- 避免包冲突
- 便于依赖管理
- 项目环境可复制
- 避免污染全局安装

## 常用工具

### venv (Python 3.3+)

创建:
```bash
python -m venv myenv
```

激活:
```bash
# Windows
myenv\\Scripts\\activate

# macOS/Linux
source myenv/bin/activate
```

### virtualenv

安装:
```bash
pip install virtualenv
```

使用方法与venv类似。

### pipenv

结合了pip和virtualenv的功能:

```bash
# 安装
pip install pipenv

# 使用
pipenv install requests
pipenv shell
```

### poetry

更现代的依赖管理:

```bash
# 安装
curl -sSL https://install.python-poetry.org | python3 -

# 使用
poetry new myproject
cd myproject
poetry add pandas
poetry shell
```

## 最佳实践

- 为每个项目创建独立的虚拟环境
- 使用requirements.txt或pyproject.toml管理依赖
- 不要将虚拟环境提交到版本控制
- 记录Python版本要求

## 需要记住的命令

退出虚拟环境:
```bash
deactivate
```

生成依赖列表:
```bash
pip freeze > requirements.txt
```

安装依赖:
```bash
pip install -r requirements.txt
```""",
                'category_id': next(c.id for c in categories if c.name == '技术'),
                'post_type': 'note',
                'created_at': datetime.now() - timedelta(days=3)
            },
            {
                'title': 'Docker常用命令速查',
                'content': """# Docker常用命令速查

Docker是容器化应用的标准工具。以下是一些日常使用的必备命令。

## 基础命令

### 镜像管理
```bash
# 列出本地镜像
docker images

# 拉取镜像
docker pull ubuntu:20.04

# 构建镜像
docker build -t myapp:1.0 .

# 删除镜像
docker rmi image_id
```

### 容器管理
```bash
# 列出运行中的容器
docker ps

# 列出所有容器(包括已停止的)
docker ps -a

# 启动容器
docker run -d -p 8080:80 nginx

# 停止容器
docker stop container_id

# 删除容器
docker rm container_id

# 进入容器Shell
docker exec -it container_id bash
```

## 数据管理

### 卷管理
```bash
# 创建卷
docker volume create mydata

# 使用卷运行容器
docker run -v mydata:/app/data myapp
```

### 绑定挂载
```bash
# 挂载本地目录
docker run -v $(pwd)/data:/app/data myapp
```

## 网络

```bash
# 创建网络
docker network create mynetwork

# 在指定网络中运行容器
docker run --network=mynetwork myapp

# 查看网络
docker network ls
```

## Docker Compose

```bash
# 启动所有服务
docker-compose up -d

# 停止所有服务
docker-compose down

# 构建并启动
docker-compose up --build
```

## 系统维护

```bash
# 查看磁盘使用
docker system df

# 清理未使用的资源
docker system prune -a
```

## 常见用例

### 运行Postgres数据库
```bash
docker run -d \
  --name postgres \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5432:5432 \
  -v postgres-data:/var/lib/postgresql/data \
  postgres:13
```

### 运行Redis缓存
```bash
docker run -d \
  --name redis \
  -p 6379:6379 \
  redis:alpine
```

定期查阅Docker文档以了解新特性和最佳实践。""",
                'category_id': next(c.id for c in categories if c.name == '技术'),
                'post_type': 'note',
                'created_at': datetime.now() - timedelta(days=7)
            },
            {
                'title': '项目回顾：电商网站重构',
                'content': """# 项目回顾：电商网站重构

最近完成了一个电商网站的技术栈重构项目，记录一些经验和教训。

## 项目背景

客户的电商网站使用了老旧的技术栈(jQuery + PHP)，面临性能问题和维护难题。我们的目标是:

1. 提升性能和用户体验
2. 改善代码可维护性
3. 扩展功能以支持移动端
4. 保持SEO排名

## 技术选择

经过评估，我们选择了:

- **前端**: Next.js (React) + TypeScript
- **后端**: Node.js + Express
- **数据库**: 从MySQL迁移到PostgreSQL
- **部署**: Docker + AWS

## 挑战与解决方案

### 1. 数据迁移

**挑战**: 数千万条历史订单和用户数据需要迁移，且不能停机。

**解决方案**:
- 开发了自定义ETL工具
- 实施了双写策略(新系统上线前同时写入新旧数据库)
- 分批次迁移并验证数据一致性

### 2. SEO保持

**挑战**: 网站有良好的SEO排名，不能因重构而丢失。

**解决方案**:
- 使用Next.js的SSR确保搜索引擎可以爬取
- 实现了精确的301重定向映射
- 保留了原有URL结构
- 添加了结构化数据

### 3. 性能优化

实施了多项优化:
- 图片懒加载和自动优化
- 代码分割和按需加载
- Redis缓存热门产品和搜索结果
- CDN分发静态资源

## 成果

项目历时4个月，取得了显著成果:

- 页面加载时间减少了67%
- 移动端转化率提升了23%
- 代码行数减少了40%
- 服务器成本降低了30%

## 经验教训

### 做对的事

- 渐进式迁移而非完全重写
- 早期关注数据迁移策略
- 持续监控性能和用户反馈

### 可改进之处

- 应该更早引入自动化测试
- 低估了旧系统的一些边缘情况
- 团队沟通可以进一步改善

## 结语

这个项目再次证明，技术重构不仅是技术挑战，更是产品和业务挑战。成功的关键在于理解业务需求，以及在技术理想和实用主义之间找到平衡。""",
                'category_id': next(c.id for c in categories if c.name == '项目'),
                'post_type': 'note',
                'created_at': datetime.now() - timedelta(days=15)
            },
            {
                'title': '旅行手记：京都的禅意空间',
                'content': """# 旅行手记：京都的禅意空间

上个月有幸前往日本京都旅行，体验了几座历史悠久的禅宗寺院和庭园。这次经历让我对空间设计和极简主义有了新的理解。

## 龙安寺石庭

龙安寺的石庭被誉为禅宗美学的杰作，由15块石头和白色砂砾组成的极简构图令人震撼。

值得注意的是:

- 无论从哪个角度观看，总有一块石头被遮挡，象征着人类无法完全理解宇宙的真理
- 每天早晨，僧人们会精心耙理砂砾，形成波纹图案
- 空间设计鼓励静坐和冥想

## 设计启示

这些日本传统空间的设计原则可以应用到现代环境中:

1. **留白的力量**: 不是所有空间都需要被填满
2. **自然元素**: 石头、水、植物的简单组合能创造宁静感
3. **框景**: 精心设计的窗户和门框可以将外部景观"框"起来
4. **路径引导**: 通过动线设计引导体验和发现

## 对数字产品设计的启示

这些禅意设计原则也适用于数字产品:

- **减法设计**: 去除非必要元素
- **节奏感**: 创造视觉上的"呼吸空间"
- **一致性**: 使用有限的设计元素，但应用得当
- **关注体验**: 关注用户的精神和情感体验

## 个人感悟

在这个信息过载的时代，禅宗美学提醒我们简单的力量。它不仅是一种美学，更是一种思考方式 - 通过去除非本质的元素来接近真相。

这次旅行启发我在个人和职业生活中寻求更多的简洁与专注。有时候，少即是多。""",
                'category_id': next(c.id for c in categories if c.name == '生活'),
                'post_type': 'note',
                'created_at': datetime.now() - timedelta(days=20)
            },
            {
                'title': 'Git工作流最佳实践',
                'content': """# Git工作流最佳实践

经过多个团队项目的经验，总结了一些Git工作流的最佳实践，记录下来方便日后参考。

## 分支策略

### 主要分支
- **main/master**: 生产环境代码，随时可部署
- **develop**: 开发环境代码，包含已完成但未发布的功能
- **release/vX.X.X**: 准备发布的版本分支
- **hotfix/xxx**: 紧急修复生产环境问题

### 功能开发
- 从develop分支创建feature分支: `feature/user-authentication`
- 完成后通过PR合并回develop
- 使用语义化的分支命名

## 提交规范

使用语义化提交消息:
```
feat: 添加用户认证功能
fix: 修复登录页面在Safari浏览器的显示问题
docs: 更新API文档
style: 格式化代码，不影响功能
refactor: 重构用户服务，不影响现有功能
test: 添加用户服务的单元测试
chore: 更新构建脚本
```

## 代码审查

- 每个PR至少需要一个审查者批准
- 使用PR模板确保提供足够上下文
- 关注代码质量、测试覆盖率和文档

## 版本管理

使用语义化版本:
- **主版本号**: 不兼容的API变更
- **次版本号**: 向后兼容的功能新增
- **修订号**: 向后兼容的问题修复

## 自动化

- 使用CI/CD自动运行测试和部署
- 配置预提交钩子进行代码格式化和lint检查
- 自动化版本号管理和更新日志生成

## 常见问题解决

### 合并冲突
1. 先拉取最新代码: `git pull origin develop`
2. 在本地解决冲突
3. 提交解决方案: `git commit -m "resolve merge conflicts"`

### 回滚错误提交
- 回滚单个提交: `git revert <commit-hash>`
- 回滚到特定版本: `git reset --hard <commit-hash>`

## 团队协作技巧

- 频繁提交小的变更而非大型变更
- 保持分支生命周期短
- 定期从主分支同步更新
- 使用issue跟踪器关联提交

这些实践帮助我们减少了合并冲突，提高了代码质量，使发布过程更加可预测和稳定。""",
                'category_id': next(c.id for c in categories if c.name == '技术'),
                'post_type': 'note',
                'created_at': datetime.now() - timedelta(days=25)
            },
            {
                'title': 'CSS Grid布局实战笔记',
                'content': """# CSS Grid布局实战笔记

CSS Grid是一个强大的布局工具，这篇笔记记录了我在实际项目中使用Grid的一些经验和技巧。

## 基础网格设置

```css
.container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
  gap: 20px;
}
```

## 常用布局模式

### 经典12列响应式布局

```css
.header { grid-column: 1 / -1; }
.sidebar { grid-column: 1 / span 3; }
.main { grid-column: 4 / -1; }
.footer { grid-column: 1 / -1; }

@media (max-width: 768px) {
  .sidebar { grid-column: 1 / -1; }
  .main { grid-column: 1 / -1; }
}
```

### 卡片网格

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}
```

### 不规则布局

```css
.gallery {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(3, 200px);
  gap: 10px;
}

.featured {
  grid-column: 1 / span 2;
  grid-row: 1 / span 2;
}
```

## 实用技巧

### 1. 命名网格区域

```css
.layout {
  display: grid;
  grid-template-areas:
    "header header header"
    "sidebar main main"
    "footer footer footer";
  grid-template-columns: 200px 1fr 1fr;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.footer { grid-area: footer; }
```

### 2. 自动放置算法

```css
.auto-flow {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-flow: dense; /* 填充空白区域 */
}
```

### 3. 对齐控制

```css
.container {
  display: grid;
  /* 水平对齐 */
  justify-items: start | end | center | stretch;
  /* 垂直对齐 */
  align-items: start | end | center | stretch;
  /* 整体水平对齐 */
  justify-content: start | end | center | stretch | space-around | space-between | space-evenly;
  /* 整体垂直对齐 */
  align-content: start | end | center | stretch | space-around | space-between | space-evenly;
}
```

## 与Flexbox比较

| 场景 | 推荐使用 |
|------|----------|
| 一维布局(行或列) | Flexbox |
| 二维布局(行和列) | Grid |
| 内容驱动的布局 | Flexbox |
| 布局驱动的设计 | Grid |

## 浏览器兼容性

现代浏览器对Grid支持良好，但IE11需要使用旧语法。可以使用以下策略:

1. 使用`@supports`检测
2. 为旧浏览器提供Flexbox回退方案
3. 使用Autoprefixer处理前缀

## 实战案例

最近在一个仪表盘项目中，我使用Grid实现了一个可拖拽调整大小的小部件布局:

```css
.dashboard {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  grid-auto-rows: minmax(200px, auto);
  gap: 20px;
}

.widget {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  padding: 20px;
}

.widget--large {
  grid-column: span 2;
  grid-row: span 2;
}
```

Grid布局极大简化了复杂界面的实现，值得深入学习和实践。""",
                'category_id': next(c.id for c in categories if c.name == '技术'),
                'post_type': 'note',
                'created_at': datetime.now() - timedelta(days=12)
            },
            {
                'title': '阅读笔记：《原子习惯》',
                'content': """# 阅读笔记：《原子习惯》

最近读完了詹姆斯·克利尔的《原子习惯》，这本书提供了一个简单而实用的框架来建立好习惯、打破坏习惯。以下是我的主要收获和思考。

## 核心概念

### 1% 改进原则

微小的改变会随着时间累积成巨大的结果。每天改进1%，一年后你将变得37倍更好。

### 习惯的四个阶段

1. **提示(Cue)**: 触发大脑启动行为的信号
2. **渴望(Craving)**: 对改变状态的动机
3. **反应(Response)**: 实际的习惯或行动
4. **奖励(Reward)**: 习惯带来的好处

## 建立好习惯的四法则

### 1. 让它显而易见(提示)

- **环境设计**: 在环境中放置提示物
- **习惯叠加**: 将新习惯与现有习惯绑定
- **实施意图**: "当X发生时，我将做Y"

### 2. 让它有吸引力(渴望)

- **诱惑捆绑**: 将你需要做的事与你想做的事结合
- **加入积极文化**: 与已有你想要习惯的人在一起
- **创造动机仪式**: 在习惯前做些让你期待的事

### 3. 让它简单易行(反应)

- **减少阻力**: 降低好习惯的执行难度
- **准备环境**: 提前为习惯做好准备
- **两分钟法则**: 将习惯简化到只需两分钟
- **一次性决定**: 预先做出决定，避免未来决策疲劳

### 4. 让它令人满足(奖励)

- **即时满足**: 为好习惯添加即时奖励
- **习惯追踪**: 使用习惯记录表可视化进度
- **不要破坏连续**: 避免错过两次

## 个人应用

我已经开始应用这些原则在几个方面:

### 晨间阅读习惯

- **提示**: 将书放在床头
- **渴望**: 与喝咖啡捆绑(先读20分钟，再喝咖啡)
- **反应**: 开始时只要求读5分钟
- **奖励**: 在阅读记录应用中打卡，分享见解

### 编程学习

- **提示**: 每天晚饭后打开学习项目
- **渴望**: 与朋友组成学习小组，互相督促
- **反应**: 使用番茄工作法，先专注25分钟
- **奖励**: 完成后在GitHub上提交代码，看到贡献图变绿

## 关键启示

1. **身份认同**: 专注于成为什么样的人，而非做什么
2. **系统重于目标**: 建立支持成功的系统
3. **环境的力量**: 环境往往比意志力更重要
4. **复合效应**: 习惯的力量来自长期坚持的复合效应

这本书改变了我对习惯形成的理解，让我意识到微小但一致的改变如何带来巨大的长期影响。推荐给任何想改善生活的人阅读。""",
                'category_id': next(c.id for c in categories if c.name == '生活'),
                'post_type': 'note',
                'created_at': datetime.now() - timedelta(days=18)
            },
            {
                'title': 'TypeScript高级类型技巧',
                'content': """# TypeScript高级类型技巧

在使用TypeScript开发大型应用时，掌握高级类型技巧可以显著提高代码质量和开发体验。这篇笔记记录了一些我经常使用的高级类型模式。

## 类型工具

### 条件类型

```typescript
type IsString<T> = T extends string ? true : false;

// 使用示例
type A = IsString<'hello'>; // true
type B = IsString<123>; // false
```

### 映射类型

```typescript
type Readonly<T> = {
  readonly [P in keyof T]: T[P];
};

// 使用示例
interface User {
  id: number;
  name: string;
}

type ReadonlyUser = Readonly<User>;
// 等同于 { readonly id: number; readonly name: string; }
```

### 类型提取

```typescript
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;

// 使用示例
function fetchUser() {
  return { id: 1, name: 'John' };
}

type FetchUserReturn = ReturnType<typeof fetchUser>; 
// { id: number; name: string; }
```

## 实用类型模式

### 可辨识联合类型

```typescript
interface Square {
  kind: 'square';
  size: number;
}

interface Rectangle {
  kind: 'rectangle';
  width: number;
  height: number;
}

interface Circle {
  kind: 'circle';
  radius: number;
}

type Shape = Square | Rectangle | Circle;

function area(shape: Shape): number {
  switch (shape.kind) {
    case 'square':
      return shape.size * shape.size;
    case 'rectangle':
      return shape.width * shape.height;
    case 'circle':
      return Math.PI * shape.radius ** 2;
    default:
      // 穷尽检查
      const _exhaustiveCheck: never = shape;
      return _exhaustiveCheck;
  }
}
```

### 类型安全的事件系统

```typescript
type EventMap = {
  click: { x: number; y: number };
  focus: undefined;
  load: { data: string };
}

class EventEmitter {
  on<K extends keyof EventMap>(event: K, callback: (data: EventMap[K]) => void) {
    // 实现省略
  }
  
  emit<K extends keyof EventMap>(event: K, data: EventMap[K]) {
    // 实现省略
  }
}

// 使用示例
const emitter = new EventEmitter();
emitter.on('click', (data) => {
  console.log(data.x, data.y); // 类型安全
});
emitter.emit('click', { x: 10, y: 20 }); // 正确
// emitter.emit('click', { x: 10 }); // 错误: 缺少属性 'y'
```

### 类型安全的Redux Actions

```typescript
type Action = 
  | { type: 'INCREMENT'; payload: number }
  | { type: 'DECREMENT'; payload: number }
  | { type: 'RESET' };

function reducer(state: number, action: Action): number {
  switch (action.type) {
    case 'INCREMENT':
      return state + action.payload;
    case 'DECREMENT':
      return state - action.payload;
    case 'RESET':
      return 0;
  }
}
```

## 高级工具类型

### 深度部分类型

```typescript
type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};

// 使用示例
interface Config {
  server: {
    host: string;
    port: number;
    options: {
      timeout: number;
      secure: boolean;
    }
  };
  database: {
    url: string;
  }
}

// 可以部分更新嵌套对象
function updateConfig(config: Config, patch: DeepPartial<Config>) {
  // 实现省略
}

updateConfig(config, {
  server: {
    options: {
      timeout: 5000
    }
  }
});
```

### 类型安全的字符串模板

```typescript
type Route = 'users' | 'posts' | 'comments';
type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE';

type Endpoint = `/${Route}` | `/${Route}/:id`;
type ApiRoute = `[${HttpMethod}] ${Endpoint}`;

// 使用示例
const api: Record<ApiRoute, Function> = {
  '[GET] /users': () => {},
  '[GET] /users/:id': () => {},
  '[POST] /users': () => {},
  // ...其他路由
};
```

## 性能考虑

TypeScript的类型系统非常强大，但复杂类型可能导致编译性能问题。一些建议:

1. 避免过度使用条件类型的递归
2. 考虑使用接口而非复杂的类型别名
3. 适当使用泛型约束减少计算量
4. 对大型联合类型使用字符串字面量

## 结语

TypeScript的类型系统几乎是一门图灵完备的语言，掌握这些高级类型技巧可以帮助我们构建更加健壮和可维护的代码库。随着项目规模增长，这些技术的价值会越发明显。""",
                'category_id': next(c.id for c in categories if c.name == '技术'),
                'post_type': 'note',
                'created_at': datetime.now() - timedelta(days=9)
            },
            {
                'title': '项目管理：敏捷开发实践总结',
                'content': """# 项目管理：敏捷开发实践总结

在过去两年带领团队实践敏捷开发方法，积累了一些经验和教训，记录下来以便日后参考。

## 敏捷基础

### Scrum框架

我们主要采用Scrum框架，包括以下关键实践:

- **Sprint**: 2周一个迭代周期
- **每日站会**: 15分钟，三个问题(昨天做了什么，今天计划做什么，有什么阻碍)
- **Sprint计划会**: 确定Sprint目标和工作项
- **Sprint评审**: 展示完成的功能
- **Sprint回顾**: 讨论改进点

### 看板管理

使用Jira实现看板，包含以下列:

- Backlog
- To Do (当前Sprint)
- In Progress
- Code Review
- QA Testing
- Done

## 实践经验

### 用户故事编写

好的用户故事应该遵循INVEST原则:

- **I**ndependent: 相互独立
- **N**egotiable: 可协商
- **V**aluable: 有价值
- **E**stimable: 可估算
- **S**mall: 足够小
- **T**estable: 可测试

示例格式:
```
作为<角色>，我希望<功能>，以便<获得的价值>
```

### 估点技巧

我们使用斐波那契数列(1, 2, 3, 5, 8, 13)进行估点，并遵循以下原则:

1. 关注相对复杂度而非时间
2. 团队共识优于个人判断
3. 8点以上的故事应拆分
4. 考虑技术债务和测试工作

### 团队速度管理

- 记录每个Sprint的完成点数
- 使用过去3-5个Sprint的平均值预测能力
- 不将速度作为绩效指标
- 关注速度趋势而非绝对值

## 常见挑战与解决方案

### 1. 需求变更频繁

**解决方案**:
- 实施变更缓冲区
- 引入产品发现阶段
- 教育利益相关者理解变更成本
- 保持一定比例的技术改进工作

### 2. 估算不准确

**解决方案**:
- 改进用户故事拆分
- 使用相对估算而非绝对时间
- 定期回顾估算准确度
- 接受一定程度的不确定性

### 3. 技术债务积累

**解决方案**:
- 分配20%时间专注于技术改进
- 可视化技术债务
- 将重构工作融入功能开发
- 建立质量门禁

### 4. 跨团队协作困难

**解决方案**:
- 建立Scrum of Scrums
- 明确依赖关系并提前规划
- 使用API契约进行团队间协作
- 考虑采用Spotify的部落模型

## 工具与流程

### 我们的工具链

- **Jira**: 敏捷项目管理
- **Confluence**: 文档和知识库
- **Bitbucket**: 代码仓库
- **Jenkins**: CI/CD
- **Slack**: 团队沟通

### 持续集成/持续部署

- 每个PR自动运行测试
- 合并到主分支后自动部署到测试环境
- 使用特性标志控制功能发布
- 自动化回滚机制

## 远程团队管理

COVID-19后，我们转为远程工作模式，调整了以下实践:

- 异步沟通优先
- 文档驱动开发
- 虚拟站会和回顾会
- 更注重结果而非工作时间
- 定期虚拟团建活动

## 结语

敏捷不是目标，而是持续改进的旅程。最重要的是培养团队的自组织能力和对价值交付的关注，而不是机械地遵循某种方法论。

每个团队都应该找到适合自己的敏捷实践方式，并不断调整和改进。""",
                'category_id': next(c.id for c in categories if c.name == '项目'),
                'post_type': 'note',
                'created_at': datetime.now() - timedelta(days=14)
            }
        ]
        
        # 创建项目
        projects = [
            {
                'title': 'DeepSeek Chat',
                'description': '我的一个自己搭建的DeepSeek Chat的网站，基于DeepSeek开源模型，提供智能对话服务,支持对话记录浏览器缓存。',
                'image_url': 'https://api.microlink.io?url=https://wus.homes&screenshot=true&meta=false&embed=screenshot.url',
                'project_url': 'https://wus.homes',
                'created_at': datetime.now() - timedelta(days=30)
            },
            {
                'title': '热搜摸鱼排行',
                'description': '无聊时打发时间的热搜排行网站,对个平台实时热榜。',
                'image_url': '../static/images/hot.png',
                'project_url': 'https://hot.wus.homes',
                'created_at': datetime.now() - timedelta(days=60)
            },
            {
                'title': '小红书去水印',
                'description': '一个可以去除小红书图片水印的网站。',
                'image_url': 'https://api.microlink.io?url=https://xhs.wus.homes&screenshot=true&meta=false&embed=screenshot.url',
                'project_url': 'https://xhs.wus.homes',
                'created_at': datetime.now() - timedelta(days=60)
            }
        ]
        
        # 添加所有数据到数据库
        for post_data in blog_posts:
            post = Post(**post_data)
            db.session.add(post)
        
        for note_data in notes:
            note = Post(**note_data)
            db.session.add(note)
        
        for project_data in projects:
            project = Project(**project_data)
            db.session.add(project)
        
        db.session.commit()
        
        print("示例数据已成功添加到数据库！")

if __name__ == "__main__":
    init_sample_data() 