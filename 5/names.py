NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    names = list(set(names))
    title_names_list = [name.title() for name in names]
    return title_names_list


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    sort_surname_list = sorted(names, reverse=True, key=lambda name: name.split(" ")[1])
    return sort_surname_list

def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = sort_by_surname_desc(names)
    sort_by_len_list = sorted(names, key=lambda item: (len(item.split(" ")[0])))
    return sort_by_len_list[0].split(" ")[0]

shortest_first_name(NAMES)
