from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import markdown2
import os
import importlib.util
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    avatar = db.Column(db.String(200))  # URL to avatar image
    bio = db.Column(db.Text, nullable=False)
    skills = db.Column(db.Text)  # Store as comma-separated values
    social_links = db.Column(db.Text)  # Store as JSON string

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200))
    project_url = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    post_type = db.Column(db.String(20), default='blog')  # 'blog' or 'note'
    
    category = db.relationship('Category', backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return f'<Post {self.title}>'

def init_db():
    with app.app_context():
        # 删除所有现有表
        db.drop_all()
        # 创建所有表
        db.create_all()
        # 创建默认分类
        if not Category.query.first():
            default_categories = [
                Category(name='技术', description='技术相关的文章和笔记'),
                Category(name='生活', description='生活随笔和感悟'),
                Category(name='项目', description='项目经验和总结')
            ]
            db.session.add_all(default_categories)
            db.session.commit()

def init_sample_data():
    """导入并执行init_data.py中的初始化样本数据函数"""
    try:
        # 检查数据库中是否已有数据
        with app.app_context():
            if Post.query.count() > 0 or Project.query.count() > 0:
                print("数据库中已有数据，跳过初始化样本数据")
                return
            
            # 导入init_data模块
            try:
                import init_data
                print("正在初始化样本数据...")
                init_data.init_sample_data()
                print("样本数据初始化完成！")
            except ImportError:
                print("未找到init_data.py模块，跳过初始化样本数据")
    except Exception as e:
        print(f"初始化样本数据时出错: {e}")

# 初始化数据库
init_db()

@app.route('/')
def index():
    posts = Post.query.filter_by(post_type='blog').order_by(Post.created_at.desc()).all()
    profile = Profile.query.first()
    return render_template('index.html', posts=posts, profile=profile)

@app.route('/about')
def about():
    profile = Profile.query.first()
    return render_template('about.html', profile=profile)

@app.route('/projects')
def projects():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('projects.html', projects=projects)

@app.route('/notes')
def notes():
    category_id = request.args.get('category', type=int)
    categories = Category.query.all()
    
    if category_id:
        notes = Post.query.filter_by(post_type='note', category_id=category_id).order_by(Post.created_at.desc()).all()
    else:
        notes = Post.query.filter_by(post_type='note').order_by(Post.created_at.desc()).all()
    
    return render_template('notes.html', notes=notes, categories=categories, current_category=category_id)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    content = markdown2.markdown(post.content)
    return render_template('post.html', post=post, content=content)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category_id = request.form.get('category_id', type=int)
        post_type = request.form.get('post_type', 'blog')
        
        post = Post(
            title=title,
            content=content,
            category_id=category_id,
            post_type=post_type
        )
        db.session.add(post)
        db.session.commit()
        
        if post_type == 'note':
            return redirect(url_for('notes'))
        return redirect(url_for('index'))
    
    categories = Category.query.all()
    return render_template('create.html', categories=categories)

@app.route('/profile/edit', methods=['GET', 'POST'])
def edit_profile():
    profile = Profile.query.first()
    if request.method == 'POST':
        if not profile:
            profile = Profile()
        
        profile.name = request.form['name']
        profile.bio = request.form['bio']
        profile.skills = request.form['skills']
        profile.avatar = request.form['avatar']
        profile.social_links = request.form['social_links']
        
        db.session.add(profile)
        db.session.commit()
        return redirect(url_for('about'))
    
    return render_template('edit_profile.html', profile=profile)

if __name__ == '__main__':
    # 应用启动时初始化样本数据
    init_sample_data()
    app.run(debug=True, port=8081) 