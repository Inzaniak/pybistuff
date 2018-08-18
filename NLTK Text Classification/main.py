from nltk import NaiveBayesClassifier
from nltk import classify
import random

ITA = open('data/italiano_utf.txt','r',encoding='utf-8').read().split('\n')
ENG = open('data/english_utf.txt','r',encoding='utf-8').read().split('\n')

def language_features(name):
    features = {}
    features["first_letter"] = name[0].lower()
    features["last_letter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = name.lower().count(letter)
        features["has({})".format(letter)] = (letter in name.lower())
    return features

labeled_words = ([(word, 'english') for word in ENG] +
                 [(word, 'italian') for word in ITA])
random.shuffle(labeled_words)
 	
featuresets = [(language_features(n), language) for (n, language) in labeled_words]
train_test = int(len(featuresets)/2)
train_set, test_set = featuresets[train_test:], featuresets[:train_test]
classifier = NaiveBayesClassifier.train(train_set)
print(classify.accuracy(classifier, test_set))

print(classifier.classify(language_features('Hello'))) # CORRECT
print(classifier.classify(language_features('Ciao'))) # CORRECT
print(classifier.classify(language_features('Incredibile'))) # WRONG
print(classifier.prob_classify(language_features('Incredibile')).prob("english")) # WRONG

classifier.show_most_informative_features(10)

wiki_eng = open('data/wiki_eng.txt','r',encoding='utf-8').read().split()
wiki_eng = list(set(wiki_eng))
wiki_lang = []
for w in wiki_eng:
    wiki_lang.append([w,classifier.classify(language_features(w))])
words_ita = len([w for w in wiki_lang if w[1] == 'italian'])
words_eng = len([w for w in wiki_lang if w[1] == 'english'])
print('Italian: {} | English: {}'.format(words_ita,words_eng))