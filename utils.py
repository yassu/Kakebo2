#!/usr/bin/env python3
from itertools import dropwhile as _dropwhile


def is_dummy_str(text):
    return list(filter(lambda c: c not in ('\n', '\t', ' ', '\r'), text)) == []


def except_both_ends(text):
    # except head of text
    text = ''.join(
        list(_dropwhile(lambda c: c in (' ', '\t', '\n', '\r'), text)))
    # reverse text
    print(text)
    text = ''.join(list(text).reverse())
    # except end of text
    text = _dropwhile(lambda c: c in (' ', '\t', '\n', '\r'), text)
    # reverse text
    text = ''.join(list(text).reverse())

    return text


def is_dummy_str_test():
    dummy_text = '  \n  \r  \t  '
    print(is_dummy_str(dummy_text))  # -> True

    non_dummy_text = 'ahfp   qrjpq   '
    print(is_dummy_str(non_dummy_text))  # -> False


def except_both_ends_test():
    text = '  ab  c  def '
    print(except_both_ends(text))


if __name__ == '__main__':
    except_both_ends_test()
