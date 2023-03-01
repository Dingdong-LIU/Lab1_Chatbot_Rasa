# Custom Actions

## Basic Custom Action

We start the tutorial by showing you how to create a custom action that tells you the time. You will need to install the following packages first:
```bash
pip install arrow dateparser
```
We use these two packages so that we don't need to worry about formatting date and time.

Check out the following code snippet from `./chatbot/01-action/actions/actions.py`

```python
class ActionTellTime(Action):

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
        
        tz_string = city_db.get(current_place, None)
        if not tz_string:
            msg = f"It's I didn't recognize {current_place}. Is it spelled correctly?"
            dispatcher.utter_message(text=msg)
            return []
                
        msg = f"It's {utc.to(city_db[current_place]).format('HH:mm')} in {current_place} now."
        dispatcher.utter_message(text=msg)
        
        return []
```

There are a few parts worth discussing:
* We are defining a class `ActionTellTime` that inherits from the `Action` class found in the `rasa_sdk` module. Whenever you write a custom action, you need to inherit from this class because it handles a lot of boilerplate on your behalf.
    * The `name(self)` function defines the name of this action. This name also needs to be copied to `domain.yml file`. Make sure you *DO NOT* misspell it when using it in your `stories.yml` / `rules.yml` / `domain.yml` files.
    * The run method contains the logic for your custom action. This method receive 
