import textdistance

string_a = 'Hello World!'
string_b = 'Hello Word!'

algs = textdistance.algorithms
lev_dis = algs.levenshtein.distance(string_a, string_b)
# Distance equals 1.0
lev_sim = algs.levenshtein.similarity(string_a, string_b)
# Similarity equals 11
lev_norm_sim = algs.levenshtein.normalized_similarity(string_a, string_b)
# Similarity Normalized equals 0.9166666666666666

print('Levenshtein Distance:', lev_dis)
print('Levenshtein Similarity:', lev_sim)
print('Levenshtein Normalized Similarity:', lev_norm_sim)