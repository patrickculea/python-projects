
class DailyMessage:
    def __init__(self):
        self.message = ""
    def get_message(self):
        self.message = input("Enter today's message: ")
    def print_message(self):
        print("Message in uppercase:", self.message.upper())
daily_text = DailyMessage()
daily_text.get_message()
daily_text.print_message()
class HelperSession:
    def __init__(self):
        print("Daily Data Helper session created")
    def __del__(self):
        print("Daily Data Helper session ended")
def create_session():
    print("Making helper session...")
    session = HelperSession()
    print("Session is ready...")
    return session 
print("")
print("Calling create_session() function...")
session_obj = create_session()
print("Program is still running...")
class PairFinder:
    def find_pair(self, numbers, target):
        lookup = {}
        for index, number in enumerate(numbers):
            needed_number = target - number
            if needed_number in lookup:
                return (lookup[needed_number], index)
            lookup[number] = index
        return None
length = int(input("How long should the numbers list be?"))
print(f"Please give me {length} numbers for the list called numbers")
numbers = []
for i in range(length):
    print(f"Number {i} is:")
    a = int(input(""))
    numbers.append(a)
target_value = int(input("Enter target sum to search: "))
result = PairFinder().find_pair(numbers, target_value)
if result is not None:
    print("index1=%d, index2=%d" % result)
else:
    print("No matching pair found.")
del session_obj
print("Program End")

        
        

