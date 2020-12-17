"""
This module is the backend of the project Restaurant management system developed by Somdev Behera and Soumya Ranjan
Barik. This module is developed to connect the main program to the MySql database. This module uses mysql.connector
package in order to make connection to the main MySql database where it stores the actual user data.

"""
# importing the mysql.connector package

import mysql.connector as mysql

my_con = mysql.connect(host='localhost', user='root', passwd='Rpmgetingear1', db='datacom',
                       auth_plugin='mysql_native_password')

if my_con.is_connected():
    print('Successful')

cur = my_con.cursor()


def data_insert(data1, data2, data3, data4, data5, data6, data7):
    """This method in this module collects the mentioned parameters from the frontend program and then inserts the same
    to the MySql table"""

    try:
        var = 'insert into restaurant(bill_no, customer_name, cust_contact, date,item,quantity, per_cost) values({},' \
              '\'{}\',' \
              '{},{},\'{}\',{},{})'.format(
               data1, data2, data3, data4, data5, data6, data7)

        cur.execute(var)

    except Exception as e:
        print(e)

    my_con.commit()
