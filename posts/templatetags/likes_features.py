from django import template

register = template.Library()

@register.simple_tag
def like_text(count):
	"returns the number of likes. prints like if there's only one like. else prints likes."
	if count == 1:
		return str(count) + " like"
	else:
		return str(count) + " likes"

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
	
