"""
Батч-импорт пользователей из внешнего источника в БД.
Гоняется по крону на пачках в десятки тысяч записей.
"""

import psycopg2

conn = psycopg2.connect("dbname=app user=app")


def import_users(rows):
    imported = 0
    for row in rows:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (email, name) VALUES ('%s', '%s')" % (row["email"], row["name"])
        )
        conn.commit()
        imported += 1

    return imported


def import_with_lookup(rows):
    for row in rows:
        cur = conn.cursor()
        cur.execute("SELECT id FROM companies WHERE name = '%s'" % row["company"])
        company = cur.fetchone()
        cur.execute(
            "INSERT INTO users (email, company_id) VALUES ('%s', %s)"
            % (row["email"], company[0])
        )
        conn.commit()
