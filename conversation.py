import json
import sys


class ConversationExtraxter(object):
    """ConversationExtraxter small script wich takes a three commandline arguments:
        @argv[1] - input json file
        @argv[2] - conversation id string
        @argv[3] - output json file
    """

    def __init__(self, inputfile, convId, outputfile):
        # read file
        with open(inputfile, 'r') as myfile:
            data = myfile.read()

        # parse file
        obj = json.loads(data)

        # show values
        for i in obj['conversations']:
            # '19:941868a7e57745aeb413d9f22d199c34@thread.skype'
            if (i['id'] == convId):
                with open(outputfile, 'w', encoding='utf-8') as f:
                    json.dump(i['MessageList'],
                              f,
                              ensure_ascii=False,
                              indent=4)


if __name__ == '__main__':
    try:
        inputfile = sys.argv[1]
        conversationId = sys.argv[2]
        outputfile = sys.argv[3]
        conversation = ConversationExtraxter(inputfile, conversationId,
                                             outputfile)
        if (len(sys.argv) < 4):
            raise BaseException
    except BaseException:
        print('''
              Something goes wrong.
              Example run:
              python3 conversation.py messages.josn <id> output.json
              ''')
