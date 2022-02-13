# from flask import render_template,request,redirect,url_for
# from . import main
# from flask_login import login_required,current_user
# from ..models import User,Post,Comment
# from .forms import PostForm,CommentForm
# from ..requests import get_quote

# # views
# @main.route("/")
# def index():
#     pickup=Post.query.filter_by(category='pickup').all()
#     interview=Post.query.filter_by(category='interview').all()
#     product=Post.query.filter_by(category='product').all()
#     promotion=Post.query.filter_by(category='promotion').all()
#     received_posts = Post.query.order_by(Post.created_at.desc()).all()
#     quote=get_quote()
    
    

#     '''View root page function that returns the index page and its data'''
#     return render_template('index.html',posts=received_posts,quote=quote,pickup=pickup,interview=interview,product=product,promotion=promotion)


# @main.route("/post",methods=['GET','POST'])
# @login_required
# def post():
#     post=PostForm()
#     if post.validate_on_submit():
#         title=post.title.data
#         category=post.category.data
#         body=post.content.data
#         new_post=Post(title=title,category=category,content=body)
#         Post.save_post(new_post)
#         return redirect(url_for('.index'))
#     return render_template("post.html",post_form=post)

# @main.route('/profile/<my_name>')
# @login_required
# def profile(my_name):
#     user = User.query.filter_by(username=my_name).first()
#     if user is None:
#         abort(404)
#     return render_template("profile.html", user=user) 
    
# @main.route('/comment/<id>', methods=['GET', 'POST'])
# @login_required
# def comment(id):
#     comment_form = CommentForm()
#     post = Post.query.get(id)
#     fetch_all_comments = Comment.query.filter_by(post_id=id).all()
#     if comment_form.validate_on_submit():
#         comment = comment_form.comment.data
#         p_id = id
#         user_id = current_user._get_current_object().id
#         new_comment = Comment(comment=comment, user_id=user_id, post_id=p_id)
#         new_comment.save_comment()
#         return redirect(url_for('.comment', id=p_id))
#     return render_template('comment.html', comment_form=comment_form, post=post, all_comments=fetch_all_comments)