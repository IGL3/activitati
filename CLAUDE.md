# Jurnal de ședință

Tracker personal pentru ședința zilnică de dimineață (UI în limba română).
Pagina are două taburi sus: **Activități** (jurnalul, `#app`) și **Pariuri** (jurnal de pariuri fotbal, `#btApp`, clase/id-uri cu prefix `bt`).
Pariurile: în Claude stau în `data/users/<id>/betdata/bets` și `data/users/<id>/betsettings`; pe GitHub Pages în localStorage (`bt-bets`, `bt-settings`) și intră în backup sub cheia `pariuri`.

## Notițe pe echipe și export (tab Pariuri)
- Sub-tabul **Notițe**: țară → echipă → notiță (autosalvare). Lista de echipe e `LEAGUES` în cod, sezonul **2026–27**
  (La Liga, Premier League, SuperLiga, Serie A, Ligue 1, Pro League (18 echipe), Bundesliga, Primeira Liga). Actualizează-o vara, după promovări/retrogradări.
  Stocare: doc `data/users/<id>/betnotes` = `{notes:{"RO|FCSB":{t,u}}}`; local `bt-notes`; intră în backup ca `pariuri.notite`.
- Butonul **Export**: alege luna → „Copiază pentru Claude” (CSV cu `;` + bankroll, de lipit în chat pentru analiză) sau, pe GitHub, descarcă CSV (Excel, zecimale cu virgulă).

## Lipește bilet (tab Pariuri)
Utilizatorul trimite poza biletului în chat; răspunde cu UN bloc JSON pe care îl lipește în „Lipește bilet”.
Câmpuri (română sau engleză): `meci`/`match`, `data`/`date` (YYYY-MM-DD), `competitie`/`comp`, `tip`/`market`
(1X2, Șansă dublă, GG / NG, Peste/Sub goluri, Handicap, Cornere, Cartonașe, Marcator, Pauză/Final, Bilet combinat, Altul),
`selectie`/`pick`, `cota`/`odds` (cota totală), `miza`/`stake`, `casa`/`book`, `result` (pending|won|lost|void|cashout), `nota`.
Dacă tipul de pariu nu există în listă, inventează un nume scurt și clar (ex. „Total ași”) și pune-l în `tip`: aplicația îl adaugă automat în lista de tipuri și în statistici (cerința utilizatorului).
Bilet combinat: `meciuri`/`legs`: [{meci, selectie, competitie}] + cota totală → un singur pariu. Mai multe bilete: array sau `{"pariuri":[…]}`.

## Două publicări ale aceleiași pagini — țin-le mereu sincronizate
- **Pagina Claude (artifact):** https://claude.ai/artifact/73Jxp6Lgf757zWvRpv5y66
  Sursa: `src/artifact.html` (fără doctype/html/head; începe cu `<title>`, `<link>` fonturi, `<style>`).
  Capabilități: `db` + `user` (date sincronizate între dispozitive).
- **GitHub Pages:** `index.html` din rădăcină, generat — nu-l edita de mână.
  Aici `window.claude` lipsește; un strat Firebase (proiect `myactivity9`, logare Google, Firestore) imită `claude.use("db"/"user")` pe aceleași căi `data/users/<uid>/...`, doar pe *.github.io. Fără logare, datele stau în localStorage; butoanele de backup rămân vizibile.

## La orice modificare
1. Editează `src/artifact.html`.
2. `python3 build.py` → regenerează `index.html`.
3. Republică artifact-ul: Artifact tool cu `url` de mai sus și `file_path` = `src/artifact.html` (fără `capabilities`, ca să rămână cele existente).
4. Commit + push pe `main` (GitHub Pages se actualizează în 1–2 minute).
