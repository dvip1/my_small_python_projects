#I wanted to make a project about linked list
#One day I was thinking about how fast time is going and made this one
#hope you enjoy! 
class space_time:
    def __init__(self, place_and_time= None):
        self.place_and_time= place_and_time
        self.next= None
class Life:
    def __init__(self):
        self.birth= None
    def insert_place_and_time(self, pat): #pat is short for space and time
        new= space_time(pat)
        connections= self.birth
        while(connections.next):
            connections= connections.next 
        connections.next= new
    def mistakes(self):
        exp=0 #yeah, mistakes increases our experience
        connections= self.birth
        while(connections):
            exp+=1
            connextions= connections.next
        return exp
    def display_pat(self):
        connections= self.birth
        while(connections):
            print(connections.place_and_time)
            connections=connections.next
if __name__=="__main__":
    new_life= Life()
    #A new journey begins here 
    new_life.birth= space_time("Gujarat,Bhilad; 26/01/04,23:45 ")
   # Ihave made countless mistakes after that^^
   # This mistakes made me who I am
    while True:
        new_life.insert_place_and_time(" ") 
        #I've visited many places after my birth
        #and yeah, life kept inserting places with different time thereafter 
        break #Sure, it will break someday
    #But, I'll keep on living till then!

