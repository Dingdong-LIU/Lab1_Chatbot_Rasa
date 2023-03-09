<img src="square-logo.svg" width=255 height=255 align="right">

#  Rasa Programming Tutorial

This repository contains a collection of tutorials that will help you understand the Rasa framework. Basic concepts of Rasa (e.g., Intent, Entity, Response, Action, Slot, Form) will be explained in a series of examples. Several chatbot interfaces are also included in this repository. Note that all the demos here are built and tested with Rasa 3. 


This project is built upon the following resources:

1. Rasa Forms course that's hosted on Rasa's [learning center](https://learning.rasa.com/).
2. A conversational AI with Rasa: [Source Code](httpss://github.com/RasaHQ/conversational-ai-course-3.x)


## Installation 

To run all the examples here you'll need to install Rasa, preferably in a virtualenv in the root directory. We strongly recommend you create a virtual environment with <code>Anaconda/Miniconda</code>. If you haven't installed <code>Anaconda/Miniconda</code>, you can refer to their official documentation:

Link: [Anaconda Installation Guide](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#)




### Create a virtualenv via Conda
```bash
conda create -n rasa_env python=3.9
```
This will create a Conda virtual environment with <code>Python3.9</code>. Then you need to install <code>rasa</code> via <code>pip3</code>.

### Activate virtual environment
```bash
conda activate rasa_env
```
### Install rasa 3
```bash
pip3 install rasa
```
Make sure that you installed <code>rasa 3.x.x</code>. For example, the above code installed <code>rasa 3.4.4</code> on my computer. You can verify that by 
```bash
pip show rasa
```
And you will find rasa version information in the outputs. Here are some sample outputs:
```bash
(rasa_env) ➜ pip show rasa          
Name: rasa
Version: 3.4.4
...
```

Note: It is very important that you installed <code>rasa 3.x.x</code>. This tutorial is **NOT** tested with <code>rasa 2</code> (and probably **incompatible**). If you need to use <code>rasa 2</code>, you can refer to previous tutorial notes (See item 1 under [Known Issue](#known-issue)).

## Basic Use of Rasa

### 0. Initial Project
It helps to verify the successful installation of `rasa` and helps you understand the basic structure of the Rasa project.

Whenever you want to start a new project, you can run the following command line to initiate a new assistant:
```bash
python -m rasa init --init-dir ./chatbot/00-rasa-init
```
This will start a prompt that will generate a new assistant. You're able to indicate <u>*where you want the new project to be created*</u> and you're also able to train the new assistant after the files have been created.

***Hint: We specified that the project should be created under `./chatbot/00-rasa-init` by appending `--init-dir` flag.***

The assistant that you'll create is called "moodbot". It's a simple assistant that tries to cheer you up if you're sad. If you're happy the bot will just say "goodbye" and if you're sad the bot will try to show you a picture of a cute tiger.

You can also refer to rasa's [learning center](https://learning.rasa.com/conversational-ai-with-rasa/creating-a-new-assistant/#code) website](https://learning.rasa.com/conversational-ai-with-rasa/creating-a-new-assistant/#code) for more detailed explanations. 

## Tutorial on Rasa Functions

### 1. Entities, Slots & Custom Actions

It helps to understand custom actions and slots before we talk about forms. In this simple chatbot, we show how they work by identifying and keeping track of where a user lives. 

The code can be found in the `./chatbot/01-custom-actions` folder.

### 2. Form
We created a pizza ordering chatbot that collects information according to a question table. 

The code can be found in the `./chatbot/02-forms-pizza-ordering-chatbot`.

## Additional Examples
You can refer to [Rasa's learning center](https://learning.rasa.com/) for more examples.


## Web Interface

### Chatroom

The project `./UI/chatroom-source` provides a basic interface for interacting with bots in the webpage, which supports text and voice as input. Please refer to https://github.com/scalableminds/chatroom for more details.

* In your Rasa bot setup, make sure to include the Rasa [REST channel](https://rasa.com/docs/rasa/user-guide/connectors/your-own-website/#rest-channels) in your `credentials.yml` file:
```bash
rest:
  # pass
```

* Install the dependencies for web application
```bash
cd UI/chatroom-source
# install dependencies if you have not installed
yarn install
``` 

* Usage - You need to open 3 terminal/shell windows:


*Terminal-1*: For Rasa server. Depending on your setup you might need to add CORS headers, e.g. `--cors "*"`.

```bash
# change to chatbot directory (just an example)
cd chatbot/02-forms-pizza-ordering-chatbot
# Run Rasa server
rasa run --credentials ./credentials.yml  --enable-api --auth-token XYZ123 --model ./models --endpoints ./endpoints.yml --cors "*"
```

*Terminal-2*: Run Rasa action server if you need customized actions

```bash
# change to chatbot directory (just an example)
cd chatbot/02-forms-pizza-ordering-chatbot
# Run Rasa action server
rasa run actions
```

*Terminal 3*: For web application
   
```bash
cd UI/chatroom-source
# run the local host
yarn serve
```
Open `http://localhost:8080` in your browser.

#### Readings
You can find out more tutorials [here](https://rasa.com/docs/rasa/messaging-and-voice-channels/), including how to connect Rasa to:
* Your Own Website
* Facebook Messenger
* Slack
* Telegram
* Twilio
* ...




### Interactive Voice Response

> Comming Soon in Lab 2


## Known Issue

1. If you prefer <code>Rasa 2.x</code>, you can refer to last year's tutorial by Qingyu: [Qingyu's Rasa 2 Tutorial](https://github.com/QingyuGuo/rasa-2.5-tutorial). Qingyu's tutorial is based on Rasa 2.x</code> is **NOT** compatible with <code>Apple Silicon Mac</code>.
