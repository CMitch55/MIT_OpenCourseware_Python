# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        '''
        Initializes a NewsStory object.

        globally unique identifier (GUID)   - a string
        title                               - a string
        description                         - a string
        link to more content                - a string
        pubdate                             - a datetime
        '''
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate
        


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS  

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    '''
    Child class of Trigger. Evaluates for the presence of a phrase within a string.
    Phrase: one or more words seperated by a space and without punctuation.
    '''
    def __init__(self, phrase):
        self.phrase = phrase.lower()
    
    def get_phrase(self):
        '''
        Safely returns phrase
        '''
        return self.phrase()

    def is_phrase_in(self, text):
        '''
        Takes in the string to find the phrase in.
        '''
        text = text.lower()
        for char in string.punctuation:
            text = text.replace(char, ' ')
        word_list = text.split()
        sep_phrase = self.phrase.split()
        test = []
        i = 0
        for p_word in sep_phrase:
            for i, t_word in enumerate(word_list):
                if p_word == t_word:
                    test.append(i)
                    
        match = True
        if len(test) < len(sep_phrase):
            return False
        for i in range(len(test) - 1):
            if test[i + 1] - test[i] != 1:
                match = False
        return match     

# Problem 3
class TitleTrigger(PhraseTrigger):
    '''
    Inherits methods from PhraseTrigger and Trigger.
    Returns alert (True) if phrase found in story title.
    '''
    
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    '''
    Inherits methods from Phrase Trigger and Trigger.
    Returns alert (True) if phrase found in story description.
    '''
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    '''
    Abstract Class. Subclass of Trigger. 

    Alerts when a specified time appears in a NewsStory.

    Constructor:
        time = EST as a ​ string in the format of "3 Oct 2016 17:00:10 "
    
    '''
    def __init__(self, time):
        time = datetime.strptime(time, "%d %b %Y %H:%M:%S")
        time = time.replace(tzinfo=pytz.timezone("EST"))
        self.time = time
    

# Problem 6
# TODO: BeforeTrigger and AfterTrigger

class BeforeTrigger(TimeTrigger):
    '''
    Subclass of TimeTrigger.

    Alerts when a NewsStory is released before a specified datetime.    
    '''
    def evaluate(self, story):
        return self.time > story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))

class AfterTrigger(TimeTrigger):
    '''
    Subclass of TimeTrigger.

    Alerts when a NewsStroy is released after a specified datetime.
    '''
    def evaluate(self, story):
        return self.time < story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))





# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
    
    def evaluate(self, NewsStory):
        return not self.trigger.evaluate(NewsStory)
        

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trig1, trig2):
        self.trig1 = trig1
        self.trig2 = trig2

    def evaluate(self, NewsStory):
        return self.trig1.evaluate(NewsStory) and self.trig2.evaluate(NewsStory)


# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trig1, trig2):
        self.trig1 = trig1
        self.trig2 = trig2

    def evaluate(self, NewsStory):
        if self.trig1.evaluate(NewsStory) or self.trig2.evaluate(NewsStory):
            return True
        else:
            return False

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """   
    # TODO: Problem 10
    # OUTLINE
        #Apply trigger list to each element in stories
            #If trigger is true, add that story to a triggered list
        #Return Trigger list
    triggered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                triggered_stories.append(story)
    return triggered_stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    ###OUTLINE###
    #Generate a dictionary of trigger names to trigger objects from lines.
        #Iterate over lines list.
            #Isolate the parameters by seperateing the things between commas.
            #If first element in new list is "ADD", add the following triggers to triggerlist.
            #Else, the first element is trigger name, second element is trigger keyword 
            #(specifies trigger type), remaining elements are trigger arguments.
                #If element[1] is "TRIGGERTYPE"
                    #Add to dictionary trig_dict[element0] = TRIGGERTYPE(element[2] , element[3] for and)
    
    trigger_dict = {}
    trigger_list = []

    for i in range(len(lines)):
        trig = lines[i].split(',')
        if trig[1] == "TITLE":
            trigger_dict[trig[0]] = TitleTrigger(trig[2])
        elif trig[1] == "DESCRIPTION":
            trigger_dict[trig[0]] = DescriptionTrigger(trig[2])
        elif trig[1] == "BEFORE":
            trigger_dict[trig[0]] = BeforeTrigger(trig[2])
        elif trig[1] == "AFTER":
            trigger_dict[trig[0]] = AfterTrigger(trig[2])
        elif trig[1] == "NOT":
            trigger_dict[trig[0]] = NotTrigger(trig[2])
        elif trig[1] == "AND":
            trigger_dict[trig[0]] = AndTrigger(trigger_dict[trig[2]], trigger_dict[trig[3]])
        elif trig[1] == "OR":
            trigger_dict[trig[0]] = OrTrigger(trigger_dict[trig[2]], trigger_dict[trig[3]])
        elif trig[0] == "ADD":
            for x in range(1, len(trig)):
                trigger_list.append(trigger_dict[trig[x]])

    #print(lines)
    #print("This is the actual trigger list:", trigger_list)
    return trigger_list



    #print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        #t1 = TitleTrigger("George")
        #t2 = DescriptionTrigger("mask")
        #t3 = DescriptionTrigger("health")
        #t4 = AndTrigger(t2, t3)
        #triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('/home/nmeece/Repo/MIT_OpenCourseware_Python/MIT_OCW/MIT_OCW_PSets/PS5/triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            #stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

