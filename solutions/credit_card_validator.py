"""
reg exps        : taken from http://www.regular-expressions.info/creditcard.html
luhn validation : taken from wikipedia
test cases      : taken from http://creditcardity.com/
"""
import re
import sys

visa = r'^4[0-9]{12}(?:[0-9]{3})?$', "Visa"
mastercard = r'^5[1-5][0-9]{14}$', "Master Card"
am_express = r'^3[47][0-9]{13}$', "American Express"
diners_club = '^3(?:0[0-5]|[68][0-9])[0-9]{11}$', "Diners Club"
discover = r'^6(?:011|5[0-9]{2})[0-9]{12}$', "Discover"
jcb = r'^(?:2131|1800|35\d{3})\d{11}$', "JCB"

cards = [visa, mastercard, am_express, diners_club, discover, jcb]
invalid_message = "Invalid Card Number"
unidentified_message = "Unidentified Card Type"


def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10


def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0


def main(card_string):
    card_string = card_string.replace(" ", "")
    card_string = card_string.replace("-", "")
    try:
        card_int = int(card_string)
        if not is_luhn_valid(card_int):
            return invalid_message
        for exp, message in cards:
            mat = re.match(exp, card_string)
            if mat:
                return message
        return unidentified_message

    except ValueError:
        return invalid_message


def test():
    mastercard_test = (5105105105105100, 5555555555554444)
    diners_club_test = (38520000023237, 30569309025904)
    visa_test = (4222222222222, 4111111111111111, 4012888888881881)
    am_express_test = (378282246310005, 371449635398431, 378734493671000)
    discover_test = (6011111111111117, 6011000990139424)
    jcb_test = (3530111333300000, 3566002020360505)
    tests = {mastercard[1]: mastercard_test,
             diners_club[1]: diners_club_test,
             visa[1]: visa_test,
             am_express[1]: am_express_test,
             discover[1]: discover_test,
             jcb[1]: jcb_test}
    total_tests = 0
    failed_tests = 0
    for card_type, card_numbers in tests.iteritems():
        for card in card_numbers:
            if card_type != main(str(card)):
                failed_tests += 1
            total_tests += 1
    if failed_tests != 0:
        print "%s out %s tests failed" % (failed_tests, total_tests)
    else:
        print "all tests passed"


if __name__ == '__main__':
    args = len(sys.argv)
    if args > 1 and sys.argv[1] == "test":
        test()
    else:
        cardnumer = raw_input("Enter card number : ")
        print main(cardnumer)
