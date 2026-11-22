# Plan — tapşırıqların ardıcıllığı və statusu

Stek: **Tkinter (ttk) + Matplotlib**. Dizayn hədəfi və rəng tokenləri: `PROJECT.md`, bölmə 3.

## Status dəyərləri

| Status | Mənası |
|---|---|
| `TODO` | Başlanmayıb |
| `IN_PROGRESS` | İcra olunur |
| `REVIEW` | Yoxlamadadır |
| `DONE` | Təsdiqlənib |
| `BLOCKED` | Asılılıq və ya açıq sual var |

> `DONE` statusu yalnız icra olunmuş testlərlə sübut olunduqda qoyulur.

---

## Asılılıq sxemi

```text
AUD-001 → THM-001 → LAY-001 ─┬→ KPI-001 ──────────────┐
                             │                         │
              CHT-001 ───────┼→ CHT-002, CHT-003, CHT-004
              (THM-001-dən)  │                         │
                             └→ TBL-001 → TBL-002      │
                                    │                  │
                                    └→ RPT-001 → RPT-002 → RPT-003 → QA-001
                                                  ↑
                                        CHT-002 – CHT-004
```

---

## Mərhələ 1 — Audit və əsas

| TASK_ID | Tapşırıq | Fayllar | Asılılıqlar | Qəbul meyarları | Status |
|---|---|---|---|---|:---:|
| AUD-001 | Mövcud kodun auditi: ekranlar, asılılıqlar, işə salınma, məlumat mənbəyi | `AUDIT.md` | — | Proqram yerli mühitdə açılır; ekranlar, məlumat mənbəyi və problemlər sənədləşdirilib; kod dəyişmir | `BLOCKED` |
| THM-001 | Tema: rəng/şrift tokenləri və `ttk.Style` (`clam` əsasında) — Frame, Label, Button, Entry, Combobox, Treeview, Scrollbar | `src/ui/theme.py` | AUD-001 | Bütün rənglər yalnız `theme.py`-dadır; standart boz ttk fonu heç bir vidcetdə görünmür; ə, ı, ö, ü, ş, ç, ğ düzgün göstərilir | `TODO` |
| LAY-001 | Karkas: üst panel, tab zolağı, 2×2 panel şəbəkəsi (`grid` + `weight`), başlıqlı `Panel` vidceti | `src/ui/shell.py`, `src/ui/widgets/panel.py`, `src/ui/views/dashboard.py` | THM-001 | Tablar arası keçid işləyir; pəncərə 1024×640-dan tam ekrana qədər dəyişəndə panellər üst-üstə düşmür və proporsional böyüyür; mövcud funksiyalar işləyir | `TODO` |

## Mərhələ 2 — Dashboard

| TASK_ID | Tapşırıq | Fayllar | Asılılıqlar | Qəbul meyarları | Status |
|---|---|---|---|---|:---:|
| CHT-001 | Qrafik əsası: tünd temalı `Figure` yaradan köməkçi, `FigureCanvasTkAgg` yerləşdirilməsi, ölçü dəyişəndə yenidən çəkilmə | `src/charts/base.py` | THM-001 | Qrafikin fonu panel fonu ilə eynidir (ağ çərçivə yoxdur); boş məlumatda xəta yox, "Məlumat yoxdur" yazısı çıxır; pəncərə bağlananda fiqur yaddaşdan silinir | `TODO` |
| KPI-001 | A paneli: `KpiCard` (böyük rəqəm, alt yazı, mini xətt/sütun qrafiki) | `src/ui/widgets/kpi_card.py`, `src/charts/builders.py` | LAY-001, CHT-001 | 3–4 kart göstərilir; rəqəmlər `data/provider.py` ilə eynidir; minlik ayırıcı düzgündür | `TODO` |
| CHT-002 | B paneli: pie/donut + sağda leqenda (rəng, ad, rəqəm) | `src/charts/builders.py` | LAY-001, CHT-001 | Payların cəmi 100%-dir; leqendadakı rəqəmlər məlumatla eynidir; 5-dən çox kateqoriya "Digər" altında birləşir | `TODO` |
| CHT-003 | D paneli: dövr üzrə yığılmış sütun qrafiki | `src/charts/builders.py` | LAY-001, CHT-001 | Hər sütunun hündürlüyü dövrün cəminə bərabərdir; ox etiketləri üst-üstə düşmür | `TODO` |
| CHT-004 | C paneli: bölgə/kateqoriya üzrə rəqəmlər + üfüqi sütunlar (xəritə əvəzi) | `src/charts/builders.py` | LAY-001, CHT-001 | Sütunlar azalan sıra ilədir; rəqəmlər məlumatla eynidir | `TODO` |

## Mərhələ 3 — Cədvəllər

| TASK_ID | Tapşırıq | Fayllar | Asılılıqlar | Qəbul meyarları | Status |
|---|---|---|---|---|:---:|
| TBL-001 | `DataTable`: tünd stilli `ttk.Treeview`, zolaqlı sətirlər, sürüşdürmə, başlığa kliklə sıralama (rəqəm/tarix/mətn düzgün tipdə) | `src/ui/widgets/data_table.py`, `src/ui/views/table_view.py` | LAY-001 | Rəqəm sütunu rəqəm kimi sıralanır (2 < 10); təkrar klik istiqaməti dəyişir və ox işarəsi göstərilir | `TODO` |
| TBL-002 | Axtarış sahəsi və sütun filtri (`Combobox`); nəticə sayı göstəricisi | `src/ui/widgets/data_table.py` | TBL-001 | Axtarış böyük/kiçik hərfə və Azərbaycan hərflərinə (İ/ı, Ə/ə) həssas deyil; 10 000 sətirdə yazarkən donma yoxdur (gecikdirilmiş axtarış) | `TODO` |

## Mərhələ 4 — Hesabatlar və təhvil

| TASK_ID | Tapşırıq | Fayllar | Asılılıqlar | Qəbul meyarları | Status |
|---|---|---|---|---|:---:|
| RPT-001 | Excel hesabatı: cədvəlin cari (filtrlənmiş) görünüşü, başlıq stili, rəqəm formatı | `src/reports/excel.py` | TBL-002 | Fayl Excel-də açılır; rəqəmlər mətn deyil, rəqəm tipindədir; cəm cədvəllə üst-üstə düşür | `TODO` |
| RPT-002 | Word hesabatı: başlıq, KPI xülasəsi, qrafik şəkilləri, cədvəl | `src/reports/word.py` | RPT-001, CHT-002, CHT-003, CHT-004 | Fayl Word-də açılır; qrafiklər açıq fonla (çap üçün) daxil edilir; cədvəl daxildir | `TODO` |
| RPT-003 | PDF hesabatı | `src/reports/pdf.py` | RPT-002 | Fayl açılır; Azərbaycan simvolları (ə, ı, ö, ü, ş, ç, ğ) düzgün görünür; uzun cədvəl səhifələrə düzgün bölünür | `TODO` |
| QA-001 | Yekun yoxlama və təhvil | `CHANGELOG.md` | RPT-003 | Bütün meyarlar sübut olunub; dəyişikliklərin siyahısı və işə salma təlimatı təqdim edilib | `TODO` |

---

## Bloklayan məsələlər

| TASK_ID | Səbəb | Nə lazımdır |
|---|---|---|
| AUD-001 | `src/` boşdur — mövcud Tkinter kodu qovluqda yoxdur | Kodu `src/`-ə yerləşdirmək **və ya** "sıfırdan hazırlanır" qərarını `PROJECT.md` bölmə 7-də qeyd etmək |

Sıfırdan hazırlanırsa, `AUD-001` "nümunə məlumat dəsti və `data/provider.py` skeleti" tapşırığı ilə əvəz olunur.

## Dəyişiklik tarixçəsi

| Tarix | TASK_ID | Dəyişiklik |
|---|---|---|
| 2026-10-27 | — | Plan Upwork elanına əsasən yenidən quruldu |
| 2026-11-16 | — | Stek PyQt6-dan Tkinter (ttk)-ə dəyişdi; dashboard istinad şəkli əsasında tapşırıqlar detallaşdırıldı (THM-001, LAY-001, KPI-001, CHT-001 – CHT-004, TBL-002 əlavə olundu; UI-001 → THM-001 + LAY-001) |
