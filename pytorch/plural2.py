import re, json


def matches_out(pattern):
    def match_in(word):
        if pattern is None:
            return True
        else:
            return re.search(pattern, word)
    return match_in


def apply_out(search, replace):
    def apply_in(word):
        return re.sub(search, replace, word)
    return apply_in


def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return (matches_rule, apply_rule)


def plural(noun):
    with open('rules.json', 'r', encoding='utf-8') as f:
        patterns = json.load(f)

    # rules = [build_match_and_apply_functions(pattern, search, replace) for (pattern, search, replace) in patterns]
    rules = []
    for (pattern, search, replace) in patterns:
        rules.append((matches_out(pattern), apply_out(search, replace)))

    for matches_rule, apply_rule in rules:
    #    (matches_rule, apply_rule) = rule
    #    # matches_rule = rule[0]
    #    # apply_rule = rule[1]
        if matches_rule(noun):
           return apply_rule(noun)


print(plural('lolly'))
