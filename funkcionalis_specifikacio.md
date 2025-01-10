# Funkcionális specifikáció
## 1. Jelenlegi helyzet leírása
Jelenleg nincs olyan egyszerű oktatási játék, amely magyar és angol szavak párosításával támogatná a nyelvtanulást különböző szinteken. A meglévő eszközök többsége túl komplex vagy nem szórakoztató, így hiányzik egy könnyen kezelhető megoldás, amely motiválja a tanulókat.
## 2. Vágyállomrendszer leírása
Egy olyan játékos alkalmazás létrehozása, amely lehetővé teszi a magyar-angol szópárok gyakorlását különböző nehézségi szinteken. Az alkalmazás gyorsan és véletlenszerűen generál szópárokat, amelyeket a felhasználó összeilleszthet, majd a program az eredményeket kiértékeli és visszajelzést ad.
## 3. Üzleti folyamatok modellje
A felhasználó kiválaszt egy nehézségi szintet ("könnyű", "közepes" vagy "nehéz").
A program generál 7 véletlenszerű magyar-angol szópárt. A felhasználó az angol szavakat párosítja a magyar megfelelőikkel.
Az alkalmazás kiértékeli a válaszokat és megjeleníti az eredményeket.
## 4. Igényelt üzleti folyamatok modellje
Szópárok véletlenszerű generálása: A program a választott nehézségi szint alapján véletlenszerűen kiválasztja a szópárokat. Párosítási játék: A felhasználó lenyíló menüből választja ki az angol szavakat, amelyeket a magyar megfelelőkkel kell párosítania. Eredmények visszajelzése: A játék végén az alkalmazás megjeleníti a helyes és helytelen válaszok számát, valamint motivációs üzenetet ad.
## 5. Követelménylista
Id	Modul	Név	Leírás
K1	Nehézségi szint	Szintválasztás	A felhasználó kiválasztja a nehézségi szintet (könnyű, közepes, nehéz).
K2	Generálás	Szópárok generálása	Az alkalmazás véletlenszerűen kiválaszt 7 szópárt a választott szint alapján.
K3	Párosítás	Feladat végrehajtása	A felhasználó a magyar szavakat a megfelelő angol szavakkal párosítja.
K4	Kiértékelés	Eredmények megjelenítése	Az alkalmazás kiértékeli a párosításokat, és megjeleníti az eredményeket.
K5	Visszajelzés	Motivációs üzenet	Az alkalmazás visszajelzést ad a teljesítmény alapján (pl. dicséret, bátorítás).

## 6. Használati esetek
Felhasználó:
Kiválasztja a nehézségi szintet.
Részt vesz a párosítási játékban.
Megkapja az eredményeket és motivációs üzenetet.
Rendszer:
Generálja a megfelelő szópárokat a választott szint alapján.
Véletlenszerűen megkeveri az angol válaszlehetőségeket.
Kiértékeli a felhasználó válaszait.