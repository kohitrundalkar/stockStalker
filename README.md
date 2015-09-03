# stockStalker
# Statutory warning: Developers tend to be lazy when it comes to readme files and documentatio.
# So this readme file could be outdated. If the behavior of the program is different than what's written here
# then figure it out yourself. Don't bother us. Because quite frankly, we don't care.
# You have been warned!

The Stack Stalker is a simple stocks value tracker. Currently it does following things.
1) Imports portfolio from a file and tracks the value in (nowhere) near realtime manner using yahoo financial APIs.
   The delay is same (a few milliseconds more) than what yahoo says, since they themselves show data
   which is about 20 min old.

2) Imports a list of stocks that the user wants to be on their watchlist and tracks their values.

3) Imports a list of triggers for each of the stocks from both the portfolio list and the stock watchlist files
   and sends notifications to the user via email. Oh yeah! It also needs users' contact info in a file.

So, there are total 3 files it expects in the beginning.
i) Portfolio list file
ii) Stocks watchlist file
iii) Contact info (e-mail) file

FILE FORMATS
For portfolio and watchlist file, the format is as follows.
For both these files, each line will contain one symbol and then the price that acts as a trigger/threshold
separated by pipe.

eg.

GOOG|gt 612.0|lt 595.50 |eq 600
YHOO|lt 32
AAPL|gt 133.2

In the example above, GOOG, YHOO etc are the symbols.
gt: Greater Than
lt: Less Than
eq: Equal To

So for GOOG, there are three triggers. if value goes above $612, if it goes below $595 and if it is equal to 600.
So if any of those conditions are met, an email will be sent to the user with the current value of that stock.
Same goes for YHOO and AAPL.

NOTE: Here the trigger gt 612.0 doesn't mean that the application will keep sending emails as long as it is below 612. It will
send it only once. The next time a notification is sent is when the stock value goes above 612 and then falls back below
$612.

Format of the contact info file is simple
Line 1 is Name of the user
Line 2 is email address

eg
John Smith
johnsmith@mail.com
