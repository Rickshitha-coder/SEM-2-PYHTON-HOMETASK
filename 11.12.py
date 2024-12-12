'''1. Create a class that validates the password which contains various methods to validate the 
password.
Get input from the user and validate the password.
Write a program to validate the password based on these rules and provide feedback(Valid 
or invalid).
Password rules:
At least one uppercase letter.
At least one lowercase letter.
At least one digit.
At least one special character.
Minimum length of 8 characters.'''
class Password:
    def validate(text):
        u_count=0
        l_count=0
        d_count=0
        s_count=0
        length=len(text)
        for i in text:
            if i.isupper():
                u_count+=1
            elif i.islower():
                l_count+=1
            elif i.isdigit():
                d_count+=1
            else:
                s_count+=1
        if u_count>=1 and l_count>=1 and d_count>=1 and s_count>=1 and length>=8:
            print("your password is vaild")
        else:
            print("Your password is invaild")
user=input("Enter the Password:")
Password.validate(user)
'''2
Create a class program that takes a paragraph of text as input and splits it into individual
sentences. Additionally, process each sentence to provide useful information, such as word
count or other linguistic analysis."
Requirements:
Design a class called TextProcessor.
Include a method to split the text into sentences (split_into_sentences).
Include a method to further process each sentence (process_sentences), such as counting
words.
Sample :
Input: "Hello! How are you? I am fine. Let's learn NLP."
Output:
Split Sentences:
o "Hello!"
o "How are you?"
o "I am fine."
o "Let's learn NLP."
Processed Sentence Data:
o Sentence: "Hello!", Word Count: 1
o Sentence: "How are you?", Word Count: 3
o Sentence: "I am fine.", Word Count: 3
o Sentence: "Let's learn NLP.", Word Count: 3'''

class Textprocessor:
    def _init_(self):
        self.text=input("Enter your text").strip()
        
    def split_into_sentences(self):
        sentences=[]
        split=""
        for i in range(len(self.text)):
            split+=self.text[i]
            if self.text[i] in ".!,?":
                
                sentences.append(split)
                split=""
            if split.strip():
                sentences.append(split.strip())
        print(sentences)
        for sentence in sentences:
            word_count = len(sentence.split())
            print(f"{sentence} - count: {word_count}")
t=Textprocessor()
t.split_into_sentences()























        



