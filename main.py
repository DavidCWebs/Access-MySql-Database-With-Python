#!/usr/bin/env python3
import sys
import pymysql
import logger
from config import mysql
import csv

conn = None
print("{}, {}, {}".format(mysql['host'], mysql['user'], mysql['password']))

def open_connection():
    global conn
    try:
        if (conn is None or not conn.open):
            conn = pymysql.connect(mysql['host'], mysql['user'], mysql['password'], mysql['db'])
    except:
#        logger.error("ERROR: Could not connect to database.")
        sys.exit()

def get_records():
    try:
        open_connection()
        with conn.cursor() as cur:
            sql = "SELECT post_title, post_content FROM wp_posts WHERE post_type = 'chapter'"
            cur.execute(sql)
            results = cur.fetchall()
            cur.close()
            conn.close()
    except Exception as e:
        print(e)
    finally:
        print ("Query successful.")
        header = ['title', 'content']
        with open('chapters.csv', 'wt') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(header)
            for result in results:
                csv_writer.writerow(result)


def main():
    get_records()

if __name__ == '__main__':
    main()
