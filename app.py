import pymysql
import streamlit as bel
import connectmysql as conn

bel.title('Hello, world')

connection = conn.connectdb()
cursor = connection.cursor()
# อ่านข้อมูลจากตาราง database


def read_person():
    cursor.execute('SELECT * FROM person')
    persons = cursor.fetchall()
    return persons


def add_person(fullname, email, age):
    try:
        cursor.execute(
            'INSERT INTO person (fullname, email, age) VALUES (%s, %s, %s)',
            (fullname, email, age)
        )
        connection.commit()
        bel.success('Add person successfully')

        # bel.markdown('click [link](?menu=Read) to view the list of person')
        bel.markdown(
            """<a href="?menu=Read" target="_self">click me</a> to view the list of person """, unsafe_allow_html=True)
        # bel.experimental_set_query_params(menu="Read")
        # # if status:
        # bel.experimental_rerun()
        # bel.experimental_get_query_params(menu == "Read")
    except pymysql.Error:
        connection.rollback()
        bel.error('Error create persom : {pymysql.Error}')


def edit_person(id, fullname='', email='', age=0):
    try:
        # if fullname:
        cursor.execute(
            'UPDATE person SET fullname = %s, email = %s, age = %s WHERE id = %s',
            (fullname, email, age, id)
        )
        connection.commit()
        bel.success('Update person successfully')
        bel.markdown(
            """<a href="?menu=Read" target="_self">click me</a> to view the list of person """, unsafe_allow_html=True)
        # elif
    except pymysql.Error:
        connection.rollback()
        bel.error('Error create persom : {pymysql.Error}')


def delete_person(id):
    try:
        # if fullname:
        cursor.execute(
            'DELETE FROM person WHERE id = %s', (id)
        )
        connection.commit()
        bel.success('Delete person successfully')
        bel.markdown(
            """<a href="?menu=Read" target="_self">click me</a> to view the list of person """, unsafe_allow_html=True)
        # elif
    except pymysql.Error:
        connection.rollback()
        bel.error('Error create persom : {pymysql.Error}')


# main nenu
menu = bel.sidebar.selectbox(
    'Menu', ['Read', 'Create', 'Update', 'Delete'])

if menu == "Read":
    bel.subheader('Read_Person')
    persons = read_person()

    # check persons is not null
    if persons:
        table_data = [["ID", "Full Name", "Email", "Age", "Edit", "Delete"]]
        for person in persons:
            # edit_link = bel.button(f"[Edit {person['id']}] (#{person['id']}))"
            # edit_link = bel.button(f"[Delete {person['id']}] (#{person['id']}))"
            edit_link = f"[Edit {person['id']}]"
            delete_link = f"[Delete {person['id']}]"
            row = [
                person['id'],
                person['fullname'],
                person['email'],
                person['age'],
                edit_link,
                delete_link
            ]
            # row.append"""(bel.button(f"Edit {person['id']}"))

            table_data.append(row)

            #     [
            #     person['id'],
            #     person['fullname'],
            #     person['email'],
            #     person['age'],
            #     bel.button(f'Edit {person['id']}'):
            # ]
            # )
        bel.table(table_data)
    else:
        bel.write('No data')

elif menu == "Create":
    bel.subheader('Create_Person')
    fullName = bel.text_input('Full Name')
    email = bel.text_input('Email')
    age = bel.number_input('Age', min_value=1, max_value=100)
    # button create
    if bel.button('Create'):
        # Check data
        if fullName and email and age:
            # sql = """INSERT INTO person (fullname, email, age) VALUES (%s, %s, %s)"""
            add_person(fullName, email, age)

        else:
            bel.write('Plases input data')

        #     cursor.execute(
        #         'INSERT INTO person (fullname, email, age) VALUES (%s, %s, %s)',
        #         (fullName, email, age))
        #     connection.commit()
        #     bel.write('Data inserted')
        # else:
        #     bel.write('Data not inserted')
elif menu == "Update":
    bel.subheader('Update data')
    id = bel.number_input('ID', min_value=1)
    fullName = bel.text_input('FullName')
    email = bel.text_input('email')
    age = bel.number_input('Age', min_value=1, max_value=100)

    if bel.button('Update'):
        edit_person(id, fullName, email, age)
    else:
        bel.write('Plases update data')

elif menu == "Delete":
    bel.subheader('Delete')
    id = bel.number_input('ID', min_value=1)

    if bel.button('Delete'):
        delete_person(id)
