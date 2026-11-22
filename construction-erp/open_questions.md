# Açıq suallar

> Müştəridən cavab gözləyən məsələlər. Cavab alındıqdan sonra nəticə `PROJECT.md` və ya `requirements.md` faylına köçürülür.

---

## 1. Müraciətdən əvvəl yoxlanılmalı

- [ ] Müştərinin konkret nəticə gözləntisi nədir?
- [ ] Hazır kod bazası mövcuddur, yoxsa hər şey sıfırdan hazırlanmalıdır?
- [ ] Büdcə və mərhələlər hansı qaydada razılaşdırılacaq?
- [ ] Ödənişli mərhələlər və qəbul meyarları necə müəyyənləşdiriləcək?
- [ ] Mövcud PHP/MySQL kodunu davam etdirmək tələb olunur, yoxsa yeni arxitektura təklif etmək olar?

> ⚠️ Elan artıq başqa freelancer tərəfindən götürülə, texniki tələblər dəyişə və ya müştəri xüsusi təcrübə tələb edə bilər.

## 2. Texniki suallar

| # | Sual | Təsir etdiyi | Status | Cavab | Tarix |
|:---:|---|---|:---:|---|---|
| Q-001 | Elanda PyQt6 göstərilib, layihə isə Tkinter (ttk) ilə planlaşdırılıb. Müştəri Tkinter-i qəbul edirmi? | Bütün plan (`THM-001`-dən başlayaraq) | Açıq | | 2026-11-16 |
| Q-002 | Mövcud Tkinter kodu var, yoxsa sıfırdan hazırlanır? (`src/` hazırda boşdur) | `AUD-001`, qiymət və müddət | Açıq | | 2026-11-16 |
| Q-003 | Dashboard-da hansı göstəricilər (KPI) və hansı bölmələr (tablar) olmalıdır? Məlumat haradan gəlir (DB, Excel, CSV)? | `KPI-001`, `CHT-002` – `CHT-004`, `data/provider.py` | Açıq | | 2026-11-16 |
| Q-004 | İstinad şəklindəki dünya xəritəsi lazımdırmı? Planda onun əvəzinə üfüqi sütun qrafiki nəzərdə tutulub. | `CHT-004`, əhatə dairəsi | Açıq | | 2026-11-16 |
| Q-005 | Rəng palitrası istinad şəklindən təxmini götürülüb. Müştərinin öz brend rəngləri varmı? | `THM-001` | Açıq | | 2026-11-16 |
