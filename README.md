WHoney

Whoney is ready!  

WHoney can also be found from Heroku:
https://whoney.herokuapp.com

Instructions to use the app:
* You are a beekeeper. Please register at first.
* After you have registered, go and make your own hive. You need to go and buy a queen first. 
Every hive has only one queen.
* After yyou have bought your queen, buy a hive and place the queen there.
* Then as a beekeeper, your most important task is to go and check that the bees are ok, IN EVERY TWO WEEKS. 
That is the reason the "hoiva" is at first in the app.
* So go and take care of the bees in your hive. You can say that everything is ok, or if you spot something weird, 
say that everything is not ok and your remark is presented in the home page of the app as long as it is not fixed.
* Your second important job as a beekeeper is to add boxes. If the hive gets too full, the bees get angry and fly away.
So remember to add boxes (not too soon though, they might freeze if you put them there too early)!
* Then after the summer you can harvest the honey (in every hive two boxes remain there for the bees, only extra boxes can be harvested).
* After you have harvested the honey, you need to feed the bees. Give them some sugar. One hive takes 20-25 kg of sugar every fall.
* Then you can also do some pest control. Give them tymol-tyyny every spring!
* Finally, to keep you up to date, you can go and see the log page. 

Apologies for: the visuals, at least the way they are coded. This is my first app ever and because I wanted to learn, I didn't use bootstrap or anything. 
Probably should have because it shows! Sorry! But learned a lot.
_________________

Ready so far:
DB descriptions, login/user registration, page structure, all functions that insert info to db, some presentation of hive related info selected from db in careactions page. 

Biggest WIP issues (sorry!): Detailed statistics and visuals. Some input evaluations in DB, html data checks should be ok. Refactoring of especially routes.py.

This is my first app ever, so all feedback is highly appreciated!

WHoney can also be found from Heroku:
https://whoney.herokuapp.com

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

