# START LAB EXERCISE 07 
print('Lab Exercise 07 \n')

# SETUP

# For P1
streaming_subscription_info = {
'Hulu' : '$5.99', 
'Netflix' : '$8.99', 
'HBO' : '$14.99',
'Amazon Prime Video' : '$8.99'
}

# For P2
baby_shark_lyrics = '''
Baby shark, doo, doo, doo, doo, doo, doo
Baby shark, doo, doo, doo, doo, doo, doo
Baby shark, doo, doo, doo, doo, doo, doo
Baby shark
Mommy shark, doo, doo, doo, doo, doo, doo
Mommy shark, doo, doo, doo, doo, doo, doo
Mommy shark, doo, doo, doo, doo, doo, doo
Mommy shark
Daddy shark, doo, doo, doo, doo, doo, doo
Daddy shark, doo, doo, doo, doo, doo, doo
Daddy shark, doo, doo, doo, doo, doo, doo
Daddy shark
Grandma shark, doo, doo, doo, doo, doo, doo
Grandma shark, doo, doo, doo, doo, doo, doo
Grandma shark, doo, doo, doo, doo, doo, doo
Grandma shark
Grandpa shark, doo, doo, doo, doo, doo, doo
Grandpa shark, doo, doo, doo, doo, doo, doo
Grandpa shark, doo, doo, doo, doo, doo, doo
Grandpa shark
Let's go hunt, doo, doo, doo, doo, doo, doo
Let's go hunt, doo, doo, doo, doo, doo, doo
Let's go hunt, doo, doo, doo, doo, doo, doo
Let's go hunt
Run away, doo, doo, doo, doo, doo, doo
Run away, doo, doo, doo, doo, doo, doo
Run away, doo, doo, doo, doo, doo, doo
Run away
Safe at last, doo, doo, doo, doo, doo, doo
Safe at last, doo, doo, doo, doo, doo, doo
Safe at last, doo, doo, doo, doo, doo, doo
Safe at last
It's the end, doo, doo, doo, doo, doo, doo
It's the end, doo, doo, doo, doo, doo, doo
It's the end, doo, doo, doo, doo, doo, doo
It's the end
'''

unique_words = ['at', 'away', 'baby', 'daddy', 
'doo', 'end', 'go', 'grandma', 'grandpa', 
'hunt', "it's", 'last', "let's", 'mommy', 
'run', 'safe', 'shark', 'the']

def convert_to_list_of_words(lyrics):
    """Returns a list of words

    Parameters:
        lyrics (string)

    Returns:
        list: a list of words
    """
    return lyrics.replace(',','').lower().strip().split()

# END SETUP




### PROBLEM 2.1
def initialize_word_dict(uniquewords):
    """Returns a dictionary where each word becomes a key and its value is 0.
    
    Parameters: 
        unique words (list).

    Returns:
        dict: dictionary of words and 0 as their initial counts.
    """

    # pass # TODO implement

    word2count = {}
    for word in uniquewords:
        word2count[word] = 0
    return word2count 

### PROBLEM 2.2
def get_counts(list_of_words, word2count):
    """Returns the input dictionary after counting each key (word).
    
    Parameters:
        list and dict: list of words in a lyrics and the initial dictionary.
    
    Returns:
        dict: dictionary of words and their counts.
    """

    # pass # TODO implement

    for word in list_of_words:
        word2count[word] += 1
    return word2count
    

### PROBLEM 2.3
def find_most_frequent_word(word2count):
    """Returns the most frequent word.

    Parameters:
        dict: dictionary of words and their counts.

    Returns:
        str: the most frequent word.
    """

    #pass # TO DO implement

    max_count = 0 
    for word, counts in word2count.items():
        if counts > max_count:
            max_count = counts
            most_frequent_word = word
    return most_frequent_word
    

def main():
    """Program entry point.  Handles program workflow (or words to that effect).

    Parameters:
        None

    Returns:
       None
    """

    #pass #TODO implement

    ### Problem 1.1 (5 points ) 
    streaming_subscription_info['Disney Plus'] = '$6.99'
    streaming_subscription_info['Youtube TV'] = '$40.00'
    #OR
    #streaming_subscription_info.update({'Disney Plus':'$6.99','Youtube TV':'$40.00'})
    
    ## NOTE: Problem 1.2 is just for the purpose of exploration. 
    #print(streaming_subscription_info['Hulu'])
    #print(streaming_subscription_info['Netflix'])
    #print(streaming_subscription_info['Youtube TV'])

    ### Problem 2.1 (5 points) 
    word2count = initialize_word_dict(unique_words)
    #print(word2count) #for the purpose of exploration.

    ### Problem 2.2 (5 points) 
    list_of_words_in_the_lyrics = convert_to_list_of_words(baby_shark_lyrics)
    word2count = get_counts(list_of_words_in_the_lyrics,word2count)
    #print(word2count) #for the purpose of exploration.

    ###Problem 2.3 (5 points)
    most_frequent_word = find_most_frequent_word(word2count)

#Do not delete the lines below.
if __name__ == '__main__':
    main()
