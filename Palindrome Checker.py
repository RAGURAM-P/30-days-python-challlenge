def is_palindrome(word):

   
    word = word.replace(" ", "").lower()
    return word == word[::-1] 

user_input = input("Enter a word or phrase: ")

if is_palindrome(user_input):
    print(f"✅ '{user_input}' is a palindrome!")
else:
    print(f"❌ '{user_input}' is NOT a palindrome.")
