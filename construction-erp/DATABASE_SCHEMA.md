# Database Schema — fiziki verilənlər bazası sxemi

> `DATA_MODEL.md` məntiqi modeli (cədvəllər və əlaqələr) təsvir edir.
> Bu fayl isə real DB sxemini göstərir: sahə tipləri, açarlar, indekslər, məhdudiyyətlər.
> Hər dəyişiklik `database/migrations/` qovluğunda miqrasiya kimi saxlanılır.

## DBMS
_[məs. MySQL 8.0]_

## Cədvəllər

### `table_name`
| Sahə | Tip | NULL | Default | Açar | Qeyd |
|---|---|---|---|---|---|
| id | BIGINT UNSIGNED | NO | AUTO_INCREMENT | PK | |

**İndekslər:**
**Xarici açarlar:**

## Miqrasiyalar
| Fayl | TASK_ID | Təsvir | Tarix |
|---|---|---|---|
