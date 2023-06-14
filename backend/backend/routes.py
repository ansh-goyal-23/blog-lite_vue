import os
import werkzeug
from datetime import datetime
# from .tasks import send_daily_mails
# from flask_wtf import FileField, FileAllowed
from flask import jsonify, request, url_for
from backend import app, db, bcrypt, cache
from backend.forms import RegistrationForm, LoginForm
from flask_cors import CORS
from backend.models import User, Post
from time import perf_counter_ns
from .data_access import get_all_users
from . import cache


app.app_context().push()
# UPLOAD_FOLDER = 'static/uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
 
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


POSTS = [
    {
        'id' : 1,
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First Blog Post',
        'image': 'default'
    },
    {
        'id' : 2,
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Blog Post',
        'image': 'default'
    },
    {
        'id' : 3,
        'author': 'Sarin Kunnoth',
        'title': 'Blog Post 2',
        'content': 'Second Blog Post',
        'image': 'default'
    },
    {
        'id' : 4,
        'author': 'Sarin Kunnoth',
        'title': 'Blog Post 1',
        'content': 'First Blog Post',
        'image': 'default'
    }
]

USERS = []

start = perf_counter_ns()
USERS = get_all_users()
stop = perf_counter_ns()
print("Time Take", stop - start)

app.config.from_object(__name__)


CORS(app, resources= {r"/*":{'origins':"*"}})

@app.route('/', methods = ['GET'])
def greetings():
    return("Hello World")

@app.route('/shark', methods = ['GET'])
def shark():
    return("This is a Good Shark!!")








@app.route('/users', methods = ['GET', 'POST'])
def users():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        hashed_pwd = bcrypt.generate_password_hash(post_data.get('password')).decode('utf-8')

        USERS.append({
            'username': post_data.get('username'),
            'email': post_data.get('email'),
            'password': hashed_pwd,})
        user_details = [post_data.get('username'), post_data.get('email'), hashed_pwd]
        try:
            user_1 = User(username= user_details[0],email= user_details[1],password= user_details[2])
            db.session.add(user_1)
            db.session.commit()
            response_object['status'] = 'User Added!'
            response_object['users'] = USERS[-1]
            with app.app_context():
                cache.clear()
        except:
            response_object['status'] = 'Failed Check Backend!'
        return jsonify(response_object)
    # elif request.method == 'GET':
    #     user_1 = User.query.all()
    #     return jsonify(user_1)
    else :
            # print("Error")
            response_object['status'] = 'Error'
            return jsonify(response_object)




@app.route('/user/<int:user_id>', methods = ['GET'])
def user(user_id):
    if request.method == 'GET':
        response_object = {'status': 'success'}
        user_id = user_id
        
        try:
            user_1 = User.query.filter_by(id = user_id).first()
            print(user_1)
            if user_1 == None:
                # print('Hello')
                response_object['status'] = 'Error!'
                return jsonify(response_object)
                
            else:
                user_details = {'username': user_1.username,'email': user_1.email, 'user_id': user_1.id},
                # print(user_details)
                return user_details[0]
        except:
            response_object['status'] = 'backend Problem'
            return jsonify(response_object)









@app.route('/handle_get', methods=['GET'])
def handle_get():     
    if request.method == 'GET':
        response_object = {'status': 'success'}
        email = request.args['email']
        password = request.args['password']
        
        try:
            # if User.query.filter_by(email= email).first()
            user_1 = User.query.filter_by(email= email).first()
            s = bcrypt.check_password_hash(user_1.password, password)
            # print(user_1)
            if user_1 == None or not s:
                # print('Hello')
                response_object['status'] = 'invalid credentials!'
                return jsonify(response_object)
                
            else:
                user_details = {'username': user_1.username,'email': user_1.email, 'user_id': user_1.id},
                # print(user_details)
                return user_details[0]
        except:
            response_object['status'] = 'invalid credentials!'
            return jsonify(response_object)
        # for user in USERS:
        #     if user['email'] == email and user['password'] == password:
        #         return [user,]
        # else:
        #     return '<h1>invalid credentials!</h1>'
        





@app.route('/get_posts', methods=['GET'])
def posts():     
    if request.method == 'GET':
        response_object = {'status': 'success'}
        user_id = request.args['user_id']
        print(user_id)
        user = User.query.filter_by(id = user_id).first()
        user_posts = []
        user_post = {
            'id': '',
        'title': '',
        'content': '',
        'user_id' : '',
        'author' : '',
        'post_img': ''
    }
        for post in user.posts:
            # print(post)
            user_post['post_img'] = '../assets/profile_pics/' + post.post_image
            user_post['id'] = post.id
            user_post['title'] = post.title
            user_post['content'] = post.content
            user_post['user_id'] = post.user_id
            user_post['author'] = post.author.username
            
            user_posts.append(user_post.copy())
            # print(user_posts)
        # print(user_posts)
        if len(user_posts) == 0:
            response_object['status'] = 'No Posts Found'
            return jsonify(response_object)
        else:
            return user_posts
        




@app.route('/upload_post', methods = ['POST'])
def upload_post():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        if post_data.get('title') == '':
            response_object['status'] = 'Title Empty'
            return jsonify(response_object)
        post_1 = Post(title = post_data.get('title'), content =  post_data.get('content'), user_id = post_data.get('user_id'))
        # print(post_data.get('file').values())
        db.session.add(post_1)
        db.session.commit()
    #     POSTS.append({
    #     'id': len(POSTS)+1,
    #     'author': post_data.get('author'),
    #     'title': post_data.get('title'),
    #     'content': post_data.get('content'),
    #     'image': 'default'
    # })
        response_object['status'] = 'Post Added!'
        return jsonify(response_object)
    
    else :
            response_object['status'] = 'Error!'
            return jsonify(response_object)




@app.route('/counts/<int:user_id>', methods = ['GET'])
def counts(user_id):
    user = User.query.filter_by(id=user_id).first()
    counts={
        'posts_count': len(user.posts),
        'followings_count': len(user.followings)-1,
        'followers_count': len(user.followers)-1
    }
    return counts

@app.route('/feed/<int:user_id>', methods = ['GET'])
def view_posts(user_id):
    response_object = {'status': 'success'}
    all_posts = []
    all_post = {
            'id': '',
        'title': '',
        'content': '',
        'user_id' : '',
        'author' : ''
    }
    
    owner=User.query.filter_by(id=user_id).first()
    posts = []
    # owner_posts  = owner.posts
    # for owner_post in owner_posts:

    #     all_post['id'] = owner_post.id
    #     all_post['title'] = owner_post.title
    #     all_post['content'] = owner_post.content
    #     all_post['user_id'] = owner_post.user_id
    #     all_post['author'] = owner_post.author.username
    #     all_post['date'] = owner_post.date_posted

    #     all_posts.append(all_post.copy())
    followings = owner.followings
    print(followings)
    posts = Post.query.order_by('date_posted')
    # print(posts)

    for post in posts:
        if str(post.user_id) in followings or post.user_id == user_id:

            all_post['id'] = post.id
            all_post['title'] = post.title
            all_post['content'] = post.content
            all_post['user_id'] = post.user_id
            all_post['author'] = post.author.username
            all_post['date'] = post.date_posted
        
            all_posts.append(all_post.copy())

    if len(all_posts) == 0:
            response_object['status'] = 'No Posts Found'
            return jsonify(response_object)
    else:
        # print(all_posts[::-1])
        all_posts = all_posts[::-1]
        return all_posts







           
@app.route('/posts/<int:post_id>', methods = ['GET', 'POST', 'DELETE'])
def post(post_id):
    response_object = {'status': 'success'}

    if request.method == 'GET':
        post = Post.query.filter_by(id=post_id).first() 
        user_post = {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'user_id' : post.user_id,
        'author' : post.author.username
        }
        # print(user_post)
        return(jsonify(user_post))
    elif request.method == 'POST':
        # For LOOP MUCH NEEDED
        post_data = request.get_json()
        post_1 = Post.query.filter_by(id = post_data.get('id')).first()
        post_1.title = post_data.get('title')
        post_1.content = post_data.get('content')
        db.session.add(post_1)
        db.session.commit()
        response_object['status'] = 'Post Updated!'
        # response_object['post'] = POSTS[post_id-1]
        return(response_object)
    elif request.method == 'DELETE':
        Post.query.filter_by(id = post_id).delete()
        db.session.commit()
        # POSTS.remove(post_data['data'])
        response_object['status'] = 'Post Removed!'
        response_object['id'] = '0'
        return(response_object)


            

@app.route('/<int:userid>/search/<string:username>', methods=['GET'])
# @cache.cached(timeout=50, key_prefix = 'searching_users')
def search(userid, username):
    start = perf_counter_ns()

    USERS = get_all_users()

    
    stop = perf_counter_ns()
    print("Time Taken", stop - start)

    
    userlist = []
    for user in USERS:
        if userid == user.id:
            continue
        if username in user.username :
            if str(userid) in user.followers:
                userlist.append([user.username, 'UNFOLLOW'])
            else:
                userlist.append([user.username, 'FOLLOW'])
    return userlist


@app.route('/<int:userid>/follow/<string:username>', methods=['GET'])
def follow(userid, username):
    response_object = {'status': 'success'}
    
    user_1 = User.query.filter_by(username=username).first()
    user_2 = User.query.filter_by(id = userid).first()
    print(user_1.followers)
    print(user_2.followings)
    user_1.followers+=str(user_2.id)
    user_2.followings+=str(user_1.id)
    db.session.commit()
    print(user_1.followers)
    print(user_2.followings)
    response_object['status'] = 'UserFollowed!'
    with app.app_context():
        cache.clear()

    return jsonify(response_object)

    

@app.route('/<int:userid>/unfollow/<string:username>', methods=['GET'])
def unfollow(userid, username):
    print("userid", userid)
    user_11 = User.query.filter_by(username=str(username)).first()
    owner = User.query.filter_by(id = userid).first()
    print("user_11", user_11.id)
    owner_following = owner.followings
    user_11_followers = user_11.followers
    for i in range(len(owner_following)):
       
        if int(owner.followings[i]) == user_11.id:
            sas = owner.followings[0:i] + owner.followings[i+1:]
            owner.followings = sas
            print(sas)
            break
    print("Next Loop")
    print("user_11.followers", user_11.followers)
    # print("user_11.followings", user_11.followings)
    for i in range(len(user_11_followers)):
        print("range", i)
        # print("user_11.followings[i]", owner_followers[i], "==", "owner.id", owner.id)
        if int(user_11.followers[i]) == userid:
            # print(1234, i)
            
            sas = user_11.followers[0:i] + user_11.followers[i+1:]
            user_11.followers = sas
            print(sas)
            break
            
    db.session.commit()
    with app.app_context():
        cache.clear()

    return "Success"
    


# @app.route('/upload', methods=['POST'])
# def upload_file():
#     image_file = url_for('assets', filename='profile_pics/' + current_user.image_file)

# picture = FileField('Update Profile Pic', validators = [])

# from jobs import tasks

# @app.route('/hello/<user_name>', methods = ['GET', 'POST'])
# def hello(user_name):
#     job = tasks.just_say_hello.delay(user_name)
#     return str(job), 200
# def dates_diff(d1, d2):
#     x = d1.strftime("%d/%m/%Y")
#     x = x.split('/')
#     y = d2.strftime("%d/%m/%Y")
#     y = y.split('/')
#     a = int(x[0]) + 30*int(x[1]) + 365*int(x[2])
#     b = int(y[0]) + 30*int(y[1]) + 365*int(y[2])
#     return a-b


# def inactive_users():
#     inact_users = []
#     users = User.query.all()
#     for user in users:
#         post = user.posts[-1]
#         recent_post_date = post.date_posted
#         now = datetime.now()
#         diff = dates_diff(now, recent_post_date)
#         if diff >= 1:
#             inact_users.append({"name": user.username, "email": user.email})

#     print(inact_users[0])
#     for user in inact_users:

#         result = send_daily_mails.delay(user)
#         print(result.get(timeout=1, propagate=False))

# inactive_users()

@app.route('/uploadPostsCSV', methods=['POST'])
def uploadPostsCSV():
    # response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)

    return "Success"


@app.route('/export_posts', methods=['GET'])
def export_posts():
    if request.method == 'GET':
        response_object = {'status': 'success'}
        user_id = request.args['user_id']
        print(user_id)
        user = User.query.filter_by(id = user_id).first()
        user_posts = []

        for post in user.posts:
            date_time = post.date_posted.strftime("%d/%m/%Y")
            user_posts.append([post.author.username,post.title,post.content,date_time])

        if len(user_posts) == 0:
            response_object['status'] = 'No Posts Found'
            return jsonify(response_object)
        else:
            return user_posts