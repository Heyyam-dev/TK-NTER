# Təhlükəsizlik qaydaları

> Bütün tapşırıqlar üçün məcburidir.

---

## 1. Verilənlər bazası

- Bütün sorğular **parametrləşdirilmiş** olmalıdır (prepared statements).
- Məlumat bütövlüyü tələb olunan əməliyyatlar **tranzaksiya** daxilində icra olunur.

## 2. Autentifikasiya və avtorizasiya

- Parollar güclü hash alqoritmi ilə saxlanılır (`password_hash`).
- Avtorizasiya **həmişə serverdə** yoxlanılır; frontend yoxlaması kifayət deyil.
- Hər rol yalnız ona lazım olan səlahiyyətlərə malikdir.

## 3. Sirlər

- Parol, API açarı və tokenlər **kodda saxlanılmır** — `.env` / mühit dəyişənləri istifadə olunur.
- `.env` faylı versiya nəzarətinə əlavə edilmir.

## 4. Giriş məlumatları

- Bütün istifadəçi girişləri serverdə yoxlanılır.
- HTML-ə çıxış escape olunur (XSS).
- Formalar CSRF tokeni ilə qorunur.

## 5. Audit

- Kritik əməliyyatlar (anbar hərəkəti, satınalma təsdiqi) loglanır: kim, nə vaxt, nə etdi.
