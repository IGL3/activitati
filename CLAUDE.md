# Activitățile mele (fost „Jurnal de ședință”)

Tracker personal pentru ședința zilnică de dimineață (UI în limba română).
Aspect: `.shell` = meniu fix în stânga (`.side`: căutare, navigație `.nav[data-nav]`, temă, cont/sincronizare) + `main.content`.
În `#app` (Activități): `.maincol` (antet, compunere, linie de timp `.tl` cu restanțe/azi/altă dată) + `.rcol` (calendar `#calBox`, „Pe scurt” `#weekBox`, `#secIssues`, `#secNotes`).
Pe telefon (<860px) `.side` are `display:contents`: meniul devine un rând de butoane lipit sus, tema și contul ajung la final.
Comutarea între aplicații folosește încă butoanele ascunse `#swAct`/`#swBet` și taburile `#tabDay`/`#tabRec`/`#btTab*`; meniul din stânga doar le apasă (script la final).
Sunt două aplicații: **Activități** (`#app`) și **Pariuri** (jurnal de pariuri fotbal, `#btApp`, clase/id-uri cu prefix `bt`).
Pariurile: în Claude stau în `data/users/<id>/betdata/bets` și `data/users/<id>/betsettings`; pe GitHub Pages în localStorage (`bt-bets`, `bt-settings`) și intră în backup sub cheia `pariuri`.

## Notițe pe echipe și export (tab Pariuri)
- Sub-tabul **Notițe**: țară → echipă → oricâte notițe separate (adaugă / editează / șterge). Lista de echipe e `LEAGUES` în cod, sezonul **2026–27**
  (La Liga, Premier League, SuperLiga, Serie A, Ligue 1, Pro League (18 echipe), Bundesliga, Primeira Liga). Actualizează-o vara, după promovări/retrogradări.
  Stocare: doc `data/users/<id>/betnotes` = `{notes:{"RO|FCSB":{items:[{id,t,u}]}}}` (formatul vechi `{t,u}` e convertit de `normNotes`); local `bt-notes`; intră în backup ca `pariuri.notite`.
- Sub-tabul **Bani**: depuneri, bonusuri, retrageri. Colecția `data/users/<id>/betdata/txns` ({type:dep|bonus|ret, amount, date, book, note}); local `bt-txns`; backup `pariuri.tranzactii`.
  Bankroll curent = bankroll inițial + depuneri + bonusuri − retrageri + profit pariuri − mize în așteptare.
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
