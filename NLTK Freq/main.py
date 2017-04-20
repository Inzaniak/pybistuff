import nltk

# Let's declare a function to get word index
def get_index(in_list,in_string):
    for num,row in enumerate(in_list):
        if in_string in row:
            return num

# Let's open the book we downloaded
book = open('data/ebook.txt','r').read()
# Divide text by rows
rows = book.split('\n')

# Search for START and END tags to remove useless parts
start_idx = get_index(rows,'*** START')
end_idx = get_index(rows,'*** END')
rows = rows[start_idx+1:end_idx]

# Create a list of words by converting to lowercase and splitting
words = [s.lower().split() for s in rows if s]
# Convert the list of lists into a flat list
words = [sublist for l in words for sublist in l]

# Import the stopwords
stop = open('data/stop.txt','r').read()
# Split the stopwords by line
stop = stop.split('\n')

# Remove punctuation and numbers from words
words = [''.join(c for c in w if c.isalpha()) for w in words]
# Remove stopwords and blanks from words
words = [w for w in words if w not in stop and w.isalpha()]

# Let's load the word into NLTK
text = nltk.Text(words)

# Calculate Frequency distribution
freq = nltk.FreqDist(text)

# Print and plot most common words
freq.most_common(20)
freq.plot(10)

# Get Bigrams from text
bigrams = nltk.bigrams(text)

# Calculate Frequency Distribution for Bigrams
freq_bi = nltk.FreqDist(bigrams)

# Print and plot most common bigrams
freq_bi.most_common(20)
freq_bi.plot(10)