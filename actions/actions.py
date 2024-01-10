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

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSummarizeSelections(Action):

    def name(self) -> Text:
        return "action_summarize_selections"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        brand = tracker.get_slot('brand')
        style = tracker.get_slot('style')
        fit = tracker.get_slot('fit')
        size = tracker.get_slot('size')

        # Check if the size is likely to be a measurement or a general size
        if size.lower() in ['xs','s', 'm', 'l', 'xl', 'xxl']:
            size_str = f"size {size.upper()}"
        else:
            size_str = f"with a {size} inch collar"

        message = f"Thanks! You have entered {brand}, {style}, {fit} fit {size_str}."
        dispatcher.utter_message(text=message)

        return []
