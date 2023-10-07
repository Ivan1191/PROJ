import pymysql
import time

# 資料庫設定
db_settings = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "alex890506",
    "db": "eline",
    "charset": "utf8"
}


def addUser(id, name):
    try:
        # 建立Connection物件
        conn = pymysql.connect(**db_settings)

        # 建立Cursor物件
        with conn.cursor() as cursor:
            # 新增資料SQL語法
            command = "INSERT INTO user(idUser, UserName)VALUES(%s, %s)"

            cursor.execute(command, (id, name))

            # 儲存變更
            conn.commit()

        # 關閉connection
        conn.close()

    except Exception as ex:
        print(ex)


def addChattingObject(name, userId):
    try:
        # 建立Connection物件
        conn = pymysql.connect(**db_settings)

        # 建立Cursor物件
        with conn.cursor() as cursor:
            # 新增資料SQL語法
            command = "INSERT INTO chatting_object(objectName, User_idUser)VALUES(%s, %s)"

            cursor.execute(command, (name, userId))

            # 儲存變更
            conn.commit()

        # 關閉connection
        conn.close()

    except Exception as ex:
        print(ex)


def addRecord(id):
    try:
        # 建立Connection物件
        conn = pymysql.connect(**db_settings)

        # 建立Cursor物件
        with conn.cursor() as cursor:
            # 新增資料SQL語法
            command = "INSERT INTO record(recordDate, chatting_object_idchatting_object)VALUES(%s, %s)"
            result = time.localtime()
            datetime = "{}-{}-{} {}:{}:{}".format(result.tm_year, result.tm_mon,
                                                  result.tm_mday, result.tm_hour, result.tm_min, result.tm_sec)
            print(datetime)
            cursor.execute(command, (datetime, id))

            # 儲存變更
            conn.commit()

        # 關閉connection
        conn.close()

    except Exception as ex:
        print(ex)


def selectUserByUserId(id):
    try:
        # 建立Connection物件
        conn = pymysql.connect(**db_settings)

        # 建立Cursor物件
        with conn.cursor() as cursor:
            # 新增資料SQL語法
            command = "SELECT * FROM user WHERE idUser = (%s)"

            cursor.execute(command, (id))
            print(cursor.fetchone())

            # 儲存變更
            conn.commit()

        # 關閉connection
        conn.close()

    except Exception as ex:
        print(ex)

# USER ID 搜尋得分


def getRecordScore(id, ScoreName):
    try:
        # 建立Connection物件
        conn = pymysql.connect(**db_settings)

        # 建立Cursor物件
        with conn.cursor() as cursor:
            # 新增資料SQL語法
            command = "SELECT " + ScoreName + \
                " FROM record WHERE idrecord = (%s)"

            cursor.execute(command, (id))

            # 儲存變更
            conn.commit()

        # 關閉connection
        conn.close()

        return cursor.fetchone()

    except Exception as ex:
        print(ex)


def selectChattingObjectByUserId(id):
    try:
        # 建立Connection物件
        conn = pymysql.connect(**db_settings)

        # 建立Cursor物件
        with conn.cursor() as cursor:
            # 新增資料SQL語法
            command = "SELECT * FROM chatting_object WHERE User_idUser = (%s)"

            cursor.execute(command, (id))
            print(cursor.fetchall())

            # 儲存變更
            conn.commit()

        # 關閉connection
        conn.close()

    except Exception as ex:
        print(ex)


# addRecord("8")
# selectUserByUserId("2")
# selectChattingObjectByUserId("1")
# score = getRecordScore("4", "calltime")
# print(score)
