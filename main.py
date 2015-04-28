import os
import webapp2
from google.appengine.api import channel
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        key = self.request.get('room')
        token = channel.create_channel(key)
        template_values = {'token': token,
                           'room': key
                          }
        path = os.path.join(os.path.dirname(__file__), 'client.html')
        self.response.out.write(template.render(path, template_values))

class MessageFromClient(webapp2.RequestHandler):
    def post(self):
        key = self.request.get('room')
        message = self.request.get('msg')
        channel.send_message(key, message)
        return

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/send', MessageFromClient)], debug=True)