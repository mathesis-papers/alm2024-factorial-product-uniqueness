import json
from fractions import Fraction
from math import factorial, prod
from itertools import accumulate


LEFT = (10, 17, 21, 23, 24, 27, 38, 45, 46, 48, 56, 65, 68, 77, 80, 84, 95, 141)
RIGHT = (11, 16, 20, 22, 25, 26, 39, 44, 47, 49, 57, 64, 69, 76, 81, 85, 94, 140)
START_U = (16, 20, 22, 26, 44, 64, 76, 94, 140)
START_V = (10, 24, 38, 46, 48, 56, 68, 80, 84)
EXPECTED = {2: 1150, 3: -326, 5: -42, 7: 44, 11: -10,
            13: -38, 17: -16, 19: -18, 23: -22, 47: -46}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def prime_factors(integer):
    require(integer >= 2, 'Factorization requires an integer at least two')
    remainder = integer
    factors = {}
    divisor = 2
    while divisor * divisor <= remainder:
        exponent = 0
        while remainder % divisor == 0:
            exponent += 1
            remainder //= divisor
        if exponent:
            factors[divisor] = exponent
        divisor += 1
    if remainder > 1:
        factors[remainder] = factors.get(remainder, 0) + 1
    require(prod(prime ** exponent for prime, exponent in factors.items()) == integer,
            'Prime factor reconstruction failed')
    return factors


def ratio_valuations(starts):
    valuations = {}
    for integer in starts:
        for sign, endpoint in ((1, integer), (-1, integer + 1)):
            for prime, exponent in prime_factors(endpoint).items():
                valuations[prime] = valuations.get(prime, 0) + sign * integer * exponent
    return dict(sorted(valuations.items()))


def factorial_product(parameters):
    return prod((Fraction(factorial(integer), integer ** integer)
                 for integer in parameters), start=Fraction(1))


def main():
    require(len(LEFT) == len(RIGHT) == 18, 'Wrong cardinality')
    require(len(set(LEFT)) == len(set(RIGHT)) == 18, 'Repeated parameter')
    require(set(LEFT).isdisjoint(RIGHT), 'Sets must be disjoint')
    require(min(LEFT + RIGHT) > 1, 'Parameter outside the stated domain')
    require(all(integer % 2 == 0 for integer in START_U + START_V), 'Starts must be even')
    require(len(set(START_U + START_V)) == 18, 'Starts must be distinct')
    require(set(LEFT) == set(START_V) | {integer + 1 for integer in START_U},
            'Left adjacent-pair reconstruction failed')
    require(set(RIGHT) == set(START_U) | {integer + 1 for integer in START_V},
            'Right adjacent-pair reconstruction failed')
    valuations_u = ratio_valuations(START_U)
    valuations_v = ratio_valuations(START_V)
    require(valuations_u == valuations_v == EXPECTED, 'Prime-exponent table differs')
    rational_u = prod((Fraction(integer, integer + 1) ** integer for integer in START_U),
                      start=Fraction(1))
    rational_v = prod((Fraction(integer, integer + 1) ** integer for integer in START_V),
                      start=Fraction(1))
    certificate = prod((Fraction(prime) ** exponent for prime, exponent in EXPECTED.items()),
                       start=Fraction(1))
    require(rational_u == rational_v == certificate, 'Adjacent-ratio identity failed')
    direct_left = factorial_product(LEFT)
    direct_right = factorial_product(RIGHT)
    require(direct_left == direct_right, 'Direct factorial products differ')
    require(sum(LEFT) == sum(RIGHT) == 965, 'Parameter sums differ')
    require(sum(START_U + START_V) == 956, 'Starting-index sum differs')
    partial_left = list(accumulate(sorted(LEFT, reverse=True)))
    partial_right = list(accumulate(sorted(RIGHT, reverse=True)))
    require(partial_left[0] == 141 and partial_right[0] == 140,
            'First partial sums differ')
    require(partial_left[8] == 714 and partial_right[8] == 715,
            'Ninth partial sums differ')
    require(not all(left <= right for left, right in zip(partial_left, partial_right)),
            'Unexpected weak majorisation')
    require(not all(right <= left for left, right in zip(partial_left, partial_right)),
            'Unexpected reverse weak majorisation')
    extension_checks = []
    for cardinality in (18, 19, 20, 25):
        common = tuple(range(142, 142 + cardinality - 18))
        extended_left = LEFT + common
        extended_right = RIGHT + common
        require(len(set(extended_left)) == len(set(extended_right)) == cardinality,
                'Extension cardinality differs')
        require(factorial_product(extended_left) == factorial_product(extended_right),
                'Extension products differ')
        require(sum(extended_left) == sum(extended_right), 'Extension sums differ')
        require(len(set(extended_left) ^ set(extended_right)) == 36,
                'Extension symmetric difference differs')
        extension_checks.append(cardinality)
    descending_products = [factorial_product(LEFT + (integer,)) for integer in (142, 143, 144)]
    require(descending_products[0] > descending_products[1] > descending_products[2],
            'Strictly decreasing common values differ')
    print(json.dumps({
        'statement': 'Two disjoint eighteen-element integer sets have equal products of m!/m^m.',
        'left': LEFT,
        'right': RIGHT,
        'factorial_product_equality': True,
        'adjacent_ratio_equality': True,
        'prime_exponents_u': valuations_u,
        'prime_exponents_v': valuations_v,
        'cardinalities': [18, 18],
        'disjoint': True,
        'parameter_sums': [965, 965],
        'decreasing_partial_sums_left': partial_left,
        'decreasing_partial_sums_right': partial_right,
        'weak_majorisation_incomparable': True,
        'common_extension_cardinalities_checked': extension_checks,
        'distinct_common_values_for_parameters': [142, 143, 144],
        'arithmetic': 'Exact integers and fractions.Fraction; no floating-point arithmetic.',
        'scope': 'The displayed sets, adjacent-ratio identity, prime-exponent table, sums, partial sums, and the listed finite extensions. Universal extension statements have written proofs in note.tex.'
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
