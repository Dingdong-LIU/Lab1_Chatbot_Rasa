# Introduction to Rasa

Before we head into structure of Rasa, let's first try to talk with the initial chatbot!

## Try the initial Chatbot
Type the following command to train and try the initial chatbot.
```bash
cd ./chatbot/00-rasa-init
rasa train
rasa shell
```
Say Hi or hello to chatbot and start the conversation. 

PS: You can try to pretend you are unhappy and see what will happen.

## Basic Stucture of Rasa
In general there are two systems inside of Rasa:
### NLU

**Natural Language Understanding**. In the context of Rasa we're usually talking about the part of the system that accepts raw text that goes in and machine-readable information that goes out. That usually means that it's the part that *accepts text* and can turn it into *intents* and *entities*.

We currently take a mixed of *rule-based* and *neural network based* methods. You can check out the `chatbot/00-rasa-init/domain.yml` file. Here are part of the content.

```yml
...
intents:
  - greet
  - goodbye
  - affirm
  - deny
  - mood_great
  - mood_unhappy
  - bot_challenge

responses:
  utter_greet:
  - text: "Hey! How are you?"

  utter_cheer_up:
  - text: "Here is something to cheer you up:"
    image: "https://i.imgur.com/nGF1K8f.jpg"

  utter_did_that_help:
  - text: "Did that help you?"

  utter_happy:
  - text: "Great, carry on!"

  utter_goodbye:
  - text: "Bye"

  utter_iamabot:
  - text: "I am a bot, powered by Rasa."
...
```
For each input from a user, rasa will try to tell what is your intent, for example, you are greeting the chatbot, you are happy, or you are sad in this scenario.

Then rasa will give you responses accordingly. Those responses can be viewed here. 

But a question is, how should rasa respond according to intents? What is the mapping between intents and responses? That is something related to **Dialogue Policies**.


### Dialogue Policies

When we talk about **Dialogue Policies** we're referring to the part of the system that predicts the next action to take. The next action isn't just determined based on the current intent, we typically need to know about the entire conversation so far.

Policies can again be based on rules or neural methods. Rasa allows you to define your own lightweight rules to define what needs to happen. But to allow for generalization, Rasa also provides a neural network called TED that picks the next best turn based on the conversation so far and all the conversations that it trained on.

In this Tutorial, we focused on a rule-based approach. But you can also use neural network-based approaches in your projects. For more information, you can check out [Rasa Learning Center](https://learning.rasa.com/).

The dialogue policies are mainly defined in `chatbot/00-rasa-init/data/rules.yml`

```yml
...
rules:

- rule: Say goodbye anytime the user says goodbye
  steps:
  - intent: goodbye
  - action: utter_goodbye

- rule: Say 'I am a bot' anytime the user challenges
  steps:
  - intent: bot_challenge
  - action: utter_iamabot
```

<!-- ## Conversation Stucuture

Sample ones are defined in `chatbot/00-rasa-init/data/stories.yml`.

```yml
version: "3.1"

stories:

- story: happy path
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_great
  - action: utter_happy

- story: sad path 1
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_unhappy
  - action: utter_cheer_up
  - action: utter_did_that_help
  - intent: affirm
  - action: utter_happy

- story: sad path 2
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_unhappy
  - action: utter_cheer_up
  - action: utter_did_that_help
  - intent: deny
  - action: utter_goodbye

``` -->

## Summarization

### File Structure
Below is the file structure of an initial Rasa project.
```bash
00-rasa-init/
├── actions
│   ├── actions.py
│   ├── __init__.py
│   └── __pycache__
│       ├── actions.cpython-39.pyc
│       └── __init__.cpython-39.pyc
├── config.yml
├── credentials.yml
├── data
│   ├── nlu.yml
│   ├── rules.yml
│   └── stories.yml
├── domain.yml
├── endpoints.yml
├── models
│   └── 20230301-135057-dyadic-bunker.tar.gz
├── README.md
└── tests
    └── test_stories.yml
```

A quick overview of all the basic files:
* The `domain.yml` file is the file where everything comes together.
* The `config.yml` file contains the configuration for your machine-learning models.
* The `data` folder contains data that your assistant will learn from.
* The `nlu.yml` file contains examples for your intents and entities.
* The `stories.yml` file contains examples of conversations turns.
* The `rules.yml` file contains predefined rules for the dialogue policies.

> We will discuss `actions` in the later part of this Tutorial.

### Useful Commands
There are a few commands that are good to be aware of from the command line.

* `rasa init` allows you to start a new Rasa project.
* `rasa train` allows you to train a new assistant based on your current training data.
* `rasa shell` allows you to chat with a trained assistant.
* `rasa -h` allows you get receive relevant help text for a command.
* `rasa` --debug gives you extra log output when running commands.

## Additional Readings Materials (About role of some files)

1. About `domain.yml` file, check this article: [what's in the domain file](https://learning.rasa.com/conversational-ai-with-rasa/domain-file/#whats-in-the-domain-file).
2. About `data` folder - what is training data and how Rasa will utilize them? Check out this article: [training data rules](https://learning.rasa.com/conversational-ai-with-rasa/training-data-rules/). It includes following content:
    1. How to tell your chatbot what to do next? How to provide examples for your chatbot to learn from? Use [story](https://learning.rasa.com/conversational-ai-with-rasa/training-data-rules/#stories) which is specified in `story.yml`
    2. How to set a rule that your chatbot must follow? Use [rule](https://learning.rasa.com/conversational-ai-with-rasa/training-data-rules/#rules) which is specified in `rules.yml`
    3. How to teach your chatbot infer correct intents from user inputs? Check out [intent](https://learning.rasa.com/conversational-ai-with-rasa/training-data-rules/#intents) which is specified in `nlu.yml`

## Q&A Session

Any questions?
