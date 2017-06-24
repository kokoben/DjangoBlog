from django import template

register = template.Library()

@register.simple_tag
def like_text(count):
	'''returns the number of likes. prints like if there's only one like. else prints likes.'''
	if count == 1:
		return str(count) + " like"
	else:
		return str(count) + " likes"

@register.simple_tag
def comment_text_index(count):
	'''returns number of comments on post page. prints comment if only one comment. else prints comments.'''
	if count == 1:
		return str(count) + " comment"
	else:
		return str(count) + " comments"

@register.simple_tag
def comment_text(count):
	'''returns the number of comments. prints comment if there's only one comment. else prints comments.'''
	if count == 1:
		return str(count) + " Comment"
	else:
		return str(count) + " Comments"

@register.simple_tag
def like_button(user, post):
	'''displays the like button. toggles like button text based on whether user has already liked the post.'''
	# user has already liked the post.
	if user.like_set.filter(post=post):
		like_text = "Unlike"
	# user hasn't liked the post.
	else:
		like_text = "Like"
	return like_text
	
