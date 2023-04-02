# :new_moon: Ex0 IN intro NewSpace(Bereshit ):new_moon:


 ![](https://www.space.gov.il/sites/default/files/styles/690_350/public/spaceIL.jpg?itok=eoMu-3ea)


# חלק הראשון: 

עליכם לכתוב דוח קצר שמסביר במילים שלכם את הסיבות הטכניות להתרסקות – באופן טבעי ישנו מידע רב שאינו זמין לנו, ובכל זאת נסו לחפש היטב את הסיבות ותארו את רצף האירועים הטכניים כפי שאתם מבנים אותם, לצורך כך תוכלו להיעזר בשני המקורות מטה (התייחסו למידע כפי שמוצג בסרטון הזה), אבל כמובן אתם מוזמנים להתבסס גם על כל מקור רלוונטי אחר.

הסיבה להתרסקות:collision::

לא ידוע מה התקלה שהתרחשה ב-IMU, בנוסף העריכו שיחידה זו אינה מהווה בעיה עבור תהליך הנחיתה מאחר וקיימת מערכת גיבוי נוספת.
אך בארץ התקבלה החלטה לאתחל את המערכת מבלי להתייעץ עם המהנדסים.
בזמן האתחול לא התקבלו (לפרק זמן קצר) הנתונים מהמד התקין.
מאחר ולא היה לחללית נתוני ניווט, מחשב החללית איתחל את עצמו מחדש.
האתחול היה אמור להיות 2 שניות, אך בפועל הוא אתחל את עצמו 5 פעמים בעקבות תקלות תוכנה.
בנוסף המנוע אמור לפעול מיד לאחר האתחול, אך הוא לא הופעל במתח הנכון בגלל התקלות תוכנה והאתחולים הרבים.
דבר זה גרם לכך שהמנוע הראשי לא פעל לבלימת החללית (שאר המנועים הקטנים כן פעלו), וזה לא היה מספיק בשביל שהחללית בראשית תוכל לבלום, מה שהוביל אותה לבסוף להתרסקות.

# חלק השני 
(והמרכזי) עליכם לתכנן ולפתח סימולציה לניהוג והנחתה של החללית ע״ג הירח: המיקוד בחלק זה הוא מידול בעיית הסימולציה ופיתוח מערכת בקרה מיטבית אשר תאפשר הנחתה "בטוחה" של בראשית (לפחות בסימולציה), כאשר יש מטרה משנית להגיע עם כמה שיותר דלק לפני הקרקע. לצורך המידול נעשה שימוש בנתוני הירח, והחללית: נתחיל במידול הפיסי של כח משיכת הירח: כידוע אין לירח אטמוספרה. במשימה זו תוכלו להזניח את השפעת הכבידה של כדור הארץ על הירח. לחללית יש מנוע ראשי בעל דחף של 430 ניוטון, ושמונה מנועי הכוון בעלי דחף של 25 ניוטון לכל אחד

#
 
 
 -------------------------------------------------------------------------
 
 
 # The first part:

You must write a short report that explains in your own words the technical reasons for the crash - naturally there is a lot of information that is not available to us, nevertheless try to search carefully for the reasons and describe the sequence of technical events as you structure them, for this purpose you can use the two sources below (refer to the information as shown in this video), but of course you are welcome to rely on any other relevant source as well.

The reason for the crash:collision::

It is not known what the fault occurred in the IMU, in addition they estimated that this unit does not pose a problem for the landing process since there is another backup system.
But in Israel, a decision was made to reboot the system without consulting the engineers.
During the initialization, the data from the normal meter were not received (for a short period of time).
Since the spacecraft had no navigation data, the spacecraft computer rebooted itself.
The boot was supposed to be 2 seconds, but in practice it rebooted itself 5 times due to software glitches.
In addition, the motor should run immediately after the restart, but it was not run at the correct voltage due to software glitches and the many restarts.
This meant that the main engine did not work to brake the spaceship (the other small engines did work), and it was not enough for the Genesis spaceship to be able to brake, which eventually led it to crash.

# The second part
(and the central one) you must plan and develop a simulation for driving and landing the spacecraft by the moon: the focus in this part is modeling the simulation problem and developing an optimal control system that will allow a "safe" landing of the Genesis (at least in the simulation), when there is a secondary goal of arriving with as much fuel as possible before the ground. For the purpose of the modeling, the data of the moon and the spacecraft were used: let's start with the physical modeling of the moon's gravity: as we know, the moon has no atmosphere. In this mission you can neglect the effect of Earth's gravity on the Moon. The spacecraft has a main engine with a thrust of 430 newtons, and eight thrusters with a thrust of 25 newtons each

--------------------------------------------------

 ![](https://images1.calcalist.co.il/PicServer3/2019/04/11/898977/3LM.jpg)

     יורי גריגוריאן
      דניאל עוקבי
       רואן שריף
                                                                                                       
                                                                                                          


