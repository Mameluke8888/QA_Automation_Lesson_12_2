from json_file_reader import JsonFileReader
from ini_file_reader import IniFileReader

# Exercise #1
#
# Add to JsonFileReader and IniFileReader functions to extract user email and password:#
# Names for functions can be get_email and get_password that will have an additional parameter section_name
# (for example the value of it can be user1)
# Names of the functions should be the same in JsonFileReader and IniFileReader
# Functions should raise an Exception if those options are not in the config files
#
# Exercise #2
# Update ConfigReader with functions that return user email and password
#
# Exercise #3
# Update all tests to use ConfigReader

class ConfigReader:
    def __init__(self, filename):
        self.reader = None

        if filename.endswith(".json"):
            self.reader = JsonFileReader(filename)
        elif filename.endswith(".ini"):
            self.reader = IniFileReader(filename)
        else:
            raise Exception("File format is not supported")

    def get_browser(self):
        return self.reader.get_browser()

    def get_wait_time(self):
        return self.reader.get_wait_time()

    def get_email(self, section_name):
        return self.reader.get_email(section_name)

    def get_password(self, section_name):
        return self.reader.get_password(section_name)