from abc import ABC, abstractmethod

# abstract class for all widget definitions
class Widget(ABC):
    
    # Function to return json data for javascript side
    @abstractmethod
    def get(self):
        pass
    
    # Get the string script for the voice agent to read
    @abstractmethod
    def get_script(self):
        pass
