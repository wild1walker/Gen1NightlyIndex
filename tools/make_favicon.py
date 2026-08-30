#!/usr/bin/env python3
"""Draw the site's favicon: the channel's moon, on the channel's night.

    python3 tools/make_favicon.py

Writes site/favicon.png (180, also the apple-touch icon) and
site/favicon-32.png.

The stable index cuts its favicon out of the Gen1Wild wordmark, so the tab
icon and the banner stay the same object.  This index has no wordmark of its
own and should not borrow that one: a nightly is not the thing it is a nightly
OF, and a tab that looks identical to the stable site's is a tab somebody will
open by mistake.

So the mark is the badge every icon in this index already carries -- the same
crescent, from the same `tools/make_icons.py`, on the same night purple.  It
is computed rather than drawn, at whatever size is asked for, so the 32 is not
a resampled 180 and neither has soft edges.
"""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from make_icons import (INK, MOON, MOON_BITE_DX, MOON_BITE_R, MOON_D,  # noqa: E402
                        MOON_R, NIGHT, png_bytes)

OUT = ROOT / "site"
SIZES = ((180, "favicon.png"), (32, "favicon-32.png"))

# The moon's own box is 10 cells wide in an icon; here it is the whole picture,
# with a little air round it.
BOX = 12.0


def draw(size):
    """One crescent, filling `size` pixels, on the night ground."""
    scale = size / BOX
    centre = (size - 1) / 2.0
    # the moon sits a shade left of centre, because a crescent's mass is on
    # its thick side and a centred bounding box reads as off-centre
    offset = 0.6 * scale
    rows = []
    for y in range(size):
        line = []
        for x in range(size):
            dx = (x - centre + offset) / scale
            dy = (y - centre) / scale
            outer = dx * dx + dy * dy
            bx = dx - MOON_BITE_DX
            bite = bx * bx + dy * dy
            if outer > MOON_R * MOON_R or bite <= MOON_BITE_R * MOON_BITE_R:
                line.append(NIGHT)
                continue
            rim = (MOON_R - 0.9) * (MOON_R - 0.9)
            inner_rim = (MOON_BITE_R + 0.8) * (MOON_BITE_R + 0.8)
            line.append(MOON_D if (outer > rim or bite <= inner_rim) else MOON)
        rows.append(line)
    # a one-pixel frame, the same as an icon's
    for x in range(size):
        rows[0][x] = INK
        rows[size - 1][x] = INK
    for y in range(size):
        rows[y][0] = INK
        rows[y][size - 1] = INK
    return rows


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for size, name in SIZES:
        body = png_bytes(draw(size), size)
        target = OUT / name
        if target.exists() and target.read_bytes() == body:
            print("  %s already current" % target.relative_to(ROOT))
            continue
        target.write_bytes(body)
        print("  wrote %s  %dx%d" % (target.relative_to(ROOT), size, size))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
