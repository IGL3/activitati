"""Generează index.html (GitHub Pages) din src/artifact.html (pagina Claude)."""
import re, pathlib
root = pathlib.Path(__file__).parent
s = (root / "src/artifact.html").read_text(encoding="utf-8")
m = re.match(r"(<title>.*?</title>\n<link[^>]*>\n<style>.*?</style>)\n(.*)", s, re.S)
if not m:
    raise SystemExit("src/artifact.html trebuie să înceapă cu <title>, <link> fonturi și <style>")
head = ('<!doctype html>\n<html lang="ro">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<meta name="theme-color" content="#000000">\n')
out = head + m.group(1) + "\n</head>\n<body>\n" + m.group(2) + "\n</body>\n</html>\n"
(root / "index.html").write_text(out, encoding="utf-8")
print("index.html generat")
