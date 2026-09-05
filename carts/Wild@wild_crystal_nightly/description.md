# Wild Crystal Nightly

**This is the Gen 2 test cart, and it is where Gen 2 bugs get found.** It is
the suite running on Crystal instead of Red — both halves and the test bench —
with the changes that have not been cut into a release yet.

It is also a preview: what settles here is what the stable **Wild Crystal**
cart will be. Playing this is how that gets decided.

Your other carts are untouched. Every mod in this one installs under an id of
its own and **conflicts with its stable twin on purpose**: run one or the
other, never both. Nothing here can reach your Wild Green saves, your settings
or your cartridge — and this cart has save slots of its own, because a cart is
its own game.

The cartridge is **dark blue**, against Wild Green Nightly's dark purple, so
you can tell at a glance which one you are opening. *(The label art is not
drawn yet, so it is a bare cartridge in that colour for now.)*

## What is in it

Three mods, all three of them nightly:

- **Gen1WildQOL Nightly** — the quality-of-life half: sprinting, autosave,
  auto continue, followers, EXP share, menu layout, the mod manager. Nearly
  all of it runs on Crystal unchanged, because it was written against hooks
  rather than modules.
- **Gen1WildUI Nightly** — the visual half. On Crystal that is `BACKDROPS`,
  `POKEDEX`, `BAG`, `PARTY MENU`, `MENU LAYOUT`, `MOD MANAGER`,
  `BATTLE MENUS` and `UI THEME`.
- **Test Bench** — a `BENCH` row on the START menu with everything this
  channel is changing on one screen, and a battle on demand. **It ships on no
  release**, which is the whole reason this cart exists: bug testing wants the
  bench pinned, and a stable cart must not carry it.

What it does **not** pin is `Wild Green Nightly` — that mod is Red's player,
Red's names and Red's title screen, and its manifest says `"games": ["red"]`.
A Crystal cart has no use for it.

## What is worth testing

The Gen 2 arms are the newest code in the channel and the least played:

- **Autosave and auto continue.** Both were completely inert on Gen 2 until
  0.32.25 — no error, no warning, the rows reading ON and nothing happening.
  Both work now, so both want a real playthrough rather than a look.
- **`UI THEME > DARK`.** It reaches the START menu, the lift, the dialogue
  boxes and the YES/NO box as of 0.32.26. A white box on a dark page is a bug;
  please say which box.
- **The party menu**, which as of 0.32.28 is drawn in the suite's own frame
  with `CANCEL` in the header rather than after the last row.
- **`BACKDROPS` in Johto.** All twenty scenes are reached on a Gen 2 boot and
  six of them were re-dealt to Johto's bosses. A backdrop that does not suit
  where you are standing is worth reporting.
- **The battle screen over a backdrop**, which is where nearly everything has
  gone wrong so far. As of 0.32.31 the HUD has nothing behind it — no white
  cells, no white slab around the HP and exp bars, no plate — and the pics
  have paper in their own shape rather than a rectangle, so a trainer is not
  see-through and does not sit on a sticker. Anything on that screen with a
  box around it that should not have one is worth a screenshot.
- **`BATTLE MENUS` on Crystal**, new in 0.32.31 and the first thing this mod
  has ever drawn on a Gen 2 battle: the four commands in four boxes instead of
  four words in one. The move list and the bug contest's menu are deliberately
  still the cart's.

It is sealed like the other carts, so it can still go online — with other
people running this same nightly.

[channel]: https://github.com/wild1walker/Gen1NightlyMods
