# Вариант 6
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def decorator(func):
    def div(string):
        tag = 'div'
        return func(string.replace(string, "<{0}>{1}</{0}>".format(tag, string)))

    return div


@decorator
def lower(tag):
    s = tag.lower()
    return s


if __name__ == '__main__':
    print(lower("ДЛЯ ТЕХ, КТО ЗАБЫВАЕТ УБРАТЬ CAPS LOCK. ЕСЛИ НАПИСАЛ ВСЕ КАПСОМ, А ОНО ТЕБЕ НЕ НАДО - нажми Shift "
                "+ F3. НО только Word! И даже не пытайся обмануть Excel!"))
