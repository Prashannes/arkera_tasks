
# Only '=' queries
class url_query():
    equals = None
    query = "url"
    
    def __init__(self, equals: str = None):
        self.equals = equals

    def get_query(self):
        if self.equals is not None:
            return "(" + self.query + " = " + self.equals + ")"
        return ""
    
# Comparison queries
class date_query(url_query):
    gt = None   # greater than <
    lt = None   # less than >
    query = "date"

    def __init__(self, equals: str = None, gt: str = None, lt: str = None):
        self.equals = equals
        self.gt = gt
        self.lt = lt

    def get_query(self):
        result = ""
        result += super().get_query()
        if ((self.gt is not None) and (self.lt is not None)):
            if (result != ""):
                result += " and "
            result += ("(" + self.gt + " < " + self.query + " < " + self.lt + ")")
        elif (self.gt is not None):
            if (result != ""):
                result += " and "
            result += ("(" + self.gt + " < " + self.query + ")")
        elif (self.lt is not None):
            if (result != ""):
                result += " and "
            result += ("(" + self.lt + " > " + self.query + ")")
        return result
            
        

# Comparison queries
class rating_query(date_query):
    query = "rating"
    
    def __init__(self, equals: str = None, gt: str = None, lt: str = None):
        super().__init__(equals, gt, lt)

    def get_query(self):
        result = ""
        result += super().get_query()
        return result

# In, not in queries
class id_query(date_query):
    inlist = None
    notinlist = None
    query = "id"
    
    def __init__(self, equals: str = None, gt: str = None, lt: str = None, inlist: str = None, notinlist: str = None):
        super().__init__(equals, gt, lt)
        self.inlist = inlist
        self.notinlist = notinlist

    def get_query(self):
        result= ""
        result += super().get_query()
        if self.inlist is not None:
            if (result != ""):
                result += " and "
            result += ("(" + self.query + " in " + self.inlist + ")")
        if self.inlist is not None:
            if (result != ""):
                result += " and "
            result += ("("+ self.query + " not in " + self.notinlist + ")")
                       
        return result







    
    
