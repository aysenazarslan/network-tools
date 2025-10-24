# app/run_original.py
import os, runpy, sys

def run_original(rel_path: str, args=None):
    base = os.path.dirname(__file__)
    path = os.path.join(base, "original", rel_path)
    if not os.path.exists(path):
        print(f"[ORIGINAL] Dosya yok: {path}")
        return
    print(f"[ORIGINAL] running: {path} {' '.join(args or [])}")
    old_argv = sys.argv[:]
    try:
        sys.argv = [path] + (args or [])
        runpy.run_path(path, run_name="__main__")
    finally:
        sys.argv = old_argv
