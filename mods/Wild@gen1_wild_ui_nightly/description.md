# Gen1WildUI Nightly

**The visual half of the Gen1Wild suite, as one mod** — and this is its test
build. It installs under its own id and **conflicts with the stable
Gen1WildUI on purpose**: run one or the other, never both.

## UI THEME

`START > OPTION > UI THEME` cycles **`LIGHT`**, **`DARK`** and
**`COLORFUL*`**. `LIGHT` is the default and is exactly what the stable bundle
looks like.

**`DARK`** is the literal thing: every page this suite draws is black and
white, so dark mode swaps the two. Paper black, ink white, the shades between
them exchanged. It reaches the Pokédex, the box, the party menu, the bag, the
item screens, the mod manager and the suite's own settings.

The overworld, the battles and the title screen are not touched, and that is
not a gap — they are pictures rather than pages, and a theme that inverted a
map would be inverting the game rather than the interface.

**`COLORFUL`** tints each page by what the screen is: the Pokédex red because
a Pokédex is a red device, the box blue, the party the green of a full HP bar,
the bag leather, the mart gold. Nothing shouts — every tint holds the same
lightness the black-and-white page had, so a word is never harder to read than
it was. On the suite's own settings screen the cards are coloured by what they
open, so you pick one by colour before you have read it.

The asterisk means what it says: the battle command grid's four buttons
(`FIGHT` / `PKMN` / `ITEM` / `RUN`) are the clearest buttons in the suite and
are not coloured yet.

## Also new in 0.2.0

**No more white bar above a wide arena.** A battle asks the renderer for a
white surround, which is right when the field is white paper and wrong when it
is a picture: the surround stops disappearing and becomes a bright frame around
the art — and a wide battle is 304x144, so the bars above and below it are the
biggest thing on the screen. The backdrop's own edge is stretched into them now,
so the picture runs off the screen instead of stopping at a rectangle.
`EDGE TO EDGE` turns it off.

**`BLACK OUTRO` holds at the cut.** It used to be at full black for exactly one
frame — the frame that pops the fade, runs the engine's own ending and pushes
it back — so that was the only covered moment the whole outro had, and the
autosave found it. It now holds for the ten frames the engine's own return
holds.

## Everything else

Unchanged from the stable bundle: battle backdrops, the battle intro, the
battle menus as a 2x2 grid, a Pokédex with a Pokémon beside every entry, Bill's
PC as an actual box, the party menu in species colours, a bag with seven
pockets, an icon and a description for every item, the lift panel, menu layout
and the mod manager. Every feature still switches on and off by itself.
