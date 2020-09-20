Ready so far:
DB descriptions, main elements of moving from main page to other pages, & selecting onfo from db to index page. = Not that much so far because I'm struggling with how to save data to db with FKs. Started that in the investments-page but doesn't work..

WHoney can also be found from Heroku:
https://tsoha-whoney.herokuapp.com

_____________

WHoney

I farm bees as a hobby and hopefully in the future, as a small extra income.
Because bees are production animals, the farmer needs to keep records on
the animals, caretaking actions and also the honey. 

For this purpose I'll build WHoney (our brand is "Wilmalan Hunaja") where
I can log e.g. (these actions will change the database):
- The queens: are they bought or self-bred, when, where?
- The hives: where, which queen, did it survive the winter, diseases.
- The farms: where are the farms located, when.
- Caretaking actions: which and when (check-up, feeding, disease control, queen change..)
- Harvesting and spinning (? linkous in FI): when, from which hive, how much.
- Storage: how much raw honey, different sized jarred honey and from which harvest batch.
- Costs: What kins of investments to equipment, queens, sugar, disease control etc.
- Profits: What sold and to what price.

In the data warehouse each of these would have their own table,
and also several links (joint table?) between them. Some additional tables
probably too, e.g. possible jar sizes.

Then I could fetch info on (again e.g.):
- Which actions have been done in each hive in time-order?
- Which hives are don't have a certain action done this season?
- Ranking of honey production of different hives or farms?
- Total production for a season?
- Total profits for each season?
- Warehouse situation, quantity and value.
