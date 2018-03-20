from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

#What function is that? It’s the view function we’re going to write next, which will
#actually return the HTML we want. You can see from the import that we’re
#planning to store it in lists/views.py.
from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):

        #resolve is the function Django uses internally to resolve URLs, and find what
        #view function they should map to. We’re checking that resolve, when called
        #with “/”, the root of the site, finds a function called home_page.
        found = resolve('/') 
        self.assertEqual(found.func, home_page) 

    def test_home_page_returns_correct_html(self):
        
        # We create an HttpRequest object, which is what Django will see when a user’s
    	#browser asks for a page.
        request = HttpRequest()

        #We pass it to our home_page view, which gives us a response. You won’t be
        #surprised to hear that this object is an instance of a class called HttpResponse. 
        response = home_page(request) 
        
        #Then, we assert that the .content of the response—which is the HTML that we
        #send to the user—has certain properties.
        #We want it to start with an <html> tag which gets closed at the end. Notice that
        #response.content is raw bytes, not a Python string, so we have to use the b''
        #syntax to compare them. More info is available in Django’s Porting to Python 3
        #docs.
        self.assertTrue(response.content.startswith(b'<html>')) 
        
        #And we want a <title> tag somewhere in the middle, with the word “To-Do”
        #in it—because that’s what we specified in our functional test.
        self.assertIn(b'<title>To-Do lists</title>', response.content) 
        self.assertTrue(response.content.endswith(b'</html>'))