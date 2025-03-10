'''DATE:26/02/2025
1. Given a string containing multiple words, write a function to reverse every alternate 
word in the sentence while keeping the others unchanged.
 Constraints:
• Words are separated by a single space.
• Punctuation should be preserved in its place.
• The first word remains unchanged, the second word is reversed, the third word 
remains unchanged, and so on.
Sample Input and Output:
Hello world this is Python
Hello dlrow this si Python'''
def reverse_words(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if i % 2 != 0:
            words[i] = words[i][::-1]
    return ' '.join(words)


sentence =input()

print(reverse_words(sentence))
