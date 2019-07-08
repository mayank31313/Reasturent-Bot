from typing import Any, Text, Dict, List

from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher


class ActionOrderFood(FormAction):
    def name(self) -> Text:
         return "action_order_food"

    @staticmethod
    def required_slots(tracker):
        return ['food']

    def run(self, dispatcher,tracker,domain):
        food = tracker.get_slot('food')
        dispatcher.utter_message("here are restaurants you can order %s from:" % str(food))
        return []

class ActionBookSeat(FormAction):
    def name(self) -> Text:
         return "action_book_seat"

    @staticmethod
    def required_slots(tracker):
        return ['food']

    def run(self, dispatcher,tracker,domain):
        food = tracker.get_slot('food')
        dispatcher.utter_message("here are restaurants serving %s near you:" % str(food))
        return []