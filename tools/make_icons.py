#!/usr/bin/env python3
"""Draw mods/<Author>@<id>/thumbnail.png: one square icon per nightly mod.

    python3 tools/make_icons.py                     # redraw every icon
    python3 tools/make_icons.py wild_green_nightly  # ... or just the ones named

Every icon is pixel art on a 32x32 grid, written out as thirty-two strings and
scaled 16x to 512x512 with no resampling, so one drawn pixel is a clean 16x16
block.  Nothing is loaded from disk, no font is involved and no library is
imported, so a rebuild on any machine produces byte-identical files -- which is
what lets CI check that the committed PNGs are still what this draws.

The grids are strings on purpose.  This index has two icons and will have a
handful; a drawing DSL would be more code than the pictures, and a grid you can
read down the page is a picture anyone can edit without running anything.

------- what a nightly icon says

Two things, and in this order:

  * it is the nightly one.  Every icon here is in the channel's purple and
    carries the same crescent moon in the same corner, so a card in FIND MODS
    reads as "the night build of that" before it is read at all.  The stable
    index's icons are each their own colour; that is what makes purple mean
    something here.
  * which mod it is.  The device with UI on its screen is the visual bundle,
    the cap is Wild Green.  Both are the shapes the stable index already uses
    for those mods, so somebody who knows the stable cards recognises these.

The cart is not drawn here.  A cart's icon is its cartridge, the cartridge is
drawn in the cart's own repository, and tools/build_index.py fetches that
label on every rebuild -- so the card and the cartridge cannot drift.

A folder with no icon is named on the way out and makes the run exit non-zero,
so an entry cannot quietly go without one.
"""

import json
import pathlib
import struct
import sys
import zlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
MODS = ROOT / "mods"

GRID = 32          # the drawing grid, in pixels
SCALE = 16         # how many image pixels one drawn pixel becomes
SIZE = GRID * SCALE

# The index's own dark card colours, the channel's purple, and the two
# borrowed colours an icon needs to say which mod it is.
BG       = (0x0b, 0x0d, 0x0c)   # the card behind everything
INK      = (0x1a, 0x12, 0x28)   # outline: the purple's own near-black
DARK     = (0x2e, 0x1e, 0x46)
MID      = (0x54, 0x37, 0x7e)   # NIGHTLY_INK, the cartridge shell
LIGHT    = (0x91, 0x5f, 0xda)   # NIGHTLY_MID, the ribbon's shadow in purple
PALE     = (0xc2, 0x9a, 0xd9)
SCREEN   = (0x14, 0x0e, 0x1e)
NIGHT    = (0x1e, 0x14, 0x2e)   # the ground every icon in this index sits on
MOON     = (0xf2, 0xe8, 0xc0)
MOON_D   = (0xb9, 0xa8, 0x76)
GREEN    = (0x65, 0xba, 0x3f)   # OUTFIT, the colour the cart is named after
GREEN_D  = (0x2e, 0x8b, 0x3a)
SKIN     = (0xf0, 0xa3, 0x63)
BILL     = (0xe6, 0xf4, 0xdc)

PALETTE = {
    ".": NIGHT,
    "e": SCREEN,
    "k": INK,
    "d": DARK,
    "p": MID,
    "P": LIGHT,
    "l": PALE,
    "s": SCREEN,
    "m": MOON,
    "n": MOON_D,
    "g": GREEN,
    "G": GREEN_D,
    "f": SKIN,
    "b": BILL,
}

# The crescent, in the top-right of every icon.  Computed rather than drawn, so
# it is provably the same shape on every card and provably symmetrical: an icon
# set whose badge drifts by a pixel between cards is an icon set nobody trusts.
#
# One disc with a second disc taken out of it, offset -- which is what a
# crescent is.
MOON_R = 4.6
MOON_BITE_R = 4.0
MOON_BITE_DX = 4.1
MOON_AT = (20, 1)          # left, top of its 10x10 box
MOON_BOX = 10


def _crescent():
    """The moon as rows of '.', 'n' (its edge) and 'm' (its face)."""
    rows = []
    centre = (MOON_BOX - 1) / 2.0
    for y in range(MOON_BOX):
        line = []
        for x in range(MOON_BOX):
            dx, dy = x - centre, y - centre
            outer = dx * dx + dy * dy
            bx = dx - MOON_BITE_DX
            bite = bx * bx + dy * dy
            if outer > MOON_R * MOON_R or bite <= MOON_BITE_R * MOON_BITE_R:
                line.append(".")
                continue
            rim = (MOON_R - 1.0) * (MOON_R - 1.0)
            inner_rim = (MOON_BITE_R + 0.9) * (MOON_BITE_R + 0.9)
            line.append("n" if (outer > rim or bite <= inner_rim) else "m")
        rows.append("".join(line))
    return tuple(rows)


MOON_ROWS = _crescent()


# ------- the icons

WILD_GREEN_NIGHTLY = (
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "..........kkkkkkkkkkkk..........",
    "........kkGGGGGGGGGGGGkk........",
    ".......kGGGggggggggggGGGk.......",
    "......kGGgggggggggggggggGk......",
    ".....kGGgggggggggggggggggGk.....",
    ".....kGgggggggggggggggggggk.....",
    "....kGgggggggggggggggggggggk....",
    "....kGgggggggggggggggggggggk....",
    "....kGgggggggggggggggggggggk....",
    "....kGGgggggggggggggggggggGk....",
    "...kkkkkkkkkkkkkkkkkkkkkkkkkk...",
    "..kbbbbbbbbbbbbbbbbbbbbbbbbbbk..",
    ".kbbbbbbbbbbbbbbbbbbbbbbbbbbbbk.",
    "..kbbbbbbbbbbbbbbbbbbbbbbbbbbk..",
    "...kkkkkkkkkkkkkkkkkkkkkkkkkk...",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
)

GEN1_WILD_UI_NIGHTLY = (
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "...kkkkkkkkkkkkkkkkkkkkkkkkk....",
    "...kPPPPPPPPPPPPPPPPPPPPPPPk....",
    "...kPpppppppppppppppppppppPk....",
    "...kPpkkkkkkkkkkkkkkkkkkkpPk....",
    "...kPpkeeeeeeeeeeeeeeeeekpPk....",
    "...kPpkeeleeeleeellleeeekpPk....",
    "...kPpkeeleeeleeeeleeeeekpPk....",
    "...kPpkeeleeeleeeeleeeeekpPk....",
    "...kPpkeeleeeleeeeleeeeekpPk....",
    "...kPpkeeellleeeellleeeekpPk....",
    "...kPpkeeeeeeeeeeeeeeeeekpPk....",
    "...kPpkkkkkkkkkkkkkkkkkkkpPk....",
    "...kPpppppppppppppppppppppPk....",
    "...kPpppdddpppppppppppppppPk....",
    "...kPpppdddppppppdddpdddppPk....",
    "...kPpdddddddppppdddpdddppPk....",
    "...kPpppdddppppppdddpdddppPk....",
    "...kPpppdddpppppppppppppppPk....",
    "...kPpppppppppppppppppppppPk....",
    "...kkkkkkkkkkkkkkkkkkkkkkkkk....",
    "................................",
)

# The same device as the UI one, with the other half's letters on it -- which
# is the pairing the stable index already draws for these two, so somebody who
# knows those cards knows these.
GEN1_WILD_QOL_NIGHTLY = (
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "...kkkkkkkkkkkkkkkkkkkkkkkkk....",
    "...kPPPPPPPPPPPPPPPPPPPPPPPk....",
    "...kPpppppppppppppppppppppPk....",
    "...kPpkkkkkkkkkkkkkkkkkkkpPk....",
    "...kPpkeeeeeeeeeeeeeeeeekpPk....",
    "...kPpkeeelleeelleeleeeekpPk....",
    "...kPpkeeleeleleeleleeeekpPk....",
    "...kPpkeeleeleleeleleeeekpPk....",
    "...kPpkeeelleeleeleleeeekpPk....",
    "...kPpkeeeeeleelleellllekpPk....",
    "...kPpkeeeeeeeeeeeeeeeeekpPk....",
    "...kPpkkkkkkkkkkkkkkkkkkkpPk....",
    "...kPpppppppppppppppppppppPk....",
    "...kPpppdddpppppppppppppppPk....",
    "...kPpppdddppppppdddpdddppPk....",
    "...kPpdddddddppppdddpdddppPk....",
    "...kPpppdddppppppdddpdddppPk....",
    "...kPpppdddpppppppppppppppPk....",
    "...kPpppppppppppppppppppppPk....",
    "...kkkkkkkkkkkkkkkkkkkkkkkkk....",
    "................................",
)

# A bench is a list of things to check, so that is what it is: a board, a clip,
# and three rows ticked off.  Kept left of x=20 and below y=10, which is where
# the shared crescent goes -- the badge is stamped over the grid, and a board it
# had punched a hole in would read as a broken picture rather than as a moon
# behind one.
GEN1_BENCH_NIGHTLY = (
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "................................",
    "........kkkkkkk.................",
    "........klllllk.................",
    "........klppplk.................",
    "...kkkkkklppplkkkkkk............",
    "...kppppklllllkppppk............",
    "...kpdddkkkkkkkdddpk............",
    "...kpddddddddmddddpk............",
    "...kpdddddddmdddddpk............",
    "...kpddmdddmddddddpk............",
    "...kpdddmdmdddllldpk............",
    "...kpddddmddddllldpk............",
    "...kpddddddddmddddpk............",
    "...kpdddddddmdddddpk............",
    "...kpddmdddmddddddpk............",
    "...kpdddmdmdddllldpk............",
    "...kpddddmddddllldpk............",
    "...kpddddddddmddddpk............",
    "...kpdddddddmdddddpk............",
    "...kpddmdddmddddddpk............",
    "...kpdddmdmdddllldpk............",
    "...kpddddmddddllldpk............",
    "...kpdddddddddddddpk............",
    "...kpppppppppppppppk............",
    "...kkkkkkkkkkkkkkkkk............",
    "................................",
    "................................",
)

# `wild_green_nightly` is deliberately not here.  It is not a mod somebody
# browses beside the others -- it is what the nightly CARTRIDGE is, and it
# carries the cart's name in the launcher, so it wears the cart's own label
# instead of anything drawn in this file.  tools/build_index.py syncs it from
# the mods repo, the same way the cart's listing already did.
#
# The grid it used to use is left below rather than deleted: it is the only
# record of what the icon looked like, and a channel that grows a second green
# cart may want it back.
ICONS = {
    "gen1_wild_ui_nightly": GEN1_WILD_UI_NIGHTLY,
    "gen1_wild_qol_nightly": GEN1_WILD_QOL_NIGHTLY,
    "gen1_bench_nightly": GEN1_BENCH_NIGHTLY,
}


def stamped(rows):
    """The grid with the crescent laid into it."""
    grid = [list(row) for row in rows]
    left, top = MOON_AT
    for y, line in enumerate(MOON_ROWS):
        for x, cell in enumerate(line):
            if cell == ".":
                continue
            gy, gx = top + y, left + x
            if 0 <= gy < GRID and 0 <= gx < GRID:
                grid[gy][gx] = cell
    return grid


def png_bytes(pixels, size=SIZE):
    """An 8-bit RGB PNG of a size x size array of (r, g, b).

    Hand-rolled, so this file imports nothing but the standard library and a
    rebuild is byte-identical anywhere.  tools/make_favicon.py draws with it
    too, which is what keeps the tab icon and the cards the same object.
    """
    raw = bytearray()
    for row in pixels:
        raw.append(0)
        for r, g, b in row:
            raw += bytes((r, g, b))

    def chunk(tag, body):
        return (struct.pack(">I", len(body)) + tag + body
                + struct.pack(">I", zlib.crc32(tag + body) & 0xffffffff))

    header = struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header)
            + chunk(b"IDAT", zlib.compress(bytes(raw), 9))
            + chunk(b"IEND", b""))


def render(rows):
    """The grid on the channel's night ground, inside a one-pixel frame.

    The ground is what makes an icon here read as a nightly at thumbnail size,
    before the shape on it has been read at all: the stable index's icons are
    each their own colour, and every icon in this one is on the same purple.
    """
    grid = stamped(rows)
    out = []
    for y in range(GRID):
        line = []
        for x in range(GRID):
            cell = grid[y][x]
            if x == 0 or y == 0 or x == GRID - 1 or y == GRID - 1:
                line.append(INK)
            else:
                line.append(PALETTE.get(cell, NIGHT))
        scaled = []
        for colour in line:
            scaled.extend([colour] * SCALE)
        for _ in range(SCALE):
            out.append(scaled)
    return out


def folders():
    """mod id -> the folder it is listed in."""
    out = {}
    if not MODS.is_dir():
        return out
    for folder in sorted(p for p in MODS.iterdir() if p.is_dir()):
        _, _, mod_id = folder.name.partition("@")
        out[mod_id or folder.name] = folder
    return out


def wears_a_label(folder):
    """Does this listing take art from its own repo instead of an icon here?"""
    meta = folder / "meta.json"
    if not meta.is_file():
        return False
    try:
        return bool(json.loads(meta.read_text(encoding="utf-8")).get("label"))
    except (ValueError, OSError):
        return False


def main(argv):
    wanted = set(argv[1:])
    listed = folders()

    for rows in ICONS.values():
        if len(rows) != GRID or any(len(row) != GRID for row in rows):
            raise SystemExit("make_icons: an icon grid is not %dx%d" % (GRID, GRID))

    drawn, missing = 0, []
    for mod_id, folder in sorted(listed.items()):
        if wanted and mod_id not in wanted:
            continue
        rows = ICONS.get(mod_id)
        if rows is None:
            # A folder whose meta.json names `label` wears art from its own
            # repo, synced by tools/build_index.py, and has no business having
            # one drawn here.  Anything else with no grid is a mod nobody has
            # drawn yet, which is still worth failing over.
            if wears_a_label(folder):
                print("  %s wears its own label" % folder.name)
                continue
            missing.append(mod_id)
            continue
        body = png_bytes(render(rows))
        target = folder / "thumbnail.png"
        if not target.exists() or target.read_bytes() != body:
            target.write_bytes(body)
            print("  wrote %s" % target.relative_to(ROOT))
        else:
            print("  %s already current" % target.relative_to(ROOT))
        drawn += 1

    for mod_id in missing:
        print("make_icons: no icon for %r; add a grid to ICONS" % mod_id,
              file=sys.stderr)

    print("%d icon(s)" % drawn)
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
