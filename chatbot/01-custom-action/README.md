# Entities, Slots & Custom Actions

* **Entities**: Numbers, dates, country names, product names, etc in a dialogue. They can be detected automatically.
* **Slots**: Long term memery in Rasa.
* **Custom Actions**: Let Rasa do something more than answer questions.

## Setup

We start the tutorial by showing you how to create a custom action that tells you the time. You will need to install the following packages first:
```bash
pip install arrow dateparser geopy timezonefinder
```
We use these two packages so that we don't need to worry about formatting date and time.

To run this project, you need 
```bash
# Change directory to 01-action
cd ./chatbot/01-custom-action
# Train rasa model
rasa train
# Start Action server
rasa run actions --port 5055
```

Then open <u>***a second terminal window***</u>, type
```bash
# Change directory to 01-action
cd ./chatbot/01-action
# Start rasa shell
rasa shell
```
Then you can talk with Rasa in the second terminal window.

PS: Ask Rasa "what time is it?"

## Basic Custom Action

The custom action defined in this project tries to fetch a detected entity for a place. If it cannot find one in the tracker, it tries to fail gracefully (End the conversation but still tell you the UTC time, in this case). This is a pattern that you'll see a lot in custom actions. You should always consider how to best catch unexpected behavior.

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
    * The `name(self)` function defines the name of this action. This name also needs to be copied to the `domain.yml`` file`. Make sure you *DO NOT* misspell it when using it in your `stories.yml` / `rules.yml` / `domain.yml` files.
    * The `run` method contains the logic for your custom action. This method receives information from the conversation so far from the `tracker` input. You can learn more about the information it can provide by checking [the docs](https://rasa.com/docs/action-server/sdk-tracker/).
* To send messages to the end user you'll want to use the `dispatcher.utter_message` method. You can also send images or buttons with this method, but in our example, we only use it to send text messages.
* The original implementation is mocking a database here with our `city_db` dictionary. We're using `geopy` and `timezonefinder` to convert a city name to a timezone.

## Entities

Rasa can be trained to detect the intent of an utterance, but it can also detect entities within an utterance. An entity can be any important detail that your assistant could use later in a conversation. This includes:

* Numbers
* Dates
* Country names
* Product names

For example, when you have an utterance like:

> I would like to book a flight to Sydney

Then we'd like to detect `Sydney` as an entity of type "destination" with a value of "Sydney."

In this example, Rasa will try to get your `place` when you answer its question. To be specific, in the following sample question & utterance:

```text
It's 14:01 utc now. You can also give me a place.
Your input ->  I live in london 
```
We'd like to detect London as an entity of "place".

To do this, we provide examples of entities in your `nlu.yml` file:
1. Use lookup tables to generate case-sensitive regular expression patterns
```yml
# line 95
- lookup: place
  examples: |
    - brussels
    - zagreb
    - london
    - lisbon
    - amsterdam
    - seattle
```
2. Train our own machine-learning model to detect entities. (In this example, we use Rasa's built "DIET" model). We provided the following training data.
```yml
# line 87
- intent: inquire_time
  examples: |
    - what time is it?
    - what time is it in [Amsterdam](place)?
    - what time is it in [London](place)?
    - tell me the time in [Lisbon](place)
    - what is the current time in [Berlin](place)
    - what time is it in [amsterdam](place)[amsterdam](place)
# Also more examples in line103 - line116
```

Here are other ways to detect entities, such as using regular expressions. You can refer to [this guide](https://learning.rasa.com/conversational-ai-with-rasa/entities/) for more methods.


## Slots

We also want Rasa to remember our location. This involves the use of slots. According to the official guide's description:

>In Rasa, slots are your <u>**long term memory**</u> in a conversation. If there's any information you'd like to store for later use, you'd typically want to <u>**store it in a slot**</u>. It's important to understand that a slot is not the same thing as an entity. You could store any information in a slot, even if no entity has been detected. That said, it is very common to fill a slot value with an entity value.

To use a slot, we first define it in the `domain.yml` file. 

```yml
slots:
  location:
    type: text
    influence_conversation: true
    mappings:
      - type: custom
        entity: place
``` 
The slot is set to `influence_conversation` and uses `custom` mappings. `influence_conversation` means that a slot can influence a story. In this case, we have to include stories with `slot_was_set` in the `stories.yml` file. These stories with `slot_was_set` will now be included as training data for the machine learning pipelines in your assistant.


Slot mappings allow you to define how each slot will be filled in. `custom` mappings mean we need to specify how to fill this slot by ourselves. We specified this in the `actions.py` file. We also have other automatic filling options such as `from_entity`. Details can be found [here](https://learning.rasa.com/conversational-ai-with-rasa/slots/#slot-mappings).

## Q&A

Any questions so far?
