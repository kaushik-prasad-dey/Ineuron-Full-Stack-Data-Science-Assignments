'''
2.  Write a program that takes a string as input, and counts the frequency of each word in the string, there might  be repeated characters in the string. Your task is to find the highest frequency and returns the length of the  highest-frequency word. 
Note - You have to write at least 2 additional test cases in which your program will run successfully and provide  an explanation for the same.  
Example input - string = “write write write all the number from from from 1 to 100” 
Example output - 5 
Explanation - From the given string we can note that the most frequent words are “write” and “from” and  the maximum value of both the values is “write” and its corresponding length is 5 
'''
def highest_frequency_word_length(input_string):
    words = input_string.split()
    word_frequency = {}

    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    max_frequency = max(word_frequency.values())
    highest_frequency_words = [word for word, frequency in word_frequency.items() if frequency == max_frequency]

    highest_frequency_word = max(highest_frequency_words, key=len)
    return len(highest_frequency_word)

if __name__=="__main__":
    # Test case 1
    input_str1 = "write write write all the number from from from 1 to 100"
    output1 = highest_frequency_word_length(input_str1)
    print("Test Case 1: Input -", input_str1)
    print("Output for the first test case:", output1)

    # Test case 2
    input_str2 = "programming is fun and coding is fun too"
    output2 = highest_frequency_word_length(input_str2)
    print("Test Case 2: Input -", input_str2)
    print("Output for the second test case:", output2)

    # Test case 3
    input_str3 = "python python python is powerful and versatile versatile"
    output3 = highest_frequency_word_length(input_str3)
    print("Test Case 3: Input -", input_str3)
    print("Output for the third test case:", output3)
