from django import template

register = template.Library()

@register.simple_tag
def toggle_like(user, post):
	'''toggles like text based on whether user has already liked the post.'''
	# user has already liked the post.
	if user.like_set.filter(post=post):
		like_text = "Unlike"
	# user hasn't liked the post.
	else:
		like_text = "Like"
	
	return like_text
	
