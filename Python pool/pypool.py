import multiprocessing
import time
from string import punctuation

text = "Hello World!, this is the text to be reduced. We need to split this text and then remove all the words shorter than 5 characters. " * 100

def clean_word(word):
    for c in word:
        if c in punctuation:
            word = word.replace(c,'')
    if len(word) > 5:
        return word
    
def clean_word_multi(word, word_len):
    for c in word:
        if c in punctuation:
            word = word.replace(c,'')
    if len(word) > word_len:
        return word

if __name__ == '__main__':
    ### SINGLE PARAMETER ###
    # For loop
    start_time = time.perf_counter()
    result = []
    for word in text.split():
        result.append(clean_word(word))
    print('For Loop:', time.perf_counter() - start_time)
    
    # List Comprehension
    start_time = time.perf_counter()
    result = [clean_word(word) for word in text.split()]
    print('List Comprehension:', time.perf_counter() - start_time)
    
    # Multiprocessing
    start_time = time.perf_counter()
    p = multiprocessing.Pool(processes=4)
    result = p.map(clean_word, text.split())
    print('Pool:', time.perf_counter() - start_time)
    print()

    ### MULTI PARAMETER ###
    # For loop
    start_time = time.perf_counter()
    result = []
    for word in text.split():
        result.append(clean_word_multi(word, 5))
    print('For Loop:', time.perf_counter() - start_time)
    
    # List Comprehension
    start_time = time.perf_counter()
    result = [clean_word_multi(word, 5) for word in text.split()]
    print('List Comprehension:', time.perf_counter() - start_time)
    
    # Multiprocessing
    start_time = time.perf_counter()
    p = multiprocessing.Pool(processes=4)
    result = p.starmap(clean_word_multi, [(word, 5) for word in text.split()])
    print('Pool:', time.perf_counter() - start_time)
    print()