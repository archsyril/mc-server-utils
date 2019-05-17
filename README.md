# mc-server-utils
just small things i make for minecraft servers.

## last-online.py
what this does is print a sorted list of players in the format of...
```
PLAYERS         DAYS HR:MN
player-name1       0 10:02
player-name2       3 02:45
player-name3      10 00:01
player-name4      11 23:50
```
player1 would have been last online 10 hours and 2 minutes ago, while player4 would have been last online 4 days, 23 hours and 50 minute ago.

tested for python 2.7.16 & python 3.7.3. not tested for code readability.

**HOW TO USE**
`python last-online.py [usercache location: optional]`

if you execute this file in the same directory as the usercache.json file (typically the server root), supplying the `usercache` location is not required.
