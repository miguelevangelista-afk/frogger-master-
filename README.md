A 2D frogger game, created with HTML5 Canvas.


## New: animated characters and rewards

**11 new animated characters** (`images/chars/*.png`, listed in `js/shop.js`): Fluffy Sheep, Cow, Pudding Pup, Shiba, Little Deer,
Purple Frog, Rock Girl, Sister, Shell Dragon, Iron Knight, Red Hood. Each one has a walk cycle in 4 directions, plus breathing/blinking
when standing still. In the shop, hover (or tap) a card to see it walk.

**Getting characters**
- Buy them in the shop with coins (Characters tab), or
- win them from Loot Boxes (bigger boxes and rarer prizes = better chance, guaranteed within 12 boxes) or from the treasure chests on the road.

**Rewards tab** (`js/rewards.js`): 7-day daily streak (day 7 = free character) and 10 missions that pay coins.

**Adding more characters**: cut a sprite sheet into 4 rows (down, left, right, up) of 101x171 frames, save it in `images/chars/`,
add one line to `CHARACTERS` in `js/shop.js`, and add the file to `sw.js`.


## Sound, items, backup and fight effects

- **Sound FX** (`js/sfx.js`): ~20 sounds made with WebAudio (no audio files). Menu > Sound FX turns them on/off. Add a sound = one line in `SOUNDS`.
- **Items** (`js/items.js`): potions, charms and elixirs found as bonus drops in loot boxes, road chests and the High Roller slot. Menu > Items to use them. They never give free coins/tickets/gems, so the economy stays balanced.
- **Backup** (`js/savedata.js`): Menu > Backup / Transfer exports/imports ALL profiles as a `.json` file, keeps an automatic IndexedDB copy (offers to restore if the browser data disappears), asks the browser for persistent storage and reminds you to export every 7 days.
- **Fight effects** (`js/fightfx.js`): pixel-art slashes, crit sparks, guard rings, hit flash/shake and a boss explosion, drawn by code (no copyrighted sprites).

## Game Boy extras

- **Direcional animado** (`js/gba.js` + `css/style.css`): o botao apertado afunda e o oposto levanta (toque, teclado e mouse).
- **A / B na luta** (`js/gba.js`, `bossFight.attack/dodge` em `js/boss.js`): A = Atacar, B = Esquivar.
- **Ann** (`images/chars/ann.png`): novo personagem animado (4 direcoes x 2 quadros), vendido na loja por 170 moedas.
- **Icone do app** trocado em `icons/icon-192.png` e `icons/icon-512.png`.



Atualização de desempenho: boss-art.js não é carregado no início; as imagens dos chefes são buscadas em images/boss/ somente quando a batalha/lista é aberta. O cache do service worker foi atualizado para frogger-v66-gba-polish.
