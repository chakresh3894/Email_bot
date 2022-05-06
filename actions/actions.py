# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# Importing required modules
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import smtplib
  
# Creating new class to send emails.
class ActionEmail(Action):
  
    def name(self) -> Text:
        
          # Name of the action
        return "action_email"
  
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
  
        # Getting the data stored in the
        # slots and storing them in variables.
        user_name = tracker.get_slot("name")
        email_id = tracker.get_slot("email")
          
          
        # Code to send email
        # Creating connection using smtplib module
        s = smtplib.SMTP('smtp.gmail.com',587)
          
        # Making connection secured
        s.starttls() 
          
        # Authentication
        s.login("chakresh.mehroliya@nectarinfotel.com", "Chakresh@123")
        
        print("loging succesfull")
        print(user_name)
        print(email_id)
          
        # Message to be sent
        message = "Hello {} , This is a demo message".format(user_name)
          
        # Sending the mail
        s.sendmail("chakresh.mehroliya@nectarinfotel.com",email_id, message)
        
        print("email has been send to",email_id)
          
        # Closing the connection
        s.quit()
          
        # Confirmation message
        dispatcher.utter_message(text="Email has been sent.")
        return []