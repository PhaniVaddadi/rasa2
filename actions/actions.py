# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Dict, List, Text, Union, Optional

from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.forms import FormAction
import re

class ActionGreetUser(Action):

    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello this is your assistant, How can i help you today?")

         return [UserUtteranceReverted()]


class DataForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        return "Data_Form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["name", "email", "phone"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
			"name": [self.from_entity(entity="name"),
			         self.from_intent(intent="say_name", value=True) ],
            "email": [self.from_entity(entity="email"),
			          self.from_intent(intent="say_email", value = True), ],
			"phone": [self.from_entity(entity="phone"),
			         self.from_intent(intent="enter_phone_number", value = True), ]
		}

    def validate_email(self, value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> Dict[Text, Any]:

        value1 = tracker.get_slot("email")

        if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$', str(value1))):
	    # validate slot
            print("Inside if")
            #print(name)
            dispatcher.utter_message(template="utter_phone")
            return {"email": value1}
        else:
            dispatcher.utter_message(template="utter_no_email")
            return {"email": None}

    def validate_phone(self, value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],) -> Dict[Text, Any]:
        value2 = tracker.get_slot('phone')
        if re.search('[6-9]{1}[0-9]{9}', str(value2)):
			# validate slot
            dispatcher.utter_message()
            return {"phone": value2}
        else:
            dispatcher.utter_message(template="utter_no_phone")
            return {"phone": None}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        dispatcher.utter_message(template="utter_goodbye")
        return []
