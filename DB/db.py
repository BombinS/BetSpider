#!/bin/usr/env python

import psycopg2

def InitConnection():
    conn = psycopg2.connect(
        host = "localhost",
        port = "5432",
        database="BetSpyder",
        user = "postgres",
        password = "!QAZ1qaz19770517"
    )
    return conn

if __name__ == "__main__":
    conn = InitConnection()
    conn.close()