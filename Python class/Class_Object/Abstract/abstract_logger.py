from abc import ABC, abstractmethod

# Abstract class
class Logger(ABC): 

    def info(self, message):
        pass

class FileLogger(Logger): # create a FileLogger class with parent abstract Logger class 

    def info(self, message):
        print("File ::", message) 

class DBLogger(Logger): # DBLogger class with parent abstract logger class
    def info(self, message):
        print("DB ::", message)

# Single logger example
class MyApplication: # creating single logger using class name MyApplication

    def register(self, logger): # method register 
        self.logger = logger # declaring the variable logger with self 

    def run(self): # method is function run 
        self.logger.info("Application Running") # provide the message 

    def stop(self): # func stop is the method 
        self.logger.info("Application Stopping")


app1 = MyApplication()  # initialize / construct
app1.register(DBLogger()) # calling the function with class DBLogger
app1.run() # call run func in DBLogger

app2 = MyApplication()  # initialize / construct
app2.register(DBLogger())
app2.register(FileLogger()) # calling the function with class FileLogger
app2.stop() # call stop func


# App with multi loggers
class AppMultiLoggers:

    def __init__(self): # initiating the function 
        self.loggers = [] # create a empty list to append 

    def register(self, logger):
        self.loggers.append(logger)

    def run(self):
        for logger in self.loggers: 
            logger.info("Application Running")

    def stop(self):
        for logger in self.loggers:
            logger.info("Application Stopping")


app = AppMultiLoggers()  # initialize / construct
app.register(DBLogger())
app.register(FileLogger())
app.run()
app.stop()