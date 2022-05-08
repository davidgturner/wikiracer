"""
To convert from similarity to distance:

If your similarity measure (s) is between 0 and 1, you can use one of these:
1.) 1-s
2.) sqrt(1-s)
3.) -log(s)
4.) (1/s)-1

These are some well-known strictly monotone decreasing candidates that work for non-negative
similarities or distances:

f(x) = 1 / (a + x)
f(x) = exp(- x^a)
f(x) = arccot(ax)

similarity = 1/difference

"""

# from math import pi, acos
#
# def cosine_similarity(x, y):
#     x=ord(x)
#     y=ord(y)
#     return sum(x[k] * y[k] for k in x if k in y) / \
#            sum(v**2 for v in x.values())**.5 / sum(v**2 for v in y.values())**.5

# # computes a distaince given a similarity
# def similarity(x, y):
#     pass
from math import sqrt, log


def distance_cost(similarity_score):
    scaler = 100

    # 4 different ways of converting similarity to cost distance averaged out
    cost_dist_1 = 1-similarity_score
    cost_dist_2 = sqrt(1-similarity_score) * scaler
    cost_dist_3 = -log(similarity_score)
    cost_dist_4 = (1 / similarity_score) - 1

    cost_distance_method_count = 4

    return scaler * ((cost_dist_1 + cost_dist_2 + cost_dist_3 + cost_dist_4) / cost_distance_method_count)


def overlap_similarity(str1, str2):
    """
    is this overlap similarity the same as the official overlap coefficient
    """
    overlap_count = string_overlap_count(str1, str2)

    str1 = str1.replace("/wiki/","")
    str2 = str2.replace("/wiki/", "")

    tokens_str1_set: set = set(str1.split("_"))
    tokens_str2_set: set = set(str2.split("_"))

    total_token_count = len(tokens_str1_set) + len(tokens_str2_set)

    return overlap_count / total_token_count

def string_overlap_count(str1, str2):
    str1 = str1.replace("/wiki/","")
    str2 = str2.replace("/wiki/", "")

    tokens_str1_set: set = set(str1.split("_"))
    tokens_str2_set: set = set(str2.split("_"))

    intersection_set = tokens_str1_set.intersection(tokens_str2_set)
    return len(intersection_set)

s1 = "/wiki/Hitler_count_blah"
s2 = "/wiki/Jesus_count_blah_blah_Hitler"
c = overlap_similarity(s1, s2)
print("s1 ", s1, " s2 ", s2, " overlap similarity ", c)
print("s1 ", s1, " s2 ", s2, "distance ", sqrt(1-c)*100)

s1 = "/wiki/Baseball"
s2 = "/wiki/Baseball_player"
c = overlap_similarity(s1, s2)
print("s1 ", s1, " s2 ", s2, " overlap similarity ", c)
print("s1 ", s1, " s2 ", s2, " distance ", sqrt(1-c)*100)

# print(cosine_similarity(s1, s2))
