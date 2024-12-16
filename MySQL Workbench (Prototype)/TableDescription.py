#importing libraries
import tkinter as tk
import customtkinter as ctk
import mysql.connector as sql

#importing password
from passwords import password as key

def table(frame):
    #fixed parameters
    firstx, secondx, thirdx = 50, 400, 770
    firsty, secondy = 80, 275
    password = key()
    run = True
    tables = []

    #functions
    def initialization():
        global run
        current_status.delete(1.0, tk.END)
        try:
            connection = sql.connect(
                host = "localhost",
                user = "root",
                password = password
            )

            if connection.is_connected():
                frame.after(1000, lambda: current_status.insert(tk.END, "Connected to MySQL server"))
                run = True


        except sql.Error as e:
            databases_menu.configure(values = tables)
            error = str(e)
            current_status.delete(1.0, tk.END)
            frame.after(1000, lambda: current_status.insert(tk.END, f"Couldn't connect to MySQL server\n"))
            frame.after(1050, lambda: current_status.insert(tk.END, f"Error: {error}"))
            run = False

        except:
            current_status.delete(1.0, tk.END)
            frame.after(1000, lambda: current_status.insert(tk.END, f"Couldn't connect to MySQL server\n"))
            run = False

    def get_databases():
        databases = []
        if run:
            try:
                connection = sql.connect(
                    host = "localhost",
                    user = "root",
                    password = password
                )

                cursor = connection.cursor()
                cursor.execute("show databases")
                
                for data in cursor.fetchall():
                    database = "\t\t".join([str(item) for item in data])
                    databases.append(database)

                return databases
            
            except sql.Error as e:
                current_status.delete(1.0, tk.END)
                current_status.insert(tk.END, f"Error: {e}")

    def get_tables(get_database):
        global db, tables
        tables = []
        if run and db:
            try:
                connection = sql.connect(
                    host = "localhost",
                    user = "root",
                    password = password,
                    database = get_database
                )

                cursor = connection.cursor()
                cursor.execute(f"show tables")
                for data in cursor.fetchall():
                    table = "\t\t".join([str(item) for item in data])
                    tables.append(table)

                return tables
            
            except sql.Error as e:
                current_status.delete(1.0, tk.END)
                current_status.insert(tk.END, f"Error: {e}")

    def handle_db_selection(selected):
        global selected_db, db
        selected_db = selected.strip()
        db = True
        tables_menu.set("Select a table")
        tables = get_tables(selected_db)
        tables_menu.configure(values = tables)   

    def show_description(table):
        global selected_table, selected_db
        try:
            all = []
            connection = sql.connect(
                host = "localhost",
                user = "root",
                password = password,
                database = selected_db
            )
            
            selected_table = table
            cursor = connection.cursor()
            cursor.execute(f"describe {selected_table}")
    
            if cursor.description:
                table_description.delete(1.0, tk.END)
                fields = [field[0] for field in cursor.description]
                table_description.insert(tk.END, "\t\t\t".join(fields) + "\n")
                table_description.insert(tk.END, "-" * 445 + "\n")

                for data in cursor.fetchall():
                    line = "\t\t\t".join([str(item) for item in data])
                    table_description.insert(tk.END, f"{line}\n")
                    all.append(line)

            show_table(table)
            return tables

        except sql.Error as e:
            current_status.delete(1.0, tk.END)
            current_status.insert(tk.END, f"Er3ror: {e}")

    def show_table(table):
        global selected_db
        try:
            connection = sql.connect(
                host = "localhost",
                user = "root",
                password = password,
                database = selected_db
            )
                
            cursor = connection.cursor()
            cursor.execute(f"select * from {table}")

            if cursor.description:
                table_textbox.delete(1.0, tk.END)
                fields = [field[0] for field in cursor.description]
                table_textbox.insert(tk.END, "\t\t".join(fields) + "\n")
                table_textbox.insert(tk.END, "-" * 445 + "\n")

                for record in cursor.fetchall():
                    record_data = "\t\t".join([str(item) for item in record])
                    table_textbox.insert(tk.END, record_data + "\n")

            cursor.close()
            connection.close()

        except sql.Error as e:
            table_textbox.delete(1.0, tk.END)
            current_status.delete(1.0, tk.END)
            current_status.insert(tk.END, f"Error: {e}")

    def clear():
        table_description.delete(1.0, tk.END)
        table_textbox.delete(1.0, tk.END)
        databases_menu.set("Select a database")
        tables_menu.set("Select a table")
        tables_menu.configure(values = [])

    #title
    dml_title = ctk.CTkLabel(frame, text = "Table schema viewer", font = ("Roboto", 24), text_color = "#FFD700")
    dml_title.place(x = 620, y = 20)

    #headings
    current_status_text = ctk.CTkLabel(frame, text = "Current status")
    table_description_text = ctk.CTkLabel(frame, text = "Table description")
    table_textbox_text = ctk.CTkLabel(frame, text = "Table")

    current_status_text.place(x = thirdx, y = firsty - 10)
    table_description_text.place(x = firstx, y = secondy - 35)
    table_textbox_text.place(x = firstx, y = secondy + 215)

    #output
    current_status = ctk.CTkTextbox(frame, width = 730, height = 100, state = tk.NORMAL)
    table_description = ctk.CTkTextbox(frame, width = 1450, height = 200, state = tk.NORMAL)
    table_textbox = ctk.CTkTextbox(frame, width = 1450, height = 200, state = tk.NORMAL)

    current_status.place(x = thirdx, y = firsty + 25)
    table_description.place(x = 50, y = secondy)
    table_textbox.place(x = 50, y = secondy + 250)

    #drop downs
    databases_menu = ctk.CTkComboBox(frame, width = 300, values = get_databases(), command = handle_db_selection)
    databases_menu.set("Select a database")
    databases_menu.place(x = firstx, y = firsty)

    tables_menu = ctk.CTkComboBox(frame, width = 300, command = lambda selected_table: show_description(selected_table), values = [])
    tables_menu.set("Select a table")
    tables_menu.place(x = secondx, y = firsty)

    #buttons
    clear_button = ctk.CTkButton(frame, text = "Clear", command = clear, fg_color="#313338", hover_color="#494D54")
    clear_button.place(x = firstx, y = secondy + 465)

    #initialize drop downs
    initialization()