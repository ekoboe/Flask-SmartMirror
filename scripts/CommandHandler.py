#from .agent.classes.Voice import Voice

from .widgets.NewsWidget import NewsWidget

# Class to manage all voice requests and return command information to socket connection
class CommandHandler:

    # Put command objects here...
    commands = {
        'news': NewsWidget(),
        'close': "none",
    }

    # def __init__(self):
    #     self.voice = Voice()  # Voice module from voice-agent repository

    def __search_for_key(self, text):  # Search for a dictionary key in the phrase
        for key in self.commands:
            if key in text:
                return key
        return None

    def run(self, text):
        key = self.__search_for_key(text)  # Get the relative key from phrase
        if key:
            if (key == "close"):  # if the command is to close something, just clear everything
                return self.__close()
            self.script = self.commands[key].get_script()  # fetch the script if there is one from the class
            return {'open': "news", 'data': self.commands[key].get()}  # Return json to send over socket
        else:
            self.voice.say("Sorry, I don't know that...")

    def speak(self):
        self.voice.say(self.script)

    def __close(self):  # Send close command and end all speaking proccess
        self.script = ""  # Reset the script
        self.voice.say("")  # End what is being talked about
        return {'close': "none", 'data': "none"}



if __name__ == "__main__":
    sample_phrase = "close the tab"
    command_handler = CommandHandler()
    print(command_handler.run(sample_phrase))



