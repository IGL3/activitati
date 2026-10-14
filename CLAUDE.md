# Jurnal de ședință

Tracker personal pentru ședința zilnică de dimineață (UI în limba română).
Pagina are două taburi sus: **Activități** (jurnalul, `#app`) și **Pariuri** (jurnal de pariuri fotbal, `#btApp`, clase/id-uri cu prefix `bt`).
Pariurile: în Claude stau în `data/users/<id>/betdata/bets` și `data/users/<id>/betsettings`; pe GitHub Pages în localStorage (`bt-bets`, `bt-settings`) și intră în backup sub cheia `pariuri`.

## Două publicări ale aceleiași pagini — țin-le mereu sincronizate
- **Pagina Claude (artifact):** https://claude.ai/artifact/73Jxp6Lgf757zWvRpv5y66
  Sursa: `src/artifact.html` (fără doctype/html/head; începe cu `<title>`, `<link>` fonturi, `<style>`).
  Capabilități: `db` + `user` (date sincronizate între dispozitive).
- **GitHub Pages:** `index.html` din rădăcină, generat — nu-l edita de mână.
  Aici `window.claude` lipsește, deci datele stau în localStorage; apar butoanele de backup.

## La orice modificare
1. Editează `src/artifact.html`.
2. `python3 build.py` → regenerează `index.html`.
3. Republică artifact-ul: Artifact tool cu `url` de mai sus și `file_path` = `src/artifact.html` (fără `capabilities`, ca să rămână cele existente).
4. Commit + push pe `main` (GitHub Pages se actualizează în 1–2 minute).
