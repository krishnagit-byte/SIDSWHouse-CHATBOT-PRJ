from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, ValidationAction, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.types import DomainDict
import re

class ValidateUserInfoForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_user_info_form"

    def validate_user_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_name value."""
        
        if len(slot_value) < 2:
            dispatcher.utter_message(text="Name must be at least 2 characters long. Please provide your full name.")
            return {"user_name": None}
        
        return {"user_name": slot_value}

    def validate_user_city(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_city value."""
        
        if len(slot_value) < 2:
            dispatcher.utter_message(text="Please provide a valid city name.")
            return {"user_city": None}
        
        return {"user_city": slot_value}

    def validate_phone_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate phone_number value."""
        
        # Simple phone validation - adjust regex as needed
        phone_pattern = re.compile(r'^[\d\s\-\(\)\+]{10,15}$')
        
        if not phone_pattern.match(slot_value):
            dispatcher.utter_message(text="Please provide a valid phone number (10-15 digits).")
            return {"phone_number": None}
        
        return {"phone_number": slot_value}

class ActionSaveUserInfo(Action):
    def name(self) -> Text:
        return "action_save_user_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get slot values
        user_name = tracker.get_slot("user_name")
        user_city = tracker.get_slot("user_city")
        phone_number = tracker.get_slot("phone_number")
        
        # Here you would typically save to database
        print(f"Saving user info:")
        print(f"Name: {user_name}")
        print(f"City: {user_city}")
        print(f"Phone: {phone_number}")
        
        # You could save to database here
        # database.save_user_info(user_name, user_city, phone_number)
        
        return []