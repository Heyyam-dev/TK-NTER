# Tkinter Dashboard Application Enhancements

> Tkinter masaüstü proqramının interfeysini tünd temalı dashboard görünüşünə gətirmək, cədvəllərini, qrafiklərini və Excel/Word/PDF hesabatlarını təkmilləşdirmək layihəsi. Proses sənədləşdirilmiş, mərhələli və yoxlanıla bilən şəkildə aparılır.

---

## 1. Məqsəd

Proqram yenidən yazılmır. Məqsəd interfeysi istinad şəklindəki kimi panellərə bölünmüş tünd dashboard-a çevirmək, cədvəlləri rahatlaşdırmaq, qrafiklər əlavə etmək və hesabatları üç formatda ixrac etməkdir.

| Sahə | Dəyər |
|---|---|
| Səviyyə | Entry Level |
| Büdcə | Elanda göstərilməyib |
| Texnologiyalar | Python, Tkinter (ttk), Matplotlib |

> Upwork elanında PyQt6 göstərilib; Tkinter-ə keçid `open_questions.md` faylında müştəri ilə razılaşdırılmalı məsələ kimi qeyd olunub.

## 2. Mərhələlər

| # | Mərhələ | Tapşırıqlar | Nəticə |
|:---:|---|---|---|
| 1 | Audit və əsas | `AUD-001`, `THM-001`, `LAY-001` | Tünd tema, üst panel, tablar, 2×2 panel şəbəkəsi |
| 2 | Dashboard | `CHT-001`, `KPI-001`, `CHT-002` – `CHT-004` | KPI kartları və üç qrafik paneli |
| 3 | Cədvəllər | `TBL-001`, `TBL-002` | Sıralama, axtarış, filtr |
| 4 | Hesabatlar və təhvil | `RPT-001` – `RPT-003`, `QA-001` | Excel, Word, PDF ixracı |

Tapşırıqların tam siyahısı və qəbul meyarları: [plan.md](plan.md). Dizayn hədəfi, rəng tokenləri və kod strukturu: [PROJECT.md](PROJECT.md).

## 3. İş prosesi

| Addım | Prompt | Nəticə |
|:---:|---|---|
| 1 | Prompt 01 — Tələblər | `PROJECT.md`, `requirements.md`, `open_questions.md` |
| 2 | Prompt 02 — Modullar və arxitektura | `ARCHITECTURE.md` |
| 3 | Prompt 03 — Verilənlər bazası | `DATA_MODEL.md`, `DATABASE_SCHEMA.md` (proqramda DB varsa) |
| 4 | Prompt 04 — Tapşırıq planı | `plan.md` |
| 5 | Prompt 05 — Planın yoxlanması | `PLAN_REVIEW.md` |
| 6 | Prompt 06 — Tapşırığın kodlaşdırılması | `src/`, `tests/` |

**Əsas qaydalar:**

1. Kod yalnız **təsdiqlənmiş** plan əsasında yazılır.
2. Hər dəfə yalnız **bir** tapşırıq (`TASK_ID`) icra olunur.
3. Cari tapşırıq yoxlanılıb təsdiqlənmədən növbətisinə keçilmir.
4. Asılılıq tamamlanmayıbsa, ondan asılı tapşırıq başlanmır (məs. `RPT-002`, `RPT-001` bitmədən).
5. Mövcud kod **kiçik və geri qaytarıla bilən** dəyişikliklərlə dəyişir; əlaqəsiz refaktor edilmir.
6. Mövcud funksiyalar pozulmamalıdır; hər dəyişiklikdən sonra proqramın açılması yoxlanılır.
7. Rəng və şrift yalnız `src/ui/theme.py` faylında təyin olunur.
8. Cədvəl, qrafik və hesabat eyni məlumat mənbəyindən (`src/data/provider.py`) oxuyur.
9. Büdcə və müddət mövcud kod alınmadan təsdiqlənmir.

## 4. Qovluq strukturu

```text
construction-erp/
├── README.md               Layihənin məqsədi və başlanğıc təlimatı
├── PROJECT.md              Təsdiqlənmiş kontekst, dizayn hədəfi, kod strukturu
├── requirements.md         Funksional və qeyri-funksional tələblər
├── open_questions.md       Müştəridən soruşulmalı məsələlər
├── ARCHITECTURE.md         Sistem arxitekturası
├── DATA_MODEL.md           Məlumat modeli
├── DATABASE_SCHEMA.md      Fiziki DB sxemi
├── plan.md                 Tapşırıqların ardıcıllığı və statusu
├── PLAN_REVIEW.md          Müstəqil texniki yoxlama
├── SECURITY.md             Təhlükəsizlik qaydaları
├── TEST_PLAN.md            Test strategiyası
├── prompts/
│   └── PROMPT_06_implement_task.md
├── src/                    Proqram kodu (strukturu: PROJECT.md, bölmə 6)
├── database/migrations/    DB dəyişiklikləri (varsa)
└── tests/                  Avtomatlaşdırılmış testlər
```

> Qovluğun adı (`construction-erp`) əvvəlki layihədən qalıb. İstəsəniz adını dəyişə bilərik.

## 5. Başlanğıc

1. Mövcud Tkinter kodunu `src/` qovluğuna yerləşdirin və ya `PROJECT.md` bölmə 7-də "sıfırdan hazırlanır" seçin (`AUD-001` buna bağlıdır).
2. `open_questions.md` üzrə sualları aydınlaşdırın (ilk növbədə PyQt6 → Tkinter).
3. Plan təsdiqləndikdən sonra `prompts/PROMPT_06_implement_task.md` faylında `TASK_ID` yazıb Claude-a verin. İlk tapşırıq: `AUD-001`, sonra `THM-001`.
