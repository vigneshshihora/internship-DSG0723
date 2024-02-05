#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

def replace_with_colon(text):
    pattern = r'[ ,.]'
    modified_text = re.sub(pattern, ':', text)
    return modified_text

sample_text = 
result = replace_with_colon(sample_text)
print(result)


# In[10]:


import re
def replace_with_colon(text):
    pattern= r'[ , .]'
    modified_text=re.sub(pattern,':',text)
    return modified_text
sample_text='python assignment,Regax exercises.'
result=replace_with_colon(sample_text)
print(result)


# In[82]:


import pandas as pd
import re
data = { 'SUMMARY': ['hello, world!', 'XXXXX test', '123four, five:; six...']}  
cleaned_data = {key: [re.sub(r'\W+', ' ', str(val)) for val in values] for key, values in data.items()}
df = pd.DataFrame(cleaned_data)
print(df)


# In[3]:


import re

def find_long_words(text):
    pattern = re.compile(r'\b\w{4,}\b')
    long_words = pattern.findall(text)
    return long_words
    text = "This is a sample text with some long words like apple, banana, and orange."
    result = find_long_words(text)
print("Long words in the text:", result)


# In[4]:


import re

def find_words(text):
    pattern = re.compile(r'\b\w{3,5}\b')
    words = pattern.findall(text)

    return words
text = "This is a sample text with some words of varying lengths such as dog, cat, apple, and orange."
result = find_words(text)
print("Words of three, four, or five characters in the text:", result)


# In[8]:


import re

def remove_parenthesis(strings):
    pattern = re.compile(r'\([^)]*\)')
    result = []
    for string in strings:
        new_string = re.sub(pattern, '', string)
        result.append(new_string)
    
    return result
sample_text = ["example .(com)", "hr@fliprobo .(com)", "github .(com)", "Hello (Data Science World)", "Data (Scientist)"]
print(remove_parenthesis(sample_text))


# 

# 

# In[27]:


import re

def remove_parenthesis_from_text(text):
    pattern = re.compile(r'\s*\([^)]*\)')
    modified_text = re.sub(pattern, '', text)
return modified_text

def main():
    sample_text.txt=:["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
    with open("sample_text.txt", 'r') as file:
        text = file.read()

    modified_text = remove_parenthesis_from_text(text)

    
    modified_text_list = modified_text.split(", ")

    modified_text_list = [s.strip() for s in modified_text_list]

    print("Expected Output:", modified_text_list)

if __name__ == "__main__":
    main()


# In[83]:


import re
sample_text = "ImportanceOfRegularExpressionsInPython"

pattern = r'[A-Z][a-z]*'


result = re.findall(pattern, sample_text)

print("", result)


# In[84]:


import re

def insert_spaces(text):
    modified_text = re.sub(r'(?<=[a-z])([A-Z0-9])', r' \1', text)
    return modified_text

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

result = insert_spaces(sample_text)

print("", result)


# In[18]:


import pandas as pd

url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.cs
df = pd.read_csv(url)

df['first_five_letters'] = df['Country'].str[:6]

print(df.head())


# In[85]:


import re

def match_string(string):
    pattern = r'^[a-zA-Z0-9_]'
    match = re.match(pattern, string)
    if match:
        return True
    else:
        return False

strings_to_test = ["Hello12", "Test_String", "123", "Special@chars", "numeric_123"]
for string in strings_to_test:
    print(f"'{string}' matches pattern:", match_string(string))


# In[87]:


def starts_with_number(string, number):
    number_str = str(number)
    
    if string.startswith(number_str):
        return True
    else:
        return False

string1 = "123ABC"
number1 = 123
print(f" '{string1}' start with {number1}? {starts_with_number(string1, number1)}")

string2 = "456DEF"
number2 = 789
print(f" '{string2}' start with {number2}? {starts_with_number(string2, number2)}")


# In[24]:


def remove_leading_zeros(ip_address):
    components = ip_address.split('.')

    components = [str(int(component)) for component in components]
    cleaned_ip = '.'.join(components)

    return cleaned_ip

ip_address = "192.168.001.001"
cleaned_ip = remove_leading_zeros(ip_address)
print("Original IP address:", ip_address)
print("IP address without leading zeros:", cleaned_ip)


# In[88]:


import re
sample_text = 'On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country.'
pattern = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)\s+\d{4}\b'


matches = re.findall(pattern, sample_text)
print("", matches)


import re

def extract_date_from_text(file_path):

    with open(file_path, 'r') as file:
        text = file.read()
    pattern = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)\s+\d{4}\b'

    matches = re.findall(pattern, text)

    return matches

file_path = "sample_text.txt"


# In[28]:


def search_words(sample_text, searched_words):
    found_words = []
    for word in searched_words:
        if word in sample_text:
            found_words.append(word)
    return found_words

sample_text = 'The quick brown fox jumps over the lazy dog.'

searched_words = ['fox', 'dog', 'horse']

found_words = search_words(sample_text, searched_words)

print("Found words:", found_words)


# In[29]:


def search_word_with_location(sample_text, searched_word):
    index = sample_text.find(searched_word)

    if index != -1:
        return f"'{searched_word}' found at index {index} in the sample text."
    else:
        return f"'{searched_word}' not found in the sample text."

sample_text = 'The quick brown fox jumps over the lazy dog.'

searched_word = 'fox'

result = search_word_with_location(sample_text, searched_word)

print(result)


# In[30]:


def find_substrings(sample_text, pattern):
    indices = []
    start_index = 0
    
    while start_index < len(sample_text):
        index = sample_text.find(pattern, start_index)
        if index == -1:
            break
        indices.append(index)
        start_index = index + len(pattern)
    
    return indices
sample_text = 'Python exercises, PHP exercises, C# exercises'

pattern = 'exercises'

substrings_indices = find_substrings(sample_text, pattern)
print(f"The pattern '{pattern}' occurs at the following indices:")
print(substrings_indices)


# In[31]:


def find_occurrence_and_position(sample_text, pattern):
    occurrences = []
    position = 0

    while True:
        index = sample_text.find(pattern, position)
        
        if index == -1:
            break
        occurrences.append((pattern, index))

        position = index + len(pattern)

    return occurrences

sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
occurrences = find_occurrence_and_position(sample_text, pattern)
if occurrences:
    print(f"The pattern '{pattern}' occurs at the following positions:")
    for occurrence in occurrences:
        print(f"Position: {occurrence[1]}, Occurrence: {occurrence[0]}")
else:
    print(f"The pattern '{pattern}' does not occur in the string.")


# In[33]:


from datetime import datetime

def convert_date_format(date_str):
    date_object = datetime.strptime(date_str, '%Y-%m-%d')
    formatted_date = date_object.strftime('%d-%m-%Y')

    return formatted_date

date_str = '2024-2-2'

formatted_date = convert_date_format(date_str)

print("Original date (yyyy-mm-dd):", date_str)
print("Converted date (dd-mm-yyyy):", formatted_date)


# In[89]:


import re

def find_decimal_numbers(text):
    
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')

   
    decimal_numbers = pattern.findall(text)

    return decimal_numbers


sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
decimal_numbers = find_decimal_numbers(sample_text)


print("", decimal_numbers)


# In[35]:


def separate_numbers_and_positions(input_string):
    numbers_with_positions = []
    for index, char in enumerate(input_string):
        if char.isdigit():
            numbers_with_positions.append((char, index))
    return numbers_with_positions


input_string = "abc123def456ghi789"
numbers_and_positions = separate_numbers_and_positions(input_string)
print("Numbers and their positions:")
for number, position in numbers_and_positions:
    print(f"Number: {number}, Position: {position}")


# In[37]:


def print_numbers_and_positions(input_string):
    numbers_with_positions = []
    for index, char in enumerate(input_string):
        if char.isdigit():
            numbers_with_positions.append((char, index))
    
    print("Numbers and their positions:")
    for number, position in numbers_with_positions:
        print(f"Number: {number}, Position: {position}")

input_string = "abc123def456ghi789"
print_numbers_and_positions(input_string)


# In[92]:


import re

def extract_max_numeric_value(text):
    
    pattern = r'\b\d+\b'

    
    numeric_values = re.findall(pattern, text)

    
    max_value = max(map(int, numeric_values))

    return max_value


sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'


max_numeric_value = extract_max_numeric_value(sample_text)
print("Maximum Numeric Value:", max_numeric_value)


# In[75]:


import re

def insert_spaces(text):
    
    modified_text = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

    return modified_text


sample_text = "RegularExpressionIsAnImportantTopicInPython"


output_text = insert_spaces(sample_text)


print("", output_text)


# In[74]:


import re


sample_text = " This is a Python Regex Example. FLIP Robo company."


pattern = r'\b[A-Z][a-z]+\b'


matches = re.findall(pattern, sample_text)


print("", matches)


# In[73]:


import re

def remove_continuous_duplicates(sentence):
   
    pattern = r'\b(\w+)(?:\s+\1\b)+'

    
    cleaned_sentence = re.sub(pattern, r'\1', sentence)

    return cleaned_sentence


sample_text = "Hello hello world world"
cleaned_sentence = remove_continuous_duplicates(sample_text)

print("", cleaned_sentence)


# In[72]:


import re

def accept_string_ending_with_alphanumeric(string):
    
    pattern = r'^.*[a-zA-Z0-9]$'

    
    match = re.match(pattern, string)

    
    if match:
        return True
    else:
        return False


test_strings = [ "hello123",   "example!",  "12345",   "python3!",  ]


for string in test_strings:
    print(f" '{string}' - Ends with alphanumeric character:", accept_string_ending_with_alphanumeric(string))


# In[71]:


import re

def extract_hashtags(text):
    
    pattern = r'#[a-zA-Z0-9_]+'

    hashtags = re.findall(pattern, text)

    return hashtags


sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""


hashtags = extract_hashtags(sample_text)
print("", hashtags)


# In[70]:


import re

def remove_u_plus_symbols(text):
    
    pattern = r'<U\+\w{4}>'

   
    cleaned_text = re.sub(pattern, '', text)

    return cleaned_text


sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"


cleaned_text = remove_u_plus_symbols(sample_text)

print("", cleaned_text)


# In[76]:


import re

def extract_dates_from_text(file_path):
    
    with open(file_path, 'r') as file:
        text = file.read()

   
    pattern = r'\b\d{2}-\d{2}-\d{4}\b'

   
    dates = re.findall(pattern, text)

    return dates


file_path = 'sample_text.txt'


dates = extract_dates_from_text(file_path)


print("Extracted Dates:", dates)


# In[81]:


import re

def remove_words_between_length_2_and_4(text):
    
    pattern = re.compile(r'\b\w{2,4}\b')

    
    cleaned_text = pattern.sub('', text)

    return cleaned_text


sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."


cleaned_text = remove_words_between_length_2_and_4(sample_text)


print("", cleaned_text)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




