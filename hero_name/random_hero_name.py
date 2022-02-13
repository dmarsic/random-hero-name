# MIT License
#
# Copyright (c) 2022 Dom Marsic
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from random import choice, choices

def random_name():
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'ai', 'ei', 'oe', 'oo', 'au']
    vowel_weights = [15, 9, 8, 3, 2, 1, 2, 2, 2, 1, 1]
    single_cons = [
        'p', 't', 'k', 's', 'f',
        'b', 'd', 'g', 'j', 'z']
    double_cons = [
        'pp', 'pt', 'ps', 'ph', 'pr', 'pl', 'py',
        'tt', 'tk', 'ts', 'th', 'tr', 'tn', 'tl', 'ty',
        'kt', 'kk', 'kr', 'kn', 'km', 'kl', 'ky',
        'sp', 'st', 'sk', 'ss', 'sh', 'sr', 'sn', 'sm', 'sl', 'sy',
        'fr', 'fl', 'fy',
        'bb', 'br', 'bl', 'by',
        'dd', 'dr', 'dl', 'dy',
        'gg', 'gr', 'gl', 'gy',
        'jy',
        'zz', 'zr', 'zm', 'zl', 'zy',
        'rt', 'rk', 'rb', 'rd', 'rg', 'rn', 'rm', 'ry',
        'nn', 'nm', 'ny',
        'mp', 'mk', 'md', 'mr', 'mn', 'mm', 'ml', 'my',
        'ln', 'lm', 'll', 'ly']
    end_cons = ['', 'r', 'n', 's', 'ss']
    end_cons_weights = [6, 3, 3, 2, 1]

    name = ""
    # First block
    name += choice(single_cons)
    name += choices(vowels, weights=vowel_weights, k=1)[0]
    # Second block
    name += choice(single_cons + double_cons)
    name += choices(vowels, weights=vowel_weights, k=1)[0]
    name += choices(end_cons, weights=end_cons_weights, k=1)[0]
    return name.title()
