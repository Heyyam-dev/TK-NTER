# Data Model — cədvəllər və əlaqələr

> Məntiqi model. Sahə tipləri, indekslər və miqrasiyalar `DATABASE_SCHEMA.md` faylındadır.

---

## 1. Cədvəllər

| Cədvəl | Modul | Təyinat | Əsas sahələr |
|---|---|---|---|
| users | AUTH | | id, name, email, role_id |
| products | INV | | |
| stock_movements | INV | | |
| purchase_orders | PUR | | |

## 2. Əlaqələr

| Cədvəl | Əlaqə | Cədvəl | Açar |
|---|:---:|---|---|
| users | 1 : N | purchase_orders | purchase_orders.created_by |

## 3. Biznes qaydaları

- _[məs. Anbar qalığı mənfi ola bilməz]_
