import pymysql


def connectdb():
    connection = pymysql.connect(
        host='b7nqmihdkndqvnpxnpa5-mysql.services.clever-cloud.com',
        user='uwr9q2b1nl8cm0go',
        password='vtJCjFuCK5o3NUJfRDlO',
        db='b7nqmihdkndqvnpxnpa5',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
