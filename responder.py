import random

class Responder:
       def __init__(self,name): 
              self.name = name

       def response(self, input):
              return ''
       def get_name(self):
              return self.name
       
class RespeatResponder(Responder):
       def response(self, input):
              return '{}って何？'.format(input)
       
class RandomResponder(Responder):
      def __init__(self, name):
       super().__init__(name)
       self.responses = ['いい天気ですね','元気ですか','眠い'] 

       def response(self, input):
             return (random.choice(self.responses))