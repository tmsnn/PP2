class string: 
    def __init__(self, str): 
        self.str = str 
    def get_string(self): 
        return self.str 
    def to_uppercase(self): 
        return self.str.upper() 
S1 = string("Hello, my gpa less than 3") 
S2 = string("Oh, it's very sad") 
print(S1.get_string(), S2.get_string(), sep = '\n') 
# print(sep = '\n')
print(S1.to_uppercase(), S2.to_uppercase(), sep = '\n')