#! usr/bin/python3

states = ['Kansas', 'Nebraska', 'North Dakota', 'South Dakota']


def functional_urls(states):
    return [urlify(state) for state in states]


def urlify(string):
    """Return a url friendly version of a string.
    
    Example: 'North Dakota' -> 'north-dakota'
    """
    return '-'.join(string.lower().split())

def full_url(string):
    return [f'https://example.com/{urlify(state)}' for state in states ]


print(functional_urls(states))
print(full_url(states))