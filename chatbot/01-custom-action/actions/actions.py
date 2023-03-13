from typing import Any, Text, Dict, List

import arrow
import dateparser
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder


city_db = {
    'brussels': 'Europe/Brussels', 
    'zagreb': 'Europe/Zagreb',
    'london': 'Europe/Dublin',
    'lisbon': 'Europe/Lisbon',
    'amsterdam': 'Europe/Amsterdam',
    'seattle': 'US/Pacific',
    'hongkong': 'Asia/HongKong'
}

class ActionTellTime(Action):

    def __init__(self) -> None:
        super().__init__()
        self.geolocator = Nominatim(user_agent="anyName")
        self.tf = TimezoneFinder()

        # coords = geolocator.gecode("Dallas, Texas")
        # tf = TimezoneFinder()
        # timezone = tf.timezone_at(lng=coords.longitude, lat=coords.latitude)

    def name(self) -> Text:
        return "action_tell_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_place = next(tracker.get_latest_entity_values("place"), None)
        utc = arrow.utcnow()
        
        if not current_place:
            msg = f"It's {utc.format('HH:mm')} utc now. You can also give me a place."
            dispatcher.utter_message(text=msg)
            return []
        
        # Find the timezone
        coords = self.geolocator.geocode(current_place)
        tz_string = self.tf.timezone_at(lng=coords.longitude, lat=coords.latitude)
        # equivalent to
        # tz_string = city_db.get(current_place, None)
        # with a larger database

        if not tz_string:
            msg = f"It's I didn't recognize {current_place}. Is it spelled correctly?"
            dispatcher.utter_message(text=msg)
            return []
                
        msg = f"It's {utc.to(tz_string).format('HH:mm')} in {current_place} now."
        dispatcher.utter_message(text=msg)
        
        return []


class ActionRememberWhere(Action):

    def __init__(self) -> None:
        super().__init__()
        self.geolocator = Nominatim(user_agent="anyName")
        self.tf = TimezoneFinder()

    def name(self) -> Text:
        return "action_remember_where"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_place = next(tracker.get_latest_entity_values("place"), None)
        utc = arrow.utcnow()
        
        if not current_place:
            msg = "I didn't get where you lived. Are you sure it's spelled correctly?"
            dispatcher.utter_message(text=msg)
            return []
        
        # Find the timezone
        # tz_string = city_db.get(current_place, None)
        coords = self.geolocator.geocode(current_place)
        tz_string = self.tf.timezone_at(lng=coords.longitude, lat=coords.latitude)

        if not tz_string:
            msg = f"I didn't recognize {current_place}. Is it spelled correctly?"
            dispatcher.utter_message(text=msg)
            return []
        
        msg = f"Sure thing! I'll remember that you live in {current_place}."
        dispatcher.utter_message(text=msg)
        
        return [SlotSet("location", current_place)]
        # return []


class ActionTimeDifference(Action):

    def __init__(self) -> None:
        super().__init__()
        self.geolocator = Nominatim(user_agent="anyName")
        self.tf = TimezoneFinder()

    def name(self) -> Text:
        return "action_time_difference"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        timezone_to = next(tracker.get_latest_entity_values("place"), None)
        timezone_in = tracker.get_slot("location")
        
        if not timezone_in:
            msg = "To calculuate the time difference I need to know where you live."
            dispatcher.utter_message(text=msg)
            return []
        
        if not timezone_to:
            msg = "I didn't recognize the timezone you'd like to compare against. Are you sure it's spelled correctly?"
            dispatcher.utter_message(text=msg)
            return []
        
        # tz_string = city_db.get(timezone_to, None)
        coords_to = self.geolocator.geocode(timezone_to)
        tz_string_to = self.tf.timezone_at(lng=coords_to.longitude, lat=coords_to.latitude)

        coords_in = self.geolocator.geocode(timezone_in)
        tz_string_in = self.tf.timezone_at(lng=coords_in.longitude, lat=coords_in.latitude)

        if not tz_string_to:
            msg = f"I didn't recognize {timezone_to}. Is it spelled correctly?"
            dispatcher.utter_message(text=msg)
            return []
        
        t1 = arrow.utcnow().to(tz_string_to)
        t2 = arrow.utcnow().to(tz_string_in)
        max_t, min_t = max(t1, t2), min(t1, t2)
        diff_seconds = dateparser.parse(str(max_t)[:19]) - dateparser.parse(str(min_t)[:19])
        diff_hours = int(diff_seconds.seconds/3600)
        
        msg = f"There is a {min(diff_hours, 24-diff_hours)}H time difference."
        dispatcher.utter_message(text=msg)
        
        return []
