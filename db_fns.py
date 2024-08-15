import sqlite3

conn = sqlite3.connect('jobs')
cur = conn.cursor()


def select(team):
    res = cur.execute(f'select job_title from jobs where team = "{team}"')
    return res.fetchall()


def insert(jobs):
    cur.executemany(f'insert into jobs values (?, ?)', jobs)
    conn.commit()
