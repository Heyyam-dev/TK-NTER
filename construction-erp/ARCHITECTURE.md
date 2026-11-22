# Arxitektura

---

## 1. Ümumi baxış

_[Sistemin qısa təsviri]_

```text
[Brauzer] → [Web server / PHP] → [MySQL]
```

## 2. Modullar

| Kod | Modul | Məsuliyyət | Asılı olduğu modullar |
|---|---|---|---|
| AUTH | İstifadəçilər və rollar | | — |
| INV | Anbar | | AUTH |
| PUR | Satınalma | | AUTH, INV |

## 3. Qovluq strukturu (`src/`)

```text
src/
└── _[modul qovluqları]_
```

## 4. Əsas axınlar

_[məs. Satınalma qəbulu → anbar qalığının artması]_

## 5. Texniki qərarlar

| # | Qərar | Səbəb | Alternativlər | Tarix |
|:---:|---|---|---|---|
| ADR-001 | | | | |
