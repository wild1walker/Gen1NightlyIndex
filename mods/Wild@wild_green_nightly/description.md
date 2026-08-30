# Wild Green Nightly

**The player wears green, he is called GREEN, and the title screen says so.**
That is the whole mod — and this is its test build.

It installs under its own id and **conflicts with the stable Wild Green on
purpose**: run one or the other, never both.

## What is new

- **`PLAYER` takes effect where you are standing.** It used to wait for the
  next launch for the overworld walker. It does not any more: every colour is
  written to disk at install anyway, so switching one is a change of which
  file a record points at, and the walker changes under your feet. `PORTRAIT
  SKIN` moves with it.
- **The version ribbon follows `PLAYER`.** It used to stay green in every
  suit. Put the character in purple and the title is lettered in purple; the
  words still say `GREEN`.
- **The title screen's colours are right in every display mode.**
  `WILD GREEN VERSION` came out yellow-green on pale yellow under `ADVANCED`,
  half the POKE BALL was skin-coloured and so was the highlight on the
  copyright line. All three were the same bug: those colours were named-palette
  overrides, and two of the engine's display modes never consult the palette
  registry at all.

Everything else is the mod you know: nine colours for the player, the
`GREEN`/`WILD`/`VERSION` name list, and not one green pixel shipped — the art
is recoloured from your own imported cache at install and `PLAYER = RED` hands
the original character straight back.
