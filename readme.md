<img src="square-logo.svg" width=255 height=255 align="right">

#  Rasa Programming Tutorial

This repository contains a collection of tutorials that will help you understand the Rasa framework. Basic concepts of Rasa (e.g., Intent, Entity, Response, Action, Slot, Form) will be explained in a series of examples. Several chatbot interfaces are also included in this repository. Note that all the demos here are built and tested with Rasa 3. 


This project is built upon the following resources:

1. Rasa Forms course that's hosted on Rasa's [learning center](https://learning.rasa.com/).


## Installation 

To run all the examples here you'll need to install Rasa, preferably in a virtualenv in the root directory. We strongly recommand you create a virtual environment with <code>Anaconda/Miniconda</code>. If you haven't installed <code>Anaconda/Miniconda</code>, you can refer to their official documentation:

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
Make sure that you installed <code>rasa 3.x.x</code>. For example, above code installed <code>rasa 3.4.4</code> on my own computer. You can verify that by 
```bash
pip show rasa
```
And you will find rasa version information in the outputs. Here are some sample output:
```bash
(rasa_env) ➜ pip show rasa          
Name: rasa
Version: 3.4.4
...
```

Note: It is very important that you installed <code>rasa 3.x.x</code>. This tutorial is not compatible with <code>rasa 2</code>. If you need to use <code>rasa 2</code>, you can refer to previous tutorial notes (See item 1 under [Known Issue](#known-issue)).

## Basic Use of Rasa

### 0. Initial Project
It helps to verify successful installation of `rasa` and help you understand basic structure of Rasa project.

Run the following commandline to initiate a new assistant:
```bash
python -m rasa init --init-dir ./chatbot/00-rasa-init
```
This will start a prompt which will generate a new assistant. You're able to indicate <u>*where you want the new project to be created*</u> and you're also able to train the new assistant after the files have been created.

***Hint: We specified that project should be created under `./chatbot/00-rasa-init` by appending `--init-dir` flag.***

The assistant that you'll create is called "moodbot". It's a simple assistant that tries to cheer you up if you're sad. If you're happy the bot will just say "goodbye" and if you're sad the bot will try to show you a picture of a cute tiger.

You can also refer to the rasa's [learning center website](https://learning.rasa.com/conversational-ai-with-rasa/creating-a-new-assistant/#code) for more detailed explainations. 

### 1. Custom Actions

It helps to understand custom actions and slots before we talk about forms. In this simple bot we show how they work by keeping track of a users name. 

Code can be found in the `01-actions` folder.

### 2. Slots 

It helps to understand custom actions and slots before we talk about forms. In this simple bot we show how they work by keeping track of a users name. 

Code can be found in the `02-slots` folder.

### 3. Simple Forms with Conditional Slots

If we want to query multiple things from the user, it may be best to use forms instead of custom actions. Luckily for us, we can use our `RulePolicy` to help us out and we can configure our slots to ignore entities mentioned outside of our form.

Code can be found in the `03-conditions` folder. 

### 4. From Text

You can fill slots from many types of input, this includes raw text! 

Code can be found in the `04-from-text` folder.

### 5. Form Validation 

What if we want to validate the input of our form? We don't want to have a name that's an empty string after all! 

Code can be found in the `05-validation` folder.


## Known Issue

1. <code>Rasa 2.x</code> is **NOT** compatible with <code>Apple Silicon Mac</code>. If you prefer <code>Rasa 2.x</code>, you can refer to last year's tutorial by Qingyu: [Qingyu's Rasa 2 Tutorial](https://github.com/QingyuGuo/rasa-2.5-tutorial).