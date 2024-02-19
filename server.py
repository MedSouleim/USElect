from flask_app import app
from flask_app.controllers import admin
# <<<<<<< HEAD
from flask_app.controllers import panda_script
# =======
from flask_app.models.voter import Voter
# >>>>>>> 3c3bf16395b435605074b89d4d06bb470246df0d
# from flask_app.controllers import users_controller
# from flask_app.controllers import sasquatch_controller


@app.route('/adddata')
def add_data():
    data = [{"id":1,"first_name":"Billie","last_name":"Langfield","email":"blangfield0@ehow.com","password":"sC0_Y9vrgd|","region":"Colorado","age":77,"cin":10049982,"vote":True,"is_banned":False,"created_at":"7/21/2023","updated_at":"4/2/2023"},
{"id":2,"first_name":"Terry","last_name":"De Vaux","email":"tdevaux1@google.com.hk","password":"qG0_<3p,X+znIYdc","region":"South Carolina","age":27,"cin":45801167,"vote":False,"is_banned":True,"created_at":"6/20/2023","updated_at":"9/11/2023"},
{"id":3,"first_name":"Sharity","last_name":"Postlethwaite","email":"spostlethwaite2@sphinn.com","password":"nZ2{gwp%l+~d","region":"Illinois","age":35,"cin":50827914,"vote":True,"is_banned":True,"created_at":"7/6/2023","updated_at":"3/9/2023"},
{"id":4,"first_name":"Pacorro","last_name":"Edy","email":"pedy3@google.es","password":"nT2!Uc~e\\","region":"California","age":30,"cin":27562198,"vote":False,"is_banned":False,"created_at":"5/10/2023","updated_at":"11/30/2023"},
{"id":5,"first_name":"Zorana","last_name":"Schuricke","email":"zschuricke4@amazonaws.com","password":"qQ1`A2Ff!E**","region":"New York","age":37,"cin":24071417,"vote":True,"is_banned":True,"created_at":"3/10/2023","updated_at":"9/21/2023"},
{"id":6,"first_name":"Lynn","last_name":"Mc Kellen","email":"lmckellen5@angelfire.com","password":"sF2*?y2HS","region":"Vermont","age":32,"cin":31956729,"vote":True,"is_banned":False,"created_at":"3/10/2023","updated_at":"6/29/2023"},
{"id":7,"first_name":"Townie","last_name":"Greenhill","email":"tgreenhill6@hc360.com","password":"tQ0%UjZObr6/2","region":"Michigan","age":39,"cin":65554487,"vote":True,"is_banned":False,"created_at":"4/27/2023","updated_at":"3/23/2023"},
{"id":8,"first_name":"Halette","last_name":"Simmon","email":"hsimmon7@amazon.co.uk","password":"hS3?e<Ya&","region":"Texas","age":51,"cin":64656225,"vote":False,"is_banned":True,"created_at":"5/29/2023","updated_at":"4/5/2023"},
{"id":9,"first_name":"Maryanne","last_name":"Forsdyke","email":"mforsdyke8@nba.com","password":"gT9?vkC~*~ETx&","region":"Georgia","age":42,"cin":52243177,"vote":True,"is_banned":False,"created_at":"8/8/2023","updated_at":"3/7/2023"},
{"id":10,"first_name":"Rene","last_name":"Wattins","email":"rwattins9@java.com","password":"bW1#>HKM4`eLW","region":"Alabama","age":61,"cin":77529526,"vote":True,"is_banned":False,"created_at":"4/13/2023","updated_at":"12/29/2022"},
{"id":11,"first_name":"Dav","last_name":"Durrington","email":"ddurringtona@bizjournals.com","password":"oW0$8\\2jb%0V0Gy","region":"Ohio","age":25,"cin":84073060,"vote":True,"is_banned":True,"created_at":"7/1/2023","updated_at":"5/30/2023"},
{"id":12,"first_name":"Upton","last_name":"Derrick","email":"uderrickb@unesco.org","password":"aT2\"Yazw$.a@","region":"Massachusetts","age":65,"cin":37260022,"vote":True,"is_banned":False,"created_at":"3/17/2023","updated_at":"10/15/2023"},
{"id":13,"first_name":"Helli","last_name":"Stollenwerck","email":"hstollenwerckc@state.gov","password":"cX4@|Q0a1,n{Xei","region":"District of Columbia","age":18,"cin":66615590,"vote":True,"is_banned":True,"created_at":"7/6/2023","updated_at":"9/20/2023"},
{"id":14,"first_name":"Cleo","last_name":"Appleford","email":"capplefordd@google.pl","password":"aV7\"Y_rbwV","region":"Pennsylvania","age":42,"cin":92531266,"vote":False,"is_banned":False,"created_at":"7/14/2023","updated_at":"5/17/2023"},
{"id":15,"first_name":"Christophe","last_name":"Duigan","email":"cduigane@freewebs.com","password":"mZ0~HG=IrU~","region":"Texas","age":66,"cin":44671130,"vote":False,"is_banned":True,"created_at":"5/24/2023","updated_at":"3/31/2023"},
{"id":16,"first_name":"Donnajean","last_name":"Labrom","email":"dlabromf@ow.ly","password":"cU1`>+5E!xLzFaMc","region":"Massachusetts","age":49,"cin":30405358,"vote":True,"is_banned":False,"created_at":"4/22/2023","updated_at":"12/23/2022"},
{"id":17,"first_name":"Alexio","last_name":"Mowday","email":"amowdayg@ow.ly","password":"nW1)*u\\h{u7","region":"Texas","age":61,"cin":20319140,"vote":False,"is_banned":True,"created_at":"1/27/2023","updated_at":"2/17/2023"},
{"id":18,"first_name":"Darin","last_name":"Dyball","email":"ddyballh@go.com","password":"iN2&tIXOBs","region":"North Carolina","age":75,"cin":96164294,"vote":False,"is_banned":True,"created_at":"9/29/2023","updated_at":"7/19/2023"},
{"id":19,"first_name":"Melodie","last_name":"Courtes","email":"mcourtesi@harvard.edu","password":"oT2}hbtKNg5#|","region":"Connecticut","age":18,"cin":79169545,"vote":False,"is_banned":False,"created_at":"10/23/2023","updated_at":"8/30/2023"},
{"id":20,"first_name":"Gayel","last_name":"Paslow","email":"gpaslowj@webs.com","password":"aB9}F`J?V!S&5eI9","region":"Ohio","age":75,"cin":85017416,"vote":True,"is_banned":False,"created_at":"1/29/2023","updated_at":"2/11/2023"},
{"id":21,"first_name":"Emma","last_name":"Blades","email":"ebladesk@artisteer.com","password":"iO5#gsmb0Z","region":"Texas","age":41,"cin":57839455,"vote":True,"is_banned":True,"created_at":"9/19/2023","updated_at":"4/15/2023"},
{"id":22,"first_name":"Kylie","last_name":"Spancock","email":"kspancockl@yale.edu","password":"dT2<\\iJ}3)dp_9u","region":"Florida","age":78,"cin":54993439,"vote":True,"is_banned":False,"created_at":"10/29/2023","updated_at":"5/19/2023"},
{"id":23,"first_name":"Justen","last_name":"Rangle","email":"jranglem@scribd.com","password":"zG6(GYb#iI~","region":"Oregon","age":52,"cin":68948463,"vote":False,"is_banned":False,"created_at":"11/15/2023","updated_at":"4/3/2023"},
{"id":24,"first_name":"Kile","last_name":"Brodley","email":"kbrodleyn@list-manage.com","password":"uR0*Ac0_uh\"$)rO","region":"District of Columbia","age":32,"cin":21054550,"vote":True,"is_banned":True,"created_at":"4/22/2023","updated_at":"9/16/2023"},
{"id":25,"first_name":"Zacherie","last_name":"Favelle","email":"zfavelleo@disqus.com","password":"wN0+c#u69XJ$|","region":"California","age":25,"cin":42856465,"vote":True,"is_banned":False,"created_at":"10/13/2023","updated_at":"2/10/2023"},
{"id":26,"first_name":"Agretha","last_name":"Ciani","email":"acianip@amazon.co.uk","password":"kU7)xun9IQ","region":"Delaware","age":36,"cin":34765886,"vote":False,"is_banned":False,"created_at":"2/22/2023","updated_at":"6/6/2023"},
{"id":27,"first_name":"Dot","last_name":"Hindes","email":"dhindesq@technorati.com","password":"cV1|Ojf>adbE","region":"California","age":28,"cin":17273690,"vote":True,"is_banned":False,"created_at":"2/23/2023","updated_at":"1/26/2023"},
{"id":28,"first_name":"Carina","last_name":"Kacheller","email":"ckachellerr@mayoclinic.com","password":"lE6+jdny1dm","region":"Illinois","age":43,"cin":11934460,"vote":True,"is_banned":True,"created_at":"7/30/2023","updated_at":"11/9/2023"},
{"id":29,"first_name":"Coleman","last_name":"Krahl","email":"ckrahls@blinklist.com","password":"pP0}s`y?K","region":"Nevada","age":49,"cin":72447938,"vote":False,"is_banned":False,"created_at":"1/28/2023","updated_at":"6/5/2023"},
{"id":30,"first_name":"Brody","last_name":"Selcraig","email":"bselcraigt@xing.com","password":"aP9?hC5_p\"h9","region":"Virginia","age":53,"cin":46307395,"vote":False,"is_banned":True,"created_at":"5/4/2023","updated_at":"7/19/2023"},
{"id":31,"first_name":"Tony","last_name":"Koppen","email":"tkoppenu@clickbank.net","password":"xN7\"h!Hbh2@v","region":"Iowa","age":80,"cin":23072204,"vote":False,"is_banned":True,"created_at":"8/23/2023","updated_at":"5/26/2023"},
{"id":32,"first_name":"Glynis","last_name":"Schroter","email":"gschroterv@delicious.com","password":"gK5.\\67Mh\\$OImb","region":"Nevada","age":22,"cin":85564299,"vote":True,"is_banned":False,"created_at":"10/22/2023","updated_at":"2/13/2023"},
{"id":33,"first_name":"Heloise","last_name":"Jorioz","email":"hjoriozw@sbwire.com","password":"lU4$9kW(bG.k*!","region":"Texas","age":42,"cin":10017572,"vote":True,"is_banned":True,"created_at":"9/15/2023","updated_at":"12/15/2022"},
{"id":34,"first_name":"Joete","last_name":"Kondratovich","email":"jkondratovichx@msu.edu","password":"vW6{8=oi'd","region":"Arizona","age":46,"cin":89581044,"vote":True,"is_banned":False,"created_at":"4/29/2023","updated_at":"9/11/2023"},
{"id":35,"first_name":"Matty","last_name":"Broxap","email":"mbroxapy@deliciousdays.com","password":"sX9/5KH={","region":"North Carolina","age":28,"cin":53912554,"vote":False,"is_banned":True,"created_at":"4/30/2023","updated_at":"7/17/2023"},
{"id":36,"first_name":"Timi","last_name":"Lamonby","email":"tlamonbyz@stanford.edu","password":"dO5\\A)7*P","region":"California","age":25,"cin":22280574,"vote":True,"is_banned":True,"created_at":"8/14/2023","updated_at":"11/3/2023"},
{"id":37,"first_name":"Merissa","last_name":"Ockwell","email":"mockwell10@naver.com","password":"eS3\\\\a`}w0+f\"=N6","region":"Texas","age":73,"cin":14979117,"vote":True,"is_banned":True,"created_at":"3/4/2023","updated_at":"11/11/2023"},
{"id":38,"first_name":"Marinna","last_name":"Woodington","email":"mwoodington11@addthis.com","password":"xF5`}*)B\"rI4Ux","region":"Indiana","age":25,"cin":88180047,"vote":True,"is_banned":False,"created_at":"11/3/2023","updated_at":"3/12/2023"},
{"id":39,"first_name":"Bax","last_name":"Membry","email":"bmembry12@ucla.edu","password":"jO4,0gx\"n|z","region":"California","age":66,"cin":45635182,"vote":True,"is_banned":False,"created_at":"12/21/2022","updated_at":"2/25/2023"},
{"id":40,"first_name":"Maia","last_name":"Isakovic","email":"misakovic13@businessinsider.com","password":"sU0|Q,VK","region":"Maryland","age":47,"cin":82428099,"vote":False,"is_banned":True,"created_at":"6/15/2023","updated_at":"5/24/2023"},
{"id":41,"first_name":"Marwin","last_name":"Preddy","email":"mpreddy14@tamu.edu","password":"rM1!X}Em","region":"North Carolina","age":56,"cin":49975780,"vote":True,"is_banned":False,"created_at":"7/16/2023","updated_at":"1/18/2023"},
{"id":42,"first_name":"Pincas","last_name":"Meadway","email":"pmeadway15@infoseek.co.jp","password":"bJ8\\#X{(XXlH\\}Y3","region":"South Carolina","age":23,"cin":55825761,"vote":False,"is_banned":False,"created_at":"1/11/2023","updated_at":"3/16/2023"},
{"id":43,"first_name":"Nance","last_name":"Danneil","email":"ndanneil16@cpanel.net","password":"tY7+>r{>2T","region":"Texas","age":23,"cin":79474839,"vote":False,"is_banned":False,"created_at":"11/9/2023","updated_at":"7/13/2023"},
{"id":44,"first_name":"Abran","last_name":"D'Alwis","email":"adalwis17@microsoft.com","password":"sZ1$tj\"~yFN>!=m","region":"North Carolina","age":73,"cin":56524276,"vote":False,"is_banned":False,"created_at":"4/10/2023","updated_at":"4/20/2023"},
{"id":45,"first_name":"Vern","last_name":"Enoch","email":"venoch18@chicagotribune.com","password":"eH5#f+3L#Br'.Nm@","region":"Texas","age":33,"cin":64387127,"vote":True,"is_banned":True,"created_at":"8/22/2023","updated_at":"11/29/2023"},
{"id":46,"first_name":"Matthew","last_name":"Gribbins","email":"mgribbins19@cbc.ca","password":"xH7(cpMvw6R~K","region":"Pennsylvania","age":55,"cin":22753822,"vote":True,"is_banned":False,"created_at":"9/7/2023","updated_at":"3/10/2023"},
{"id":47,"first_name":"Lazare","last_name":"Herculson","email":"lherculson1a@irs.gov","password":"yO1_*xhSggz7P","region":"Florida","age":47,"cin":95679675,"vote":True,"is_banned":True,"created_at":"2/5/2023","updated_at":"5/12/2023"},
{"id":48,"first_name":"Melli","last_name":"Hallen","email":"mhallen1b@ehow.com","password":"fG8\"YTteO","region":"Pennsylvania","age":49,"cin":31710285,"vote":True,"is_banned":True,"created_at":"2/9/2023","updated_at":"8/28/2023"},
{"id":49,"first_name":"Brandy","last_name":"Achromov","email":"bachromov1c@hubpages.com","password":"lJ3+6X5Q!(qOk","region":"Minnesota","age":19,"cin":48469551,"vote":True,"is_banned":False,"created_at":"2/1/2023","updated_at":"10/6/2023"},
{"id":50,"first_name":"Hoyt","last_name":"Sugge","email":"hsugge1d@washingtonpost.com","password":"jD4(Z@0y`lNJNu","region":"Virginia","age":42,"cin":35849385,"vote":False,"is_banned":True,"created_at":"12/22/2022","updated_at":"3/24/2023"},
{"id":51,"first_name":"Paxon","last_name":"Tripp","email":"ptripp1e@baidu.com","password":"uB0{/&4%Lq","region":"Washington","age":37,"cin":59951381,"vote":False,"is_banned":True,"created_at":"12/18/2022","updated_at":"3/27/2023"},
{"id":52,"first_name":"Corny","last_name":"Topaz","email":"ctopaz1f@house.gov","password":"yS9!&sm2W9Pn","region":"Florida","age":66,"cin":67978828,"vote":False,"is_banned":True,"created_at":"10/1/2023","updated_at":"8/8/2023"},
{"id":53,"first_name":"Georgine","last_name":"Prescote","email":"gprescote1g@gizmodo.com","password":"tF1|zAA>b1QoQN","region":"New York","age":37,"cin":42557543,"vote":False,"is_banned":False,"created_at":"6/1/2023","updated_at":"5/22/2023"},
{"id":54,"first_name":"Ranique","last_name":"Giacubo","email":"rgiacubo1h@europa.eu","password":"qI5+Hn8p\"'1M9EMt","region":"South Dakota","age":53,"cin":24984331,"vote":True,"is_banned":True,"created_at":"9/2/2023","updated_at":"4/7/2023"},
{"id":55,"first_name":"Rosemaria","last_name":"Focke","email":"rfocke1i@thetimes.co.uk","password":"mY1#uaH<","region":"New York","age":31,"cin":36808273,"vote":False,"is_banned":False,"created_at":"1/14/2023","updated_at":"1/19/2023"},
{"id":56,"first_name":"Ellissa","last_name":"Grafton","email":"egrafton1j@youku.com","password":"yG1<0'Md","region":"Missouri","age":77,"cin":95480328,"vote":False,"is_banned":True,"created_at":"2/5/2023","updated_at":"12/24/2022"},
{"id":57,"first_name":"Arlan","last_name":"Plewman","email":"aplewman1k@redcross.org","password":"oQ6_,=SdGOxy","region":"Oregon","age":53,"cin":35439184,"vote":False,"is_banned":False,"created_at":"1/30/2023","updated_at":"2/21/2023"},
{"id":58,"first_name":"Allyn","last_name":"Francklin","email":"afrancklin1l@google.pl","password":"kF5,,j6H(i&R{","region":"District of Columbia","age":58,"cin":39164139,"vote":True,"is_banned":True,"created_at":"3/29/2023","updated_at":"12/12/2022"},
{"id":59,"first_name":"Dewie","last_name":"Dessant","email":"ddessant1m@nih.gov","password":"xR3&yN{5eD13,","region":"Oklahoma","age":21,"cin":24263348,"vote":True,"is_banned":True,"created_at":"12/17/2022","updated_at":"6/28/2023"},
{"id":60,"first_name":"Elbertina","last_name":"Cosely","email":"ecosely1n@adobe.com","password":"qJ8*A.Q(11C*#t{","region":"Florida","age":52,"cin":23983236,"vote":True,"is_banned":False,"created_at":"4/10/2023","updated_at":"8/28/2023"},
{"id":61,"first_name":"Burton","last_name":"Bawme","email":"bbawme1o@webmd.com","password":"vH9?4$&{UmQWa&","region":"California","age":25,"cin":42643761,"vote":True,"is_banned":True,"created_at":"1/30/2023","updated_at":"8/29/2023"},
{"id":62,"first_name":"Noellyn","last_name":"Slade","email":"nslade1p@gravatar.com","password":"mK2%_UoO`","region":"Montana","age":61,"cin":59088443,"vote":False,"is_banned":False,"created_at":"8/8/2023","updated_at":"1/11/2023"},
{"id":63,"first_name":"Sarita","last_name":"Goldbourn","email":"sgoldbourn1q@delicious.com","password":"nR6#3L?rEmjoN9zc","region":"Texas","age":50,"cin":70040638,"vote":False,"is_banned":True,"created_at":"8/1/2023","updated_at":"4/17/2023"},
{"id":64,"first_name":"Benny","last_name":"Titmuss","email":"btitmuss1r@clickbank.net","password":"kO8_F,@H%&M","region":"Missouri","age":71,"cin":46081544,"vote":False,"is_banned":True,"created_at":"4/23/2023","updated_at":"7/4/2023"},
{"id":65,"first_name":"Bertina","last_name":"Tobin","email":"btobin1s@blog.com","password":"tY8\\&1m2C<%a","region":"North Carolina","age":68,"cin":59512046,"vote":True,"is_banned":True,"created_at":"9/18/2023","updated_at":"8/3/2023"},
{"id":66,"first_name":"Carlita","last_name":"Rubinsztein","email":"crubinsztein1t@wikispaces.com","password":"oO9?Mzn?sEin!8C","region":"New York","age":20,"cin":80065611,"vote":True,"is_banned":True,"created_at":"7/31/2023","updated_at":"12/15/2022"},
{"id":67,"first_name":"Denise","last_name":"MacNish","email":"dmacnish1u@chicagotribune.com","password":"xU3&kXKhM1K","region":"Florida","age":58,"cin":50207685,"vote":False,"is_banned":True,"created_at":"3/24/2023","updated_at":"12/20/2022"},
{"id":68,"first_name":"Nicholle","last_name":"Hadingham","email":"nhadingham1v@nationalgeographic.com","password":"kG9%\"vWc","region":"Florida","age":61,"cin":66007688,"vote":False,"is_banned":False,"created_at":"9/4/2023","updated_at":"3/28/2023"},
{"id":69,"first_name":"Kirsteni","last_name":"Wanless","email":"kwanless1w@marriott.com","password":"iF4\\YDx/Hv59Q+!C","region":"Texas","age":25,"cin":29615076,"vote":False,"is_banned":True,"created_at":"1/24/2023","updated_at":"12/8/2023"},
{"id":70,"first_name":"Godart","last_name":"Boater","email":"gboater1x@ucoz.ru","password":"iB3~i6(=(4PB","region":"District of Columbia","age":60,"cin":34784785,"vote":False,"is_banned":True,"created_at":"10/12/2023","updated_at":"11/3/2023"},
{"id":71,"first_name":"Kristien","last_name":"Lawther","email":"klawther1y@quantcast.com","password":"qB9`un5C+{{'C","region":"Washington","age":45,"cin":27333502,"vote":True,"is_banned":False,"created_at":"10/13/2023","updated_at":"11/4/2023"},
{"id":72,"first_name":"Valentine","last_name":"Pickless","email":"vpickless1z@psu.edu","password":"zU6,0ibE\\`E\"2Kd","region":"Texas","age":63,"cin":72876919,"vote":True,"is_banned":True,"created_at":"10/31/2023","updated_at":"8/21/2023"},
{"id":73,"first_name":"Nisse","last_name":"Antal","email":"nantal20@reddit.com","password":"kA7!RiX4+","region":"New York","age":54,"cin":78417865,"vote":True,"is_banned":True,"created_at":"6/7/2023","updated_at":"3/30/2023"},
{"id":74,"first_name":"Gayler","last_name":"Baxster","email":"gbaxster21@noaa.gov","password":"rK6(b@4yF4rn=","region":"New Jersey","age":44,"cin":13470698,"vote":True,"is_banned":False,"created_at":"12/9/2022","updated_at":"3/26/2023"},
{"id":75,"first_name":"Dill","last_name":"Jerzykiewicz","email":"djerzykiewicz22@cyberchimps.com","password":"yA2$<9tDb6Q>X7Xq","region":"Texas","age":71,"cin":46000705,"vote":True,"is_banned":True,"created_at":"10/26/2023","updated_at":"1/6/2023"},
{"id":76,"first_name":"Reinaldo","last_name":"Warstall","email":"rwarstall23@independent.co.uk","password":"eG5'7\\W.G3MdY2dl","region":"Utah","age":41,"cin":10589218,"vote":False,"is_banned":False,"created_at":"4/11/2023","updated_at":"4/20/2023"},
{"id":77,"first_name":"Mei","last_name":"Pietruszewicz","email":"mpietruszewicz24@bizjournals.com","password":"iT5{R8_4G","region":"District of Columbia","age":18,"cin":99035985,"vote":False,"is_banned":False,"created_at":"5/6/2023","updated_at":"10/18/2023"},
{"id":78,"first_name":"Ardine","last_name":"Hallows","email":"ahallows25@ameblo.jp","password":"aE1(l'gmkT@","region":"Arizona","age":77,"cin":28118126,"vote":True,"is_banned":False,"created_at":"11/2/2023","updated_at":"2/23/2023"},
{"id":79,"first_name":"Damon","last_name":"Hennemann","email":"dhennemann26@economist.com","password":"nW8&_O3ZQX0NzC","region":"Missouri","age":44,"cin":20218590,"vote":False,"is_banned":True,"created_at":"6/24/2023","updated_at":"1/24/2023"},
{"id":80,"first_name":"Lynett","last_name":"Doree","email":"ldoree27@ted.com","password":"nR1'Li0vcdm59j","region":"Maryland","age":52,"cin":61572346,"vote":True,"is_banned":False,"created_at":"9/10/2023","updated_at":"12/18/2022"},
{"id":81,"first_name":"Janel","last_name":"MacMichael","email":"jmacmichael28@tmall.com","password":"rE1+s!RbD=\"mIrQ?","region":"Connecticut","age":45,"cin":76749590,"vote":True,"is_banned":True,"created_at":"9/2/2023","updated_at":"1/1/2023"},
{"id":82,"first_name":"Shurlocke","last_name":"Dongles","email":"sdongles29@gov.uk","password":"yX9%<>*jTw","region":"Texas","age":62,"cin":57845704,"vote":True,"is_banned":True,"created_at":"12/4/2023","updated_at":"1/14/2023"},
{"id":83,"first_name":"Lottie","last_name":"Allabarton","email":"lallabarton2a@smh.com.au","password":"aU4<vFN2\\b","region":"Texas","age":34,"cin":57731826,"vote":False,"is_banned":True,"created_at":"1/31/2023","updated_at":"10/15/2023"},
{"id":84,"first_name":"Trula","last_name":"Kamenar","email":"tkamenar2b@shinystat.com","password":"zS3|#!7$!M3=,","region":"New York","age":39,"cin":18932786,"vote":True,"is_banned":False,"created_at":"7/14/2023","updated_at":"2/27/2023"},
{"id":85,"first_name":"Lulita","last_name":"Postance","email":"lpostance2c@aol.com","password":"pD1(sro*","region":"New York","age":22,"cin":15554539,"vote":False,"is_banned":True,"created_at":"9/7/2023","updated_at":"10/9/2023"},
{"id":86,"first_name":"Bibbie","last_name":"Pounds","email":"bpounds2d@sciencedaily.com","password":"rD3(y<|70v","region":"Delaware","age":68,"cin":95224445,"vote":True,"is_banned":True,"created_at":"9/26/2023","updated_at":"4/21/2023"},
{"id":87,"first_name":"Herold","last_name":"Deery","email":"hdeery2e@wikispaces.com","password":"sB8?C}##e","region":"California","age":34,"cin":65872538,"vote":False,"is_banned":False,"created_at":"1/10/2023","updated_at":"2/10/2023"},
{"id":88,"first_name":"Linda","last_name":"Olivetta","email":"lolivetta2f@wordpress.org","password":"rS9/ArFn7","region":"Florida","age":39,"cin":60535755,"vote":False,"is_banned":True,"created_at":"12/10/2022","updated_at":"7/19/2023"},
{"id":89,"first_name":"Miof mela","last_name":"Proffitt","email":"mproffitt2g@boston.com","password":"kI9?mM=hZ","region":"Delaware","age":59,"cin":80991204,"vote":False,"is_banned":False,"created_at":"9/9/2023","updated_at":"10/21/2023"},
{"id":90,"first_name":"Gilli","last_name":"Ashurst","email":"gashurst2h@sohu.com","password":"yS9.RD.h)AEPZuS0","region":"Kentucky","age":48,"cin":80125366,"vote":True,"is_banned":True,"created_at":"7/3/2023","updated_at":"7/29/2023"},
{"id":91,"first_name":"Nollie","last_name":"Balsom","email":"nbalsom2i@ycombinator.com","password":"hM9?q'ED3=)BL","region":"Texas","age":28,"cin":98330733,"vote":True,"is_banned":False,"created_at":"9/13/2023","updated_at":"2/15/2023"},
{"id":92,"first_name":"Libbi","last_name":"Laborde","email":"llaborde2j@bizjournals.com","password":"kA1,Zkl0ot#'VnT","region":"Pennsylvania","age":37,"cin":88761099,"vote":False,"is_banned":True,"created_at":"11/4/2023","updated_at":"9/16/2023"},
{"id":93,"first_name":"Paolina","last_name":"Cobbledick","email":"pcobbledick2k@timesonline.co.uk","password":"jP0~vRq@KO,5$","region":"Texas","age":38,"cin":86839505,"vote":True,"is_banned":False,"created_at":"7/4/2023","updated_at":"11/22/2023"},
{"id":94,"first_name":"Sigismondo","last_name":"Halloway","email":"shalloway2l@ifeng.com","password":"sQ3`eOKQ_Ekcp+A5","region":"Virginia","age":75,"cin":75621033,"vote":False,"is_banned":True,"created_at":"12/26/2022","updated_at":"8/18/2023"},
{"id":95,"first_name":"Valentin","last_name":"Petrenko","email":"vpetrenko2m@homestead.com","password":"eU3$r7L6gl","region":"South Carolina","age":55,"cin":98443576,"vote":True,"is_banned":False,"created_at":"7/6/2023","updated_at":"10/7/2023"},
{"id":96,"first_name":"Davide","last_name":"Smithson","email":"dsmithson2n@quantcast.com","password":"bK1'Ad|dOHn7/QwQ","region":"California","age":75,"cin":39717934,"vote":False,"is_banned":True,"created_at":"9/4/2023","updated_at":"10/9/2023"},
{"id":97,"first_name":"Crissy","last_name":"Middleditch","email":"cmiddleditch2o@weather.com","password":"cV3/z!{%t4Ysz","region":"California","age":64,"cin":70295179,"vote":True,"is_banned":True,"created_at":"3/21/2023","updated_at":"5/13/2023"},
{"id":98,"first_name":"Danyelle","last_name":"Fleming","email":"dfleming2p@altervista.org","password":"zP9\"6X/v6)+tD(%v","region":"South Carolina","age":66,"cin":19615380,"vote":True,"is_banned":True,"created_at":"3/16/2023","updated_at":"8/15/2023"},
{"id":99,"first_name":"Lorette","last_name":"Speakman","email":"lspeakman2q@free.fr","password":"iI4//i#$u~&0L","region":"Wyoming","age":67,"cin":62655416,"vote":True,"is_banned":True,"created_at":"8/8/2023","updated_at":"4/27/2023"},
{"id":100,"first_name":"Erna","last_name":"Goschalk","email":"egoschalk2r@51.la","password":"fC7_rUME2YBkMo=","region":"Wisconsin","age":29,"cin":82727752,"vote":False,"is_banned":False,"created_at":"6/29/2023","updated_at":"5/29/2023"},
{"id":101,"first_name":"Tony","last_name":"Galea","email":"tgalea2s@usatoday.com","password":"mR8*KgGp","region":"California","age":26,"cin":63963224,"vote":False,"is_banned":False,"created_at":"5/15/2023","updated_at":"9/4/2023"},
{"id":102,"first_name":"Dur","last_name":"Leaming","email":"dleaming2t@ucsd.edu","password":"uI8%t8cD&UGjQP","region":"Arizona","age":56,"cin":64214839,"vote":True,"is_banned":True,"created_at":"11/18/2023","updated_at":"8/9/2023"},
{"id":103,"first_name":"Meredithe","last_name":"Wynes","email":"mwynes2u@squarespace.com","password":"bF7#)o4zS\"dN7FT","region":"South Carolina","age":27,"cin":23986207,"vote":False,"is_banned":False,"created_at":"2/15/2023","updated_at":"1/10/2023"},
]
    for one in data:
        Voter.create(one)
    return 'data is stored !'


# <<<<<<< HEAD

# -------------------------------------------
if __name__=="__main__":
    app.run(debug=True,port = 5001)
# =======

