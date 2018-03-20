from django.core.urlresolvers import resolve
from django.test import TestCase

#What function is that? It’s the view function we’re going to write next, which will
#actually return the HTML we want. You can see from the import that we’re
#planning to store it in lists/views.py.
from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):

        #resolve is the function Django uses internally to resolve URLs, and find what
        #view function they should map to. We’re checking that resolve, when called
        #with “/”, the root of the site, finds a function called home_page.
        found = resolve('/') #
        self.assertEqual(found.func, home_page) 