# PROJECT — Təsdiqlənmiş layihə konteksti

> Bu fayl yalnız **təsdiqlənmiş** məlumatları saxlayır. Fərziyyələr və cavabsız suallar `open_questions.md` faylına yazılır.

| Sahə | Dəyər |
|---|---|
| Layihə adı | Tkinter Dashboard Application Enhancements |
| Müştəri | _[ad / Upwork profili]_ |
| Mənbə | Upwork elanı ("Maraqlı nümunə" etiketi) |
| Status | Qaralama |
| Son yenilənmə | 2026-11-16 |

---

## 1. Elanın təsdiqlənmiş məlumatları

| Sahə | Dəyər |
|---|---|
| İş | Mövcud masaüstü proqramın interfeysini düzəltmək, cədvəlləri təkmilləşdirmək, qrafikləri və Excel, Word, PDF hesabatlarını hazırlamaq |
| Büdcə | Elanın mətnində konkret qiymət göstərilməyib |
| Səviyyə | Entry Level |
| Elandakı texnologiyalar | Python, PyQt6, Matplotlib |

> **Stek qərarı (2026-11-16):** layihə **Tkinter (ttk) + Matplotlib** ilə aparılır. Elanda PyQt6 göstərildiyi üçün bu fərq `open_questions.md` faylında müştəri ilə razılaşdırılmalı məsələ kimi qeyd olunub.

## 2. Gözlənilən nəticə

Proqram **yenidən yazılmır**, təkmilləşdirilir. Hədəf — istinad şəklindəki kimi tünd rəngli, panellərə bölünmüş dashboard:

1. Səliqəli, tünd temalı və istifadəsi rahat interfeys.
2. Təkmilləşdirilmiş cədvəllər (sıralama, filtr, axtarış).
3. Matplotlib qrafikləri (panel daxilində, tema ilə eyni rənglərdə).
4. Excel, Word və PDF formatında hesabatlar.

## 3. Dizayn hədəfi (istinad şəkli əsasında)

### 3.1 Ekranın quruluşu

```text
┌──────────────────────────────────────────────────────────────┐
│ Üst panel: loqo · menyu · sağda əməliyyat düymələri (ixrac)  │
├──────────────────────────────────────────────────────────────┤
│ Tablar:  [ Bölmə 1 ]  [ Bölmə 2 ]  [ Bölmə 3 ]               │
├───────────────────────────────┬──────────────────────────────┤
│ A. Qısa göstəricilər (KPI)    │ B. Paylanma (pie/donut)      │
│    böyük rəqəm + mini qrafik  │    sağda leqenda və rəqəmlər │
├───────────────────────────────┼──────────────────────────────┤
│ C. Bölgə/kateqoriya üzrə      │ D. Dövr üzrə yığılmış        │
│    rəqəmlər + üfüqi sütunlar  │    sütun qrafiki (stacked)   │
└───────────────────────────────┴──────────────────────────────┘
```

| Panel | Məzmun | Komponent |
|---|---|---|
| Üst panel | Loqo, menyu, ixrac düymələri | `ttk.Frame` + `ttk.Button` |
| Tablar | Bölmələr arası keçid | Xüsusi tab zolağı (`ttk.Frame`), `ttk.Notebook` deyil — stil nəzarəti üçün |
| A. KPI | 3–4 əsas rəqəm, hər birində mini xətt/sütun qrafiki | `KpiCard` + Matplotlib sparkline |
| B. Paylanma | Kateqoriyalar üzrə pay | Matplotlib pie/donut + leqenda |
| C. Bölgələr | Bölgə üzrə rəqəmlər | Üfüqi sütun qrafiki |
| D. Dövr | Aylar üzrə yığılmış sütunlar | Matplotlib stacked bar |
| Cədvəl ekranı | Detal sətirləri | `ttk.Treeview` |

> İstinad şəklindəki **dünya xəritəsi** Tkinter + Matplotlib ilə əlavə kitabxanasız çəkilmir. C panelində xəritə əvəzinə üfüqi sütun qrafiki planlaşdırılıb; xəritə tələb olunarsa ayrıca tapşırıq kimi qiymətləndirilir.

### 3.2 Rəng və şrift tokenləri

Rənglər istinad şəklindən **təxmini** götürülüb, müştəri təsdiqindən sonra dəqiqləşir. Hamısı tək faylda (`src/ui/theme.py`) saxlanılır, başqa yerdə rəng kodu yazılmır.

| Token | Dəyər | İstifadə |
|---|---|---|
| `BG` | `#1A1330` | Pəncərənin fonu |
| `PANEL` | `#241B3F` | Panel və kartların fonu |
| `PANEL_HEADER` | `#2E2350` | Panel başlığı, üst panel |
| `BORDER` | `#3A2E5E` | Ayırıcı xətlər |
| `TEXT` | `#F2EEFA` | Əsas mətn, böyük rəqəmlər |
| `TEXT_MUTED` | `#A79DC4` | Alt yazılar, ox etiketləri |
| `ACCENT_1` | `#3DE8C5` | Əsas vurğu (firuzəyi) |
| `ACCENT_2` | `#F6A55C` | Narıncı |
| `ACCENT_3` | `#E0569B` | Çəhrayı |
| `ACCENT_4` | `#8B6CF0` | Bənövşəyi |
| `ACCENT_5` | `#F5D76E` | Sarı |

| Şrift | Dəyər |
|---|---|
| Ailə | Segoe UI (Windows-da standart; ə, ı, ö, ü, ş, ç, ğ dəstəkləyir) |
| KPI rəqəmi | 22 pt, qalın |
| Panel başlığı | 10 pt, qalın, böyük hərflə |
| Əsas mətn | 10 pt |
| Alt yazı | 8 pt |

## 4. Əhatə dairəsi

**Daxildir:**
- Tünd tema, layout, tab naviqasiyası
- KPI kartları və dörd panelli dashboard
- Cədvəl komponentlərinin təkmilləşdirilməsi
- Hesabat ixracı: Excel, Word, PDF

**Daxil deyil (təsdiq gözləyir):**
- Yeni biznes məntiqi və yeni modullar
- Verilənlər bazasının yenidən qurulması
- Veb versiya və ya başqa platformaya keçid
- Coğrafi xəritə vizualı

## 5. Texnologiya steki

| Qat | Texnologiya | Qeyd |
|---|---|---|
| Dil | Python 3.10+ | Dəqiq versiya mövcud koddan asılıdır |
| UI | Tkinter + `ttk` (`clam` mövzusu əsasında xüsusi stil) | Standart kitabxana, əlavə quraşdırma yoxdur |
| Qrafik | Matplotlib (`FigureCanvasTkAgg`) | |
| Excel | _[openpyxl]_ | Təklifdir |
| Word | _[python-docx]_ | Təklifdir |
| PDF | _[ReportLab]_ | Təklifdir; Azərbaycan simvolları üçün TTF şrift qeydiyyatı lazımdır |

Kitabxana seçimləri **təklifdir**, müştəri ilə razılaşdırılana qədər təsdiqlənmiş sayılmır.

## 6. Kod strukturu (hədəf)

```text
src/
├── main.py                 Giriş nöqtəsi
├── ui/
│   ├── theme.py            Rəng/şrift tokenləri, ttk.Style qurulması
│   ├── shell.py            Üst panel, tablar, məzmun sahəsi
│   ├── widgets/
│   │   ├── panel.py        Başlıqlı panel
│   │   ├── kpi_card.py     KPI kartı
│   │   └── data_table.py   Treeview: sıralama, filtr, axtarış
│   └── views/
│       ├── dashboard.py    Dörd panelli ekran
│       └── table_view.py   Cədvəl ekranı
├── charts/
│   ├── base.py             Tünd temalı Figure yaradılması
│   └── builders.py         sparkline, pie, bar, stacked bar
├── data/
│   └── provider.py         Məlumatın tək mənbəyi (UI, qrafik və hesabat buradan oxuyur)
└── reports/
    ├── excel.py
    ├── word.py
    └── pdf.py
```

Əsas prinsip: **cədvəl, qrafik və hesabat eyni `data/provider.py` funksiyalarından oxuyur** — rəqəmlərin üst-üstə düşməsi bununla təmin olunur.

## 7. Mövcud kod bazası

- [ ] Mövcud Tkinter kodu `src/` qovluğuna yerləşdirilib
- [ ] Sıfırdan hazırlanır

> Hazırda `src/` boşdur. Bu seçim edilmədən `AUD-001` başlamır, qiymət və müddət təsdiqlənmir.

## 8. Mərhələlər və ödəniş

| # | Mərhələ | Tapşırıqlar | Nəticə | Qəbul meyarı | Məbləğ | Müddət |
|:---:|---|---|---|---|---:|---|
| 1 | Audit və əsas | AUD-001, THM-001, LAY-001 | Tünd tema, üst panel, tablar, boş panellər | Proqram açılır; pəncərə ölçüsü dəyişəndə panellər düzgün yerləşir | _[razılaşma]_ | |
| 2 | Dashboard | KPI-001, CHT-001 – CHT-004 | Dörd panel real məlumatla dolu | Hər qrafikin rəqəmləri məlumat mənbəyi ilə eynidir | _[razılaşma]_ | |
| 3 | Cədvəllər | TBL-001, TBL-002 | Sıralama, filtr, axtarış | 10 000 sətirdə donma yoxdur | _[razılaşma]_ | |
| 4 | Hesabatlar | RPT-001 – RPT-003, QA-001 | Excel, Word, PDF ixracı | Üç format da açılır, rəqəmlər cədvəllə eynidir | _[razılaşma]_ | |
