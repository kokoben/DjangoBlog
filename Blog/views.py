from django.views.generic.base import RedirectView

class UserRedirectView(RedirectView):
	permanent = False
	query_string = True # what does this do?

	def get_redirect_url(self, username):
		return '/posts/%s' % username
