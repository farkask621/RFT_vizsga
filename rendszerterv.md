# Rendszerterv
## 1. A rendszer célja
A rendszer célja egy modern, felhasználóbarát platform biztosítása, amely lehetővé teszi a hírek gyors és pontos elérését bármilyen eszközről és böngészőről. A hírek típusok szerint csoportosítva érhetők el, biztosítva a könnyű kereshetőséget. Az adminisztrátorok képesek híreket hozzáadni, módosítani és törölni, míg a felhasználók regisztráció és bejelentkezés után kommenteket fűzhetnek a hírekhez. A cél egy dinamikus, reszponzív webalkalmazás létrehozása, amely megfelel a modern webes elvárásoknak.

## 2. Projektterv
A projekt során Scrum keretrendszerben dolgozunk. A Scrum master koordinálja a csapat munkáját, míg a Product Owner biztosítja a felhasználói igények megfelelő érvényesítését. A fejlesztők frontend, backend, és tesztelési feladatokat végeznek. Az ütemterv szerint az első szakaszban elkészülnek a specifikációk és a prototípus, majd következik az alapfunkciók fejlesztése, végül a tesztelés. A projekt három mérföldköve: a tervezési dokumentációk átadása, a prototípus bemutatása, majd a kész rendszer leszállítása.

## 3. Üzleti folyamatok modellje
A rendszer két fő szerepkörrel dolgozik: admin és felhasználó. Az adminok kezelhetik a híreket és a felhasználókat, míg a felhasználók hozzáférhetnek a hírekhez és kommentelhetnek. Az üzleti folyamatok biztosítják a hírek kategóriákba sorolását és azok kezelését.

## 4. Követelmények
A rendszer funkcionális követelményei közé tartozik a regisztráció, bejelentkezés, kommentelés és a hírek CRUD műveletei. Nem funkcionális követelmény az átlátható, könnyen kezelhető felhasználói felület, valamint a reszponzív dizájn. A felület minden modern eszközről és böngészőről elérhető lesz. A rendszer szintén támogatja a különböző szerepkörök jogosultságainak kezelését.

## 5. Funkcionális terv
Az adminisztrátorok képesek hírek létrehozására, módosítására, törlésére, valamint felügyelik a felhasználók tevékenységét. A felhasználók böngészhetik a híreket, megtekinthetik a kategóriákat, és hozzászólhatnak.A főmenü hierarchiája tartalmazza a bejelentkezési opciókat, a kezdőlapot, kategorizált híreket, és a felhasználói adatok kezelését.

## 6. Fizikai környezet
A fejlesztéshez Visual Studio Code-ot használunk a forráskód írásához. A tesztelés során különböző operációs rendszereken (Windows, Linux, macOS) biztosítjuk a program kompatibilitását. A fejlesztés során Python programnyelvet használunk, és a Tkinter könyvtár segítségével valósítjuk meg a grafikus felületet.

## 7. Implementációs terv
A programot Python nyelven készítjük el, amely egy könnyen telepíthető és futtatható nyílt forráskódú környezetet biztosít. Az interfész létrehozásához a Tkinter könyvtárat használjuk. A telepítési lépésekhez biztosítjuk a szükséges könyvtárak (pl. random és tkinter) megfelelő dokumentációját. A forráskód strukturált és magyar nyelvű változóneveket használ az átláthatóság érdekében.

## 8. Tesztterv
A rendszer működésének validálásához számos tesztesetet hozunk létre. Tesztelni fogjuk például a szóösszepárosítás helyességét, a nehézségi szintek működését, valamint az interfész elemek elérhetőségét és funkcionalitását.  A csapattagok teszteredményeit egy központi dokumentumban gyűjtjük össze, amelyet a vezetőség számára is elérhetővé teszünk.