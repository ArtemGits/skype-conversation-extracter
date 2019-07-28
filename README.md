# skype-conversation-extracter
The small script witch extract conversation from json file

# requirements
You need download skype history from official skype website.
This is instruction for this : https://support.skype.com/en/faq/FA34894/how-do-i-export-my-skype-files-and-chat-history

# usage
After downloading, you need to know the id of conversation. You can open the json history and find that id.
Ok now you can extract these messages:  

```
python3 conversation.py messages.json 19:941868a7e57745aeb413d9f22d199c34@thread.skype output.json
```

