# random-hero-name

## Intro

In need of a hero name? Get some ideas here.

This Python module contains just one function, `hero_name.random_hero_name.random_name()`. It generates a almost-pronounceable name, following a few simple rules to string consonants and wovels together.

Example names:

```
Zarber
Barman
Septe
Tipsen
Gakta
Bimma
Kampe
Jeklar
Fefre
Perdiss
```

## Usage

Example on how to use it in your program:

```python
from hero_name.random_hero_name import random_name

if __name__ == '__main__':
    print(random_name())
```

You can test it by running the included script:

```bash
$ python3 get_names.py

0 Zepyair
1 Teibber
2 Suthan
3 Fifyer
4 Pastoen
5 Dibo
6 Gitke
7 Jozrin
8 Dotu
9 Joetkas
```

Doesn't sound right? Play with weights in the function, both for wovels and end consonants.

## Author

Dom Marsic, 2022
