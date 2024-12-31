"""
Takes any number of words and reverses it.
"""


def main():
    
    reversed_text = []
    
    for letter in reversed(input_text):
        reversed_text.append(letter)
    
    for letter in reversed_text:
        print(letter, end='')



if __name__ == "__main__":
    
    input_text = input("Enter Text or Sentence to Reverse: ")
    main()