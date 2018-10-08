from functionality.exceptions import IllegalInputException


def parse_array_params(tokenizer, ignore_trailing_comma=False):
    res = []
    while not tokenizer.is_empty() and not tokenizer.is_next_reserved_keyword():
        curr = tokenizer.get_next()
        if curr[-1] == ',':
            if not ignore_trailing_comma and tokenizer.is_next_reserved_keyword():
                raise IllegalInputException('Expected a another argument after ","')

        res.extend([param for param in curr.split(',') if param])

    return res
