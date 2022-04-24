import re

from py_wikiracer.internet import Internet


def valid_url_pattern(test_str: str):
    diss_list = []
    for x in Internet.DISALLOWED:
        #print(re.escape(x))
        # patt += re.escape(x)
        if x == '/':
            diss_list.append(re.escape(x + "/"))
        else:
            diss_list.append(re.escape(x))
    # some_chars = ",".join(Internet.DISALLOWED)
    # print(some_chars)
    exclude_pattern_2: str = "|".join(diss_list)
    #
    # escaped_exclude_pattern: str = re.escape(exclude_pattern_2)
    #
    #print(exclude_pattern_2)
    #
    #print(bool(re.search(exclude_pattern_2, '/wiki/Crystal_Lake,_Illinois')))
    return bool(re.search(exclude_pattern_2, test_str))


print(valid_url_pattern("blah"))