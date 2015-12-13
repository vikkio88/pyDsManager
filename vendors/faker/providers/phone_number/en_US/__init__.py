from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '+##(#)##########',
        '+##(#)##########',
        '0##########',
        '0##########',
        '###-###-####',
        '(###)###-####',
        '1-###-###-####',
        '###.###.####',
        '###-###-####',
        '(###)###-####',
        '1-###-###-####',
        '###.###.####',
        '###-###-####x###',
        '(###)###-####x###',
        '1-###-###-####x###',
        '###.###.####x###',
        '###-###-####x####',
        '(###)###-####x####',
        '1-###-###-####x####',
        '###.###.####x####',
        '###-###-####x#####',
        '(###)###-####x#####',
        '1-###-###-####x#####',
        '###.###.####x#####'
    )