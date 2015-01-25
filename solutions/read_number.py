import sys
ones = [
    'none',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine']
tens = [
    'none',
    'none',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety']
rest = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen']
power = ['', 'thousand', 'million', 'billion', 'trillion']
power.reverse()


def read_three_dig(number, power):
    if int(number) == 0:
        return ""
    diff = 3 - len(number)
    for i in xrange(diff):
        number = '0' + number
    ret = []
    if number[0] != '0':
        ret.append(ones[int(number[0])] + ' hundred')
    if number[1] not in {'0', '1'}:
        ret.append(tens[int(number[1])])
    if number[1] == '1':
        ret.append(rest[int(number[2])])
        return ' '.join(ret + [power])
    if number[2] != '0':
        ret.append(ones[int(number[2])])
    return ' '.join(ret + [power])


import re


def clean(string):
    return re.sub('(, )+', ', ', string).strip()

number = sys.argv[1]
split = format(int(number), ',').split(',')

if len(split) > 5:
    print "too long"
else:
    extra = len(power) - len(split)
    ans = []
    for i in xrange(len(split)):
        ans.append(read_three_dig(split[i], power[extra + i]))
    print clean(', '.join(ans))

# Example usage :
# python read_number.py 211111102000123
# output :
# two hundred eleven trillion,one hundred eleven billion,one hundred two
# million,one hundred twenty three
