Создаём песочницу
---

CREATE TABLE "sex" (
  "id" serial NOT NULL,
  PRIMARY KEY ("id"),
  "title" character varying(100) NOT NULL
);
INSERT INTO "sex" ("id", "title")
VALUES ('1', 'male'), ('2', 'female'), ('3', 'others');


CREATE TABLE "employees" (
  "id" serial NOT NULL,
  PRIMARY KEY ("id"),
  "age" integer NOT NULL,
  "score" integer NOT NULL,
  "sex" integer NOT NULL,
  "created_at" timestamp NOT NULL
);

INSERT INTO "employees" (age, score, sex, created_at) SELECT
  floor(random()* (95-18+ 1) + 18) age,
  floor(random()*1000) score,
  generate_series(1, 3) sex,
  * FROM generate_series(
    '1888-03-29 00:00:00'::timestamp,
    '2024-03-29 23:00:00'::timestamp,
    '1 minute'::interval
  ) created_at


Задачки на оптимизацию запросов
---


--------- 1 задача
SELECT COUNT(*) as cnt, sex, age
FROM "employees"
WHERE "age" >= 20 AND "age" <= 60  AND "sex" IN (1, 2)
GROUP BY sex, age
ORDER BY age DESC, cnt


---------- 1 решение

CREATE INDEX idx_employees_main
ON employees (age DESC, sex)
WHERE age BETWEEN 20 AND 60 AND sex IN (1, 2);


-- Запрос

explain analyze
SELECT COUNT(*) as cnt, sex, age
FROM "employees"
where age between 20 and 60 AND "sex" IN (1, 2)
GROUP BY sex, age
ORDER BY age DESC, cnt


-- execution time: ~4200 ms
---------------

--------------- 2 задача


SELECT id, age
FROM "employees"
WHERE score > 100 and sex = 3
ORDER BY created_at DESC, age ASC
LIMIT 100 offset 10000


---------------- 2 решение

create index idx_employees_second on employees (score, sex, created_at desc, age asc)
include (id)
where score > 100 and sex = 3;

-- execution time: ~7500 ms
-------------------

----------------- 3 задача


select *
from employees
left join sex on sex.id = sex
where title LIKE '%male'
limit 100


------------------ 3 решение

CREATE INDEX idx_employees_sex ON employees (sex)
INCLUDE (id, age, score);

create index idx_sex_id on sex(id)
where title like '%male';

-- execution time: ~2ms



-------------------


------------------- 4 задача

SELECT id, age
FROM "employees"
WHERE score > 100
ORDER BY age ASC
LIMIT 100 offset 10000

------------------ 4 решение

create index idx_employees_fourth on employees (age asc, score)
include (id)
where score > 100;

-- execution time: ~1.275ms
----------------