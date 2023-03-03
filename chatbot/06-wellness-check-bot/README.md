# wellness-check-bot
This is a simple Rasa bot that uses a form to create a daily log of health information.

## Running the assistant
1. Install Rasa Open Source: https://rasa.com/docs/rasa/user-guide/installation/
2. Train the model:

```bash
rasa train
```

3. Open a second terminal window and start the action server:

```bash
rasa run actions
```

4. Return to the first terminal window and start the assistant on the command line:

```bash
rasa shell
```
### Sample Output
![wellness-bot-conversation](https://github.com/karen-white/wellness-check-bot/blob/master/images/bot_conversation.png?raw=true)
