"""Refresh source/ from the live project. Run this BEFORE every stage.

The authoring crew reads ONLY source/. This script is the single point where
the live project enters the kit, so a stale read is a bug in one place, not five.
"""
import hashlib
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent
PROJECT = ROOT.parent
SRC = ROOT / "source"

COPIES = [
    (PROJECT / "Stratocracy_Prototype_GDD.md", SRC / "gdd.md"),
    (PROJECT / "stratocracy-content" / "kb" / "rules.md", SRC / "kb_rules.md"),
    (PROJECT / "stratocracy-content" / "kb" / "setting.md", SRC / "kb_setting.md"),
]


def md5(p):
    return hashlib.md5(p.read_bytes()).hexdigest()


def main():
    SRC.mkdir(exist_ok=True)
    ok = True
    lines = []
    for src, dst in COPIES:
        if not src.exists():
            print(f"MISSING: {src}")
            ok = False
            continue
        shutil.copyfile(src, dst)
        lines.append(f"{dst.name:16} <- {src}  md5={md5(dst)}")
        print(f"synced {dst.name:16} md5={md5(dst)}")
    (SRC / "MANIFEST.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    if not ok:
        sys.exit(1)
    print("\nsource/ is current. Now start Claude Code here and run a stage.")


if __name__ == "__main__":
    main()
