import json, re


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


class lazyRules:
    rules_filename = 'plural4-rules.txt'

    def __init__(self, filename):
        self.pattern_file = open(self.rules_filename, encoding='utf-8')

    #        with open(filename, 'r', encoding='utf-8') as f:
    #            self.patterns = json.load(f)
    #            # print(self.patterns)
    #            self.max = len(self.patterns) - 1
    #            # print(self.max)

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        # print(self.current)
        # pattern = self.patterns[self.current][0]
        # search = self.patterns[self.current][1]
        # replace = self.patterns[self.current][2]
        if self.pattern_file.closed:
            raise StopIteration

        #        if self.current > self.max:
        #            raise StopIteration

        line = self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration

        # (pattern, search, replace) = self.patterns[self.current]
        pattern, search, replace = line.split(None, 2)
        print(pattern, search, replace)
        self.current += 1

        return matches_out(pattern), apply_out(search, replace)


def plural(noun):
    rules = lazyRules('rules.json')
    for matches_out, apply_out in rules:
        if matches_out(noun):
            return apply_out(noun)


print(plural('lolly'))
