# Test strategiyası

> Test yalnız **həqiqətən icra olunubsa** "keçdi" sayılır. Əmr və nəticə mütləq qeyd olunur.

---

## 1. Test növləri

| Növ | Məqsəd | Alət |
|---|---|---|
| Unit | Ayrı funksiya və siniflər | _[məs. PHPUnit]_ |
| İnteqrasiya | Modul + verilənlər bazası | |
| Qəbul | Tapşırığın qəbul meyarları | |

## 2. Testlərin işə salınması

```bash
# [məs. vendor/bin/phpunit tests/]
```

## 3. Prioritet ssenarilər

- Anbar qalığının düzgün hesablanması
- Səlahiyyəti olmayan istifadəçinin girişinin bloklanması
- Tranzaksiya xətasında dəyişikliklərin geri qaytarılması

## 4. Test nəticələri

| TASK_ID | Test | Əmr | Nəticə | Tarix |
|---|---|---|:---:|---|
