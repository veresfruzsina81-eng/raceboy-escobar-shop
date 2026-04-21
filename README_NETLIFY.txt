# Raceboy x Escobar Shop - statikus Netlify verzió

Ez a csomag már NEM Django.
Ez egy egyszerű statikus webshop alap, ami megy GitHub repóban és Netlify-on.

## Fájlok
- index.html
- assets/style.css
- netlify.toml

## Hogyan tedd fel GitHubra
1. Nyisd meg a repót.
2. Töröld a régi Django fájlokat, vagy külön új repóba töltsd fel ezt a csomagot.
3. Az itt lévő fájlokat úgy töltsd fel, hogy az `index.html` a repó gyökerében legyen.

## Netlify beállítás
- Build command: hagyd üresen
- Publish directory: `.`

## Fontos
Ha még mindig a régi Django repó van fent Netlify alatt, akkor 404 maradhat.
Ebben az esetben vagy:
- új Netlify site-ot csinálsz ebből a csomagból, vagy
- a régi site deployját teljesen lecseréled erre.
