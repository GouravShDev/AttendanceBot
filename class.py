class ScheduledClass():
    def __init__(self,classLink,time):
        self._classLink = classLink
        self._time = time
    
    def getClassLink(self):
        return self._classLink

    def getClassTime(self):
        return self._time