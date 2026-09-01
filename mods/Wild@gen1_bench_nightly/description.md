# Test Bench

**One screen with everything the nightly channel is changing on it, one press
from START.** It ships on no release.

`START > BENCH`:

- **`UI THEME`** — light, dark, colourful
- **`PLAYER`** — the character's colour, which is live now, so you can watch it
  change under your feet
- **`COLORS`** — the display mode, because the title screen's bands differ
  between them
- **`BATTLE LAYOUT`** — OG or WIDE
- **`BACKDROPS`**, **`EDGE TO EDGE`**, **`FIELD TEST`** — the arena rows
- **`MAP`** — what the backdrop is being picked from
- **`START A BATTLE`** — pick an opponent and a level and press A
- **`ASK FOR A SAVE`** — and a reading of whether it has landed
- **`VOXEL`** — which voxel mod is installed, if any, and whether that one
  moves the battle HUDs onto its own world canvas. `SNAP` means the XP bar and
  the caught marker should be following them there; `FRAME` means they should
  not, which is what two of the four forks want and is not a fault

## Why it is a mod of its own

Because that is what makes gutting it free. Taking the testing weight out of a
release is not a refactor, an option to switch off, or a flag somebody has to
remember: it is **not pinning this mod**. The stable cart pins four mods and
this is not one of them.

Every row reaches its mod through what that mod publishes, and a row whose mod
is missing reads `--` and does nothing — a bench that silently dropped a row
could not tell you the mod was gone.

## What it deliberately will not do

**Write a save now.** `ASK FOR A SAVE` calls the same request every checkpoint
calls, so a bench-asked save takes the same windows and the same refusals as
any other. A button that forced a write would be testing a code path the game
does not have.
