usage: unfollow_lamesters.py [-h] [-p PASSWORD] [-D]
                             screen_name terms [terms ...]

Search the description/bio field of your twitter friends to root out potential
lamesters

positional arguments:
  screen_name           Screen name of twitter user whose friends list you'd
                        like to search against
  terms                 The case-insensitive terms you'd like to search
                        descriptions for (e.g. 'SEO', 'social media').

optional arguments:
  -h, --help            show this help message and exit
  -p PASSWORD, --password PASSWORD
                        Password of twitter account. Only necessary for
                        destructive operation.
  -D, --destructive     Act destructively. That is, unfollow those who match
                        your search.
