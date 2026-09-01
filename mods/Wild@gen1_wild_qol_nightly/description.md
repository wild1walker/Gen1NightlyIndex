# Gen1WildQOL Nightly

**The quality-of-life half of the Gen1Wild suite, as one mod** — and this is
its test build. It installs under its own id and **conflicts with the stable
Gen1WildQOL on purpose**: run one or the other, never both.

## What is new

**Autosave no longer lands in the middle of the fade out of a battle.**

Two mistakes about the same blind spot: the mod knew that a fade is an
animation, and only knew it about the *overworld's* fades.

The end of a battle is not one of those. It is a stack state with a veil of its
own — the engine's white return, and the black outro on top of it — and the
overworld's own flags are false the whole way through, so those frames were
treated as the quietest in the game and the expensive half of a sync cycle ran
over them. Every battle, and it is the one fade you watch all the way through.

A state says how covered it is itself now, so a veil on its way somewhere is
exactly as busy as walking. A veil that is *full* is untouched — that is still
the best frame in the game to spend, and refusing it would bring back the door
freeze this all exists to remove.

And the write itself was landing on the worst frame of the outro: the black
outro was at full black for exactly one frame, and that one frame is the cut,
where the fade pops itself off the stack, runs the engine's own ending and
pushes itself back. The veil now has to have *stayed* full before anything is
spent under it.

## Works beside any voxel mod, and needs none

A [voxel mod][voxel] redraws the overworld as a 3D diorama and can draw the
battle over the map instead of over white paper. **Nothing here requires one
and nothing changes if you have none.**

There is not one of them — the original Dramatic Shape is defunct and three
maintained forks have grown out of it, each under an id of its own because only
one may run at a time. This bundle knew one of the six ids and now knows all of
them: `BATTLE_ART_VOXEL_FORK`, `DRAMALESS_SHAPE`, `potato_voxel`, and the
original lineage's three.

**The caught marker no longer lands away from the foe's name.** The forks
disagree about one thing: the Dramatic Shape lineage lifts the battle HUDs off
the flat 160x144 frame and draws them on its own world canvas; `DRAMALESS_SHAPE`
and `potato_voxel` leave them exactly where the engine put them. The marker read
a fork with no answer as a fork saying yes, so under those two it was drawn onto
a window-sized canvas at coordinates meant for a small one. It asks per frame
now, and the answer is no unless something said yes.

The follower keeps its scaled size in a voxel overworld under `potato_voxel`
too, which was missing for the same reason.

[voxel]: https://gen1recomp.org/voxel-mod

## Everything else

Unchanged from the stable bundle: sprinting, autosave with rollback backups,
auto continue, sound fixes, followers, all 151 catchable, EXP share, the move
reminder, menu layout and the mod manager. Every feature still switches on and
off by itself.
