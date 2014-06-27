def util_create_keywords(value):
    return map(lambda key: {'term': key}, value.split('|'))
