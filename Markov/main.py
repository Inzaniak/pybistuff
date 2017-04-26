import nltk

# Let's declare a function to get word index
def get_index(in_list,in_string):
    for num,row in enumerate(in_list):
        if in_string in row:
            return num

# We convert the script from the NLTK Stopwords tutorial into a def
def clean_book(path):
    # Let's open the book we downloaded
    book = open(path,'r').read()
    # Divide text by rows
    rows = book.split('\n')
    # Search for START and END tags to remove useless parts
    start_idx = get_index(rows,'*** START')
    end_idx = get_index(rows,'*** END')
    rows = rows[start_idx+1:end_idx]
    # We need to create a string for markovify
    text = '\n'.join([r for r in rows if r!=''])
    return text

import markovify

# Build the model.
ebook_a = clean_book('data/ebook.txt')
text_model_a = markovify.Text(ebook_a)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model_a.make_sentence())

# Print three randomly-generated sentences of no more than 140 characters
for i in range(3):
    print(text_model_a.make_short_sentence(140))

# Recreate the model using 3 sentences 
three_model = markovify.Text(ebook_a,state_size=3)
for i in range(5):
    print(three_model.make_sentence())
    
# Build the second model.
ebook_b = clean_book('data/ebook2.txt')
text_model_b = markovify.Text(ebook_b)
for i in range(5):
    print(text_model_b.make_sentence())
    
# Combine the models into a single one
both_models = markovify.combine([text_model_a,text_model_b])
for i in range(5):
    print(both_models.make_sentence())
    