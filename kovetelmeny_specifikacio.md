# Követelmény specifikáció
## 1. Áttekintés
A nyelvtanulók számára egyre fontosabb, hogy a tanulási folyamatot interaktív, játékos módon végezzék. Az általunk fejlesztett alkalmazás célja, hogy segítse a magyar-angol szavak párosítását különböző nehézségi szinteken keresztül. Az alkalmazás lehetőséget kínál a felhasználóknak, hogy szórakoztató formában gyakorolják a nyelvet, miközben az eredmények alapján visszajelzést és motivációt kapnak.

## 2. A jelenlegi helyzet leírása
Jelenleg kevés olyan játékos alkalmazás létezik, amely magyar-angol szópárok párosításán alapul, és különböző nehézségi szinteken teszi lehetővé a gyakorlást. A létező megoldások többsége vagy túl komplex, vagy nem ad elegendő visszacsatolást a felhasználók teljesítményéről. Ezen kívül a motivációs elemek is hiányoznak, amelyek segítenék a tanulók fejlődését. 

## 3. Vágyálomrendszer
Az alkalmazás célja egy szórakoztató, de hatékony eszköz létrehozása, amely támogatja a nyelvtanulást az alábbi funkciókkal:
- Könnyen érthető és reszponzív kezelőfelület.
- Különböző nehézségi szintek: "könnyű", "közepes" és "nehéz".
- Véletlenszerűen generált magyar-angol szópárok.
- Az eredmények kiértékelése és motivációs üzenetek a teljesítmény alapján.
- Egy egyszerű, intuitív játékélmény, amely minden korosztály számára élvezetes.

## 4. Jelenlegi üzleti folyamatok modellje
	 4.1. Szópárok Generálása
   	 A felhasználó kiválasztja a kívánt nehézségi szintet.
   	 Az alkalmazás véletlenszerűen kiválaszt 7 magyar-angol szópárt a szintnek megfelelő szókészletből.
	 4.2. Párosítási Feladat
        A felhasználó az angol szavakat a megfelelő magyar szóval párosítja lenyíló menük segítségével.
	 4.3. Eredmények Kiértékelése
   	 Az alkalmazás kiértékeli a helyes és helytelen válaszokat, majd megjeleníti az eredményeket és motivációs üzeneteket.

## 5. Igényelt üzleti folyamatok modellje
 	5.1. Szópárok Generálása
   	 Felelős: Az alkalmazás.
   	 Folyamat: Az alkalmazás a választott nehézségi szint alapján véletlenszerűen generál 7 magyar-angol szópárt, és az angol szavakat 	 megkeveri.
	 5.2. Párosítási Feladat
   	 Felelős: Felhasználók.
   	 Folyamat: A felhasználók lenyíló menükből kiválasztják az angol szavakat, amelyeket a magyar szavakhoz társítanak.
5.3. Eredmények Kiértékelése
   	 Felelős: Az alkalmazás.
   	 Folyamat: Az alkalmazás összeveti a felhasználó válaszait a helyes megoldásokkal, és megjeleníti az eredményeket (helyes és 	 	 helytelen válaszok száma).
	 5.4. Motivációs Üzenetek
   	 Felelős: Az alkalmazás.
   	 Folyamat: Az alkalmazás teljesítményalapú visszacsatolást nyújt, például gratuláló vagy bátorító üzenetekkel.
5.5. Felhasználói Élmény
   	 Felelős: Az alkalmazás.
   	 Folyamat: A felület reszponzív kialakítása biztosítja, hogy a játék élvezetes legyen különböző eszközökön (mobil, tablet, PC).
