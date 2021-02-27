
class Participant:

    def __init__(self,_string):
        s=_string.strip().replace('\n','')
        self.Name=s[:-1]
        self.category=s[-1]
    def __str__(self):
        return self.Name + " : " + self.category

    def set_category(self,category):
        self.category=category

    def get_category(self):
        return self.category

    def set_name(self,name):
        self.Name = name

    def get_name(self):
        return self.Name
