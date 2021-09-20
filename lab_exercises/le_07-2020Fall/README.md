# SI 506: Lab Exercise 07

## This week's Lab Exercise
This week's lab exercise includes two problems that focus on understanding the basics about the Python dictionary, which includes creating a dictionary, updating it, and making use of its keys and values. 

## Data description and Set up
Streaming information are adopted from an article <https://www.tomsguide.com/us/best-streaming-video-services,review-2625.html>. 

Baby Shark lyrics is obtained from <https://www.lyricfind.com/>.

Variables `streaming_subscription_info`, `baby_shark_lyrics`, `unique_words` and a function  `convert_to_list_of_words()` are pre-defined for this exercise. 


## 1.0 Problem 01 (5 Points)
We can use a dictionary as a collection of certain information. For this problem, we will use a dictionary to store monthly costs for some streaming services. A dictionary `streaming_subscription_info` is already defined in the setup. Below demonstrates how the dictionary is built. Its key represents each streaming service and a value represents monthly plan costs. 
```
Hulu is $5.99/month.
Netflix is $8.99/month.
HBO is $14.99/month.
Amazon Prime Video is $8.99/month.
```
```Python
streaming_subscription_info = {
'Hulu' : '$5.99', 
'Netflix' : '$8.99', 
'HBO' : '$14.99', 
'Amazon Prime Video' : '$8.99'
}
```
1. Add two more streaming information key-value pairs to `streaming_subscription_info` in the `main()`. Both key and value should follow the same format. Hint: dictionaries are mutable.
```
Disney Plus is $6.99/month.
Youtube TV is $40.00/month.
```
2. Run the print statement below and see what it gives you. Simply use the print statement to check the monthly cost for `Netflix` and `Youtube TV`. This can be done by two seperate lines (two print statements). Hint: streaming names are used as keys. 
```Python
print(streaming_subscription_info['Hulu'])
```

## 2.0 Problem 02 (15 points)
Not just for a simple collection, we can also use it to collect word frequencies and analyze them. For this problem, we will use a dictionary to find out the most frequent word in the Baby Shark lyrics.

1. Let's first build an initial dictionary. 
* Create a function `initialize_word_dict()` that takes a list of unique words as a parameter. It returns a dictionary where each key represents each unique word and a value is 0. 
* Use the function to create a variable `word2count` from a list `unique_words` in the `main()`. 
* You can explore the dictionary by either `print(word2count)` or `print(word2count.items())` in the `main()`.

2. Then, let's count the number of occurences for each word in the lyrics.
* Create a function `get_counts()` that takes two parameters: a list of words and a dictionary. It returns the same dictionary after counting the number of occurences and storing it into the dictionary. NOTE: we assume that an input dictionary contains all the words in an input list of words. 
* Use the function to update the dictionary and assign the returned dictionary into the same variable name `word2count` in the `main()`. To convert the lyrics into a list of words, simply use `convert_to_list_of_words()`. 
* You can explore the dictionary again and see what has been changed. 

3. Finally, let's build a function that finds the most frequent word in the dictionary using the dictionary method `dict.items()`. Hint: consider how we use `enumerate()` in a loop.
* Create a function `find_most_frequent_word()` that takes a dictionary as a parameter and returns the most frequent word. NOTE: we assume that there are no ties when finding the most frequent word.  
* Use the function to find the most frequent word in the dictionary `word2count` and assign it to a variable `most_frequent_word` in the `main()`.
