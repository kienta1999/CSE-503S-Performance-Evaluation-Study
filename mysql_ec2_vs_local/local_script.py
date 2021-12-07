import pymysql
import pymysql.cursors
import time

print('---------------------------------------------------------')
print('Local Laptop')
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             database='stress_test',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Create a new table
        sql = "CREATE TABLE IF NOT EXISTS `users2` (`id` int(11) NOT NULL AUTO_INCREMENT, \
            `name` varchar(255) NOT NULL, PRIMARY KEY (`id`))"
        cursor.execute(sql)

        sql = "INSERT INTO `users2` (`name`) VALUES (%s)"
        cursor.execute(sql, ('Kien Ta', ))
        
        sql = "INSERT INTO `users2` (`name`) VALUES (%s)"
        cursor.execute(sql, ('Anh Le', ))
        
        sql = "INSERT INTO `users2` (`name`) VALUES (%s)"
        cursor.execute(sql, ('Quan Khuc', ))

        sql = "INSERT INTO `users2` (`name`) VALUES (%s)"
        cursor.execute(sql, ('Ngoc Trinh', ))
    connection.commit()

    # 1000 INSERT
    begin = time.time()
    with connection.cursor() as cursor:
        for i in range(1000):
            c = chr(ord('a') + i % 26)
            sql = "INSERT INTO `users2` (`name`) VALUES (%s)"
            cursor.execute(sql, (c, ))
    connection.commit()
    print(f'Total time for 1000 INSERT: {time.time() - begin}')

    # 1000 SELECT
    begin = time.time()
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `users2` WHERE `name` = %s"
        for i in range(1000):
            cursor.execute(sql, ('c',))
    connection.commit()
    print(f'Total time for 1000 SELECT: {time.time() - begin}')

    # 1000 UPDATE
    begin = time.time()
    with connection.cursor() as cursor:
        sql = "UPDATE `users2` SET `name` = %s WHERE `name` = %s"
        for i in range(1000):
            cursor.execute(sql, ('aaaaaaaa', 'a'))
    connection.commit()
    print(f'Total time for 1000 UPDATE: {time.time() - begin}')

    # 1000 DELETE
    begin = time.time()
    with connection.cursor() as cursor:
        sql = "DELETE FROM `users2` WHERE `name` = %s"
        for i in range(1000):
            cursor.execute(sql, ('b', ))
    connection.commit()
    print(f'Total time for 1000 DELETE: {time.time() - begin}')