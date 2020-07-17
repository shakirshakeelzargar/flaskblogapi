from main import application
from flask import render_template,redirect,url_for
from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
import requests
import json
from datetime import datetime
import os
from datetime import datetime
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception as ex:
    print("error in loading env var: ",ex)
DB_USERNAME=os.environ.get("DB_USERNAME")
DB_PASSWORD=os.environ.get("DB_PASSWORD")
DB_DATABASE=os.environ.get("DB_DATABASE")
DB_HOST=os.environ.get("DB_HOST")
print(DB_USERNAME)

# response = json.loads(requests.get("https://raw.githubusercontent.com/shakirshakeelzargar/practice-python/master/assets/fd-reminder.json").text)


# application.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(DB_USERNAME, DB_PASSWORD,DB_HOST,DB_DATABASE)

db=SQLAlchemy(application)

class BlogPost(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title= db.Column(db.Text(),nullable=False)
    content=db.Column(db.Text(),nullable=False)
    author=db.Column(db.String(100),default='N/A')
    date_post=db.Column(db.DateTime,default=datetime.utcnow())
    
    def __repr__(self):
        return str(id)


# all_posts=[{'Sal':'Mr','Name':'Ashir','Prof':'Director'},{'Sal':'Miss','Name':'Ruby'}]
@application.route('/home')
@application.route('/')
def index():
    return render_template("home.html") #asdasd

@application.route('/Var/<string:name>')
def Func1(name):
    return "Welcome to " + name

@application.route('/Test',methods=['Get'])
def func2():
    return "Lololo"

@application.route('/Posts',methods=['GET','POST'])
def func_post():
    if request.method=='POST':
        new_post = BlogPost(title=request.form['title'],content=request.form['content'],author=request.form['author'])
        db.session.add(new_post)
        db.session.commit()
        return redirect('/Posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_post).all()
        db.session.close()
        return render_template('Posts.html',posts=all_posts)



@application.route('/Posts/api',methods=['GET','POST'])
def func_post_api():
    if request.method=='POST':
        new_post = BlogPost(title=request.form['title'],content=request.form['content'],author=request.form['author'])
        db.session.add(new_post)
        db.session.commit()
        return redirect('/Posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_post).all()
        # return all_posts[0].title
       
        output_posts={}
        output_posts["Company"]="Blueturrets"
        output_posts["posts"]=[]
        for i in range(0,len(all_posts)):
            t={}
            t['title']=all_posts[i].title
            t['author']=all_posts[i].author
            t['content']=all_posts[i].content
            output_posts["posts"].append(t)
        return output_posts





@application.route('/Posts/Delete/<int:id>')
def delete(id):
    post = BlogPost.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/Posts')

@application.route('/Posts/Edit/<int:id>',methods=['GET','POST'])
def edit(id):
    post = BlogPost.query.get(id)
    if request.method =='POST':
        post.title=request.form['title']
        post.content=request.form['content']
        post.author=request.form['author']
        db.session.commit()
        return redirect('/Posts')
    else:
        return render_template('Edit.html',post=post)