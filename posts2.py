#!/usr/bin/env python3
import sys
import pymysql
import logger
from config import mysql
import csv

conn = None

def open_connection():
    global conn
    try:
        if (conn is None or not conn.open):
            conn = pymysql.connect(mysql['host'], mysql['user'], mysql['password'], mysql['db'])
    except:
#        logger.error("ERROR: Could not connect to database.")
        sys.exit()

def get_records():
    sql = """
    SELECT post_date, post_title, post_content,
    (SELECT GROUP_CONCAT(wp_terms.name) FROM wp_term_relationships
    LEFT JOIN wp_term_taxonomy ON(wp_term_relationships.term_taxonomy_id = wp_term_taxonomy.term_taxonomy_id)
    LEFT JOIN wp_terms ON(wp_term_taxonomy.term_id = wp_terms.term_id)
    WHERE wp_posts.ID = wp_term_relationships.object_id AND wp_term_taxonomy.taxonomy = 'category') as Category
    FROM wp_posts
    WHERE wp_posts.post_status = 'publish'
    AND wp_posts.post_type = 'post'
    ORDER BY wp_posts.post_date DESC;
    """
    try:
        open_connection()
        with conn.cursor() as cur:
            cur.execute(sql)
            results = cur.fetchall()
            cur.close()
            conn.close()
    except Exception as e:
        print(e)
    finally:
        print ("Query successful.")
        header = ['date', 'title', 'content']
        with open('posts-with-cats-2.csv', 'wt') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(header)
            for result in results:
                csv_writer.writerow(result)


def main():
    get_records()

if __name__ == '__main__':
    main()
