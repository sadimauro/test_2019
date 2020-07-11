#!/usr/bin/env python3

import strcalc
import countryinfo
import collections

DECK_1 = [
    ["AUSTRIA", ""],
    ["AZERBAIJAN", ""],
    ["BARBADOS", ""],
    ["BELGIUM", ""],
    ["BRAZIL", ""],
    ["CANADA", ""],
    ["CUBA", ""],
    ["DENMARK", ""],
    ["FIJI", ""],
    ["FINLAND", ""],
    ["GERMANY", ""],
    ["GHANA", ""],
    ["HUNGARY", ""],
    ["IRAN", ""],
    ["JAPAN", ""],
    ["JORDAN", ""],
    ["KENYA", ""],
    ["LEBANON", ""],
    ["LIBYA", ""],
    ["QATAR", ""],
    ["SUDAN", ""],
    ["SWEDEN", ""],
    ["TURKEY", ""],
    ["UGANDA", ""],
    ["UKRAINE", ""],
    ["VIETNAM", ""],
    ["ZAMBIA", ""],
]

DECK_1_SETS = [
    ["AUSTRIA", "AZERBAIJAN", "LIBYA"],
    ["AZERBAIJAN", "BARBADOS", "BELGIUM"],
    ["CANADA", "KENYA", "SUDAN"],
    ["JAPAN", "SWEDEN", "ZAMBIA"],
    ["JORDAN", "QATAR", "UKRAINE"],
]

def fill_fields(country_name = None, capital_name = None, sets = None):
    k = []
    v = []
    if not country_name:
        return None

    country_info = countryinfo.CountryInfo(country_name.title())
    if not capital_name or capital_name == "":
        capital_name = country_info.capital()

    k.append("sets")
    sets_list = []
    for i in range(len(sets)):
        if country_name in sets[i]:
            sets_list.append(str(i+1))
    v.append(';'.join(sets_list))
    
    k.append("country")
    v.append(country_name)

    k.append("name_len")
    v.append(str(len(country_name)) )

    k.append("name_len_mod3")
    v.append(str(len(country_name) % 3))

    k.append("scrabble")
    v.append(str(strcalc.scrabble_val(country_name)))

    k.append("scrabble_mod3")
    v.append(str(strcalc.scrabble_val(country_name) % 3))

    k.append("phone")
    v.append(str(strcalc.phone_val(country_name)))

    k.append("phone_mod3")
    v.append(str(strcalc.phone_val(country_name) % 3))

    k.append("ord_value_0")
    v.append(str(strcalc.ord_val(country_name, zero_based=True)))

    k.append("ord_value_1")
    v.append(str(strcalc.ord_val(country_name, zero_based=False)))

    k.append("ord_value_0_mod_3")
    v.append(str(strcalc.ord_val(country_name, zero_based=True) % 3))

    k.append("ord_value_1_mod_3")
    v.append(str(strcalc.ord_val(country_name, zero_based=False) % 3))

    k.append("capital")
    v.append(capital_name)

    k.append("name_len")
    v.append(str(len(capital_name)))

    k.append("name_len_mod3")
    v.append(str(len(capital_name) % 3))

    k.append("scrabble")
    v.append(str(strcalc.scrabble_val(capital_name)))

    k.append("scrabble_mod3")
    v.append(str(strcalc.scrabble_val(capital_name) % 3))

    k.append("phone")
    v.append(str(strcalc.phone_val(capital_name)))

    k.append("phone_mod3")
    v.append(str(strcalc.phone_val(capital_name) % 3))

    k.append("alpha_2")
    v.append(country_info.iso()['alpha2'])

    k.append("alpha_3")
    v.append(country_info.iso()['alpha3'])

    k.append("currencies")
    v.append(';'.join(country_info.currencies()))

    k.append("region")
    v.append(country_info.region())

    k.append("tlds")
    v.append(';'.join(country_info.tld()))

    k.append("2name_len % 3")
    v.append(str((len(country_name) + len(capital_name)) % 3))

    return k, v

def print_table_header(deck, sets):
    dummy = deck[0][0]
    print(','.join(fill_fields(dummy, None, sets)[0]))

def print_table_rows(deck, sets):
    for c in deck:
        print(','.join(fill_fields(c[0], c[1], sets)[1]))

if __name__ == "__main__":
    print_table_header(DECK_1, DECK_1_SETS)
    print_table_rows(DECK_1, DECK_1_SETS)
