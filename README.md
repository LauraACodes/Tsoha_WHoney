Ready so far:
DB descriptions, login/user registration, page structure, all functions that insert info to db, some presentation of hive related info selected from db in careactions page. 

Biggest WIP issues (sorry!): Detailed statistics and visuals. Some input evaluations in DB, html data checks should be ok. Refactoring of especially routes.py.

This is my first app ever, so all feedback is highly appreciated!

WHoney can also be found from Heroku:
https://tsoha-whoney.herokuapp.com

The system creates some required basic info to the app.

Begin with creating a account. 

Then try the following yourself: Take care of the bees of some hive. You can e.g. add a box, report a check up (tell that everything is NOT ok), and give some sugar to them (they actually get sugar-water mix, but the intake is counted in sugar kgs).

Then from the main page you can go and tell that you have bought a queen and a hive. 
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

In the data warehouse each of these would have their own table,
and also several links (joint table?) between them. Some additional tables
probably too, e.g. possible jar sizes.

Then I could fetch info on (again e.g.):
- Which actions have been done in each hive in time-order?
- Which hives are don't have a certain action done this season?

