"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2


def create_suppliers_table(cur):
    """Создает таблицу suppliers."""
    with psycopg2.connect(host="localhost", database="north", user="postgres", password="Ghjcnj038") as conn:
        with conn.cursor() as cur:  # делает commit после выполнения
            cur.executemany("INSERT INTO user_acoount VALUES (%s, %s)", [(9, 'John')])
            cur.execute("SELECT * FROM user_acoount")

            rows = cur.fetchall()
            for row in rows:
                print(row)

    conn.close()
