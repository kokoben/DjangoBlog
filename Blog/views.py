from django.views.generic.base import RedirectView

class UserRedirectView(RedirectView):

	def get_redirect_url(self, username):
		return '/posts/%s' % username
