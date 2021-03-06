from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

#Tests are organised into classes, which inherit from unittest.TestCase.
class NewVisitorTest(unittest.TestCase):

    #setUp and tearDown are special methods which get run before and after each
    #test. I’m using them to start and stop our browser—note that they’re a bit like a
    #try/except, in that tearDown will run even if there’s an error during the test
    #itself.1 No more Firefox windows left lying around!
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    #The main body of the test is in a method called test_can_start_a_list_and_re
    #trieve_it_later. Any method whose name starts with test_ is a test method,
    #and will be run by the test runner. You can have more than one test_ method
    #per class. Nice descriptive names for our test methods are a good idea too.
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get ('http://localhost:8000')
        
        # She notices the page title and header mention to-do lists
        #We use self.assertIn instead of just assert to make our test assertions.
        #unittest provides lots of helper functions like this to make test assertions, like
        #assertEqual, assertTrue, assertFalse, and so on. You can find more in the
        #unittest documentation.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
           self.assertTrue(
                any(row.text == '1: Buy peacock feathers' for row in rows),
                "New to-do item did not appear in table"
        )
        )

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        #self.fail just fails no matter what, producing the error message given. I’m
        #using it as a reminder to finish the test.
        self.fail('Finish the test')

#Finally, we have the if __name__ == '__main__' clause (if you’ve not seen it
#before, that’s how a Python script checks if it’s been executed from the command
#line, rather than just imported by another script). We call unittest.main(),
#which launches the unittest test runner, which will automatically find test
#classes and methods in the file and run them.
#warnings='ignore' suppresses a superfluous ResourceWarning which was
#being emitted at the time of writing. It may have disappeared by the time you
#read this; feel free to try removing it!
if __name__ == '__main__': #
    unittest.main(warnings='ignore')


#We’re using several of the methods that Selenium provides to examine web pages:
#find_element_by_tag_name, find_element_by_id, and find_elements_by_tag_name
#(notice the extra s, which means it will return several elements rather than just one).
#We also use send_keys, which is Selenium’s way of typing into input elements. You’ll
#also see the Keys class (don’t forget to import it), which lets us send special keys like
#Enter, but also modifiers like Ctrl.

# The page updates again, and now shows both items on her list
# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.
# She visits that URL - her to-do list is still there.
# Satisfied, she goes back to sleep

