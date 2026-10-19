numbers = [10, -5, 3,-2,8,-1,6]
positive_numbers =[num for num in numbers if num >= 0]
print(f"positive_numbers = {positive_numbers}.")

sentence = "Comprehensions make Python code cleaner"
word_lengths={word:len(word) for word in sentence.split()}
print(f"Word lengths ={word_lengths}")

dictionary={input("define key"): input("What should its value be?") for i in range(3)}
print(f"Your dictionary = {dictionary}.")
small_dictionary = {a:b for a,b in dictionary.items() if len(a) <= 7}
print(f"Small_dictionary = {small_dictionary}.")
