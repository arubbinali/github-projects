#importing libraries
import tkinter as tk
import customtkinter as ctk
import mysql.connector as sql

#importing password
from passwords import password as key

def dql(frame):
    
    #fixed parameters
    firstx, firsty = 40, 70
    secondx = 770
    thirdx = 1160
    gap = '*' * 256
    password = key()
    button_color = "#313338"

    #functions
    def run_table(event = None):
        global table
        result_textbox.delete(1.0, tk.END)
        current_query_textbox.delete(1.0, tk.END)
        table = table_in.get()
        try:
            if table:
                show_table(table)
            else:
                result_textbox.insert(tk.END, f"{gap}\nInitialization\n{gap}\n\nError: No table given, enter a table name")
        except:
            result_textbox.insert(tk.END, f"{gap}\nInitialization\n{gap}\n\nError: No database given, enter a database name")
        table_in.delete(0, tk.END)

    def run_query(event = None):
        global query
        result_textbox.delete(1.0, tk.END)
        query = query_in.get().strip()
        if query:
            history_textbox.insert(tk.END, query + "\n")
            output(query)
        else:
            result_textbox.insert(tk.END, f"{gap}\nInitialization\n{gap}\n\nError: No query given, enter a query")
        query_in.delete(0, tk.END)

    def clear_history():
        history_textbox.delete(1.0, tk.END)

    def clear_result():
        result_textbox.delete(1.0, tk.END)
        current_query_textbox.delete(1.0, tk.END)

    def get_prev_query(event = None):
        if not query_in.get():
            index = history_textbox.index("end-1c").split(".")[0]
            query_in.insert(tk.END, history_textbox.get(f"{int(index) - 1}.0", f"{index}.end-1c"))

    def clear_query_in(event = None):
        query_in.delete(0, tk.END)

    def show_current_query(query_status):
        if query_status:
            current_query_textbox.delete(1.0, tk.END)
            current_query_textbox.insert(tk.END, query)
        else:
            current_query_textbox.delete(1.0, tk.END)
            current_query_textbox.insert(tk.END, "Invalid query")

    def get_database(event = None):
        global database
        result_textbox.delete(1.0, tk.END)
        current_query_textbox.delete(1.0, tk.END)
        database = database_in.get()
        if database:
            result_textbox.insert(1.0, f"{gap}\nInitialization\n{gap}\n\nDatabase name entered: {database}")
        else:
            result_textbox.insert(tk.END, f"{gap}\nInitialization\n{gap}\n\nError: No database given, enter a database name")
        database_in.delete(0, tk.END)
        
    def show_table(table):
        try:
            connection = sql.connect(
                host = "localhost",
                user = "root",
                password = password,
                database = database
            )
            
            if connection.is_connected():
                result_textbox.insert(tk.END, f"{gap}\nConnected to MySQL Server\n{gap}\n\n")
            
            cursor = connection.cursor()
            cursor.execute(f"select * from {table}")

            if cursor.description:
                fields = [field[0] for field in cursor.description]
                result_textbox.insert(tk.END, "\t\t".join(fields) + "\n")
                result_textbox.insert(tk.END, "-" * 448 + "\n")

                for record in cursor.fetchall():
                    record_data = "\t\t".join([str(item) for item in record])
                    result_textbox.insert(tk.END, record_data + "\n")
            else:
                result_textbox.insert(tk.END, f"Query executed successfully: {query}\n")

            cursor.close()
            connection.close()

        except sql.Error as e:
            result_textbox.delete(1.0, tk.END)
            result_textbox.insert(tk.END, f"{gap}\nConnected to MySQL Server\n{gap}\n\nError: {e}\n")

    def show_databases():
        result_textbox.delete(1.0, tk.END)
        current_query_textbox.delete(1.0, tk.END)
        try:
            connection = sql.connect(
                host = "localhost",
                user = "root",
                password = password,
            )
            
            if connection.is_connected():
                result_textbox.insert(tk.END, f"{gap}\nConnected to MySQL Server\n{gap}\n\n")
            
            cursor = connection.cursor()

            cursor.execute("show databases")

            if cursor.description:
                fields = [field[0] for field in cursor.description]
                result_textbox.insert(tk.END, "\t\t".join(fields) + "\n")
                result_textbox.insert(tk.END, "-" * 448 + "\n")

                for record in cursor.fetchall():
                    record_data = "\t\t".join([str(item) for item in record])
                    result_textbox.insert(tk.END, record_data + "\n")

            cursor.close()
            connection.close()
        except sql.Error as e:
            result_textbox.delete(1.0, tk.END)
            result_textbox.insert(tk.END, f"{gap}\nConnected to MySQL Server\n{gap}\n\nError: {e}\n")

    def show_tables():
        result_textbox.delete(1.0, tk.END)
        current_query_textbox.delete(1.0, tk.END)
        try:
            connection = sql.connect(
                host = "localhost",
                user = "root",
                password = password,
            )
            
            if connection.is_connected():
                result_textbox.insert(tk.END, f"{gap}\nConnected to MySQL Server\n{gap}\n\n")
            
            cursor = connection.cursor()

            try:
                cursor.execute(f"show tables in {database}")
            except:
                result_textbox.insert(tk.END, f"Error: No database selected, enter a database to use first")

            if cursor.description:
                fields = [field[0] for field in cursor.description]
                result_textbox.insert(tk.END, "\t\t".join(fields) + "\n")
                result_textbox.insert(tk.END, "-" * 448 + "\n")

                for record in cursor.fetchall():
                    record_data = "\t\t".join([str(item) for item in record])
                    result_textbox.insert(tk.END, record_data + "\n")

            cursor.close()
            connection.close()
        except sql.Error as e:
            result_textbox.delete(1.0, tk.END)
            result_textbox.insert(tk.END, f"{gap}\nConnected to MySQL Server\n{gap}\n\nError: {e}\n") 

    def output(query):
        try:
            connection = sql.connect(
                host = "localhost",
                user = "root",
                password = password,
                database = database
            )
            if connection.is_connected():
                result_textbox.insert(tk.END, f"{gap}\nConnected to MySQL Server\n{gap}\n\n")
            
            cursor = connection.cursor()

            cursor.execute(query)
            operation = query.split()[0]
            if operation.lower() == "delete":
                table = query.split()[2]
                cursor.execute(query)
            elif operation.lower() == "update":
                table = query.split()[1]
                cursor.execute(query)
            else:
                table = query.split()[2][0 : query.split()[2].find("(")]
                cursor.execute(query)

            cursor.execute(f"select * from {table}")

            if cursor.description:
                fields = [field[0] for field in cursor.description]
                result_textbox.insert(tk.END, "\t\t".join(fields) + "\n")
                result_textbox.insert(tk.END, "-" * 448 + "\n")

                for record in cursor.fetchall():
                    record_data = "\t\t".join([str(item) for item in record])
                    result_textbox.insert(tk.END, record_data + "\n")
            else:
                result_textbox.insert(tk.END, f"Query executed successfully: {query}\n")

            cursor.close()
            connection.close()
            valid_query = True
        except sql.Error as e:
            result_textbox.delete(1.0, tk.END)
            result_textbox.insert(tk.END, f"{gap}\nConnected to MySQL Server\n{gap}\n\nError: {e}\n")
            valid_query = False
        except:
            result_textbox.delete(1.0, tk.END)
            result_textbox.insert(tk.END, f"{gap}\nConnected to MySQL Server\n{gap}\n\nError: No database given, first enter database to use")
            valid_query = False
        show_current_query(valid_query)

    #title
    dml_title = ctk.CTkLabel(frame, text = "Data Query Language Executor", font = ("Roboto", 24), text_color = "#FFD700")
    dml_title.place(x = 590, y = 20)

    #headings
    history_text = ctk.CTkLabel(frame, text = "Query history")
    history_text.place(x = firstx, y = firsty)
    query_text = ctk.CTkLabel(frame, text = "Enter the table to view\n\n\n\n\n\n\n\n\nEnter an insert, update or delete query", justify = "left")
    query_text.place(x = secondx, y = firsty + 10)
    select_database_text = ctk.CTkLabel(frame, text = "Enter database to use")
    select_database_text.place(x = thirdx, y = firsty + 140)
    current_query_text = ctk.CTkLabel(frame, text = "Current query")
    current_query_text.place(x = thirdx, y = firsty)
    result_text = ctk.CTkLabel(frame, text = "Result")
    result_text.place(x = firstx, y = firsty + 260)

    #output
    history_textbox = ctk.CTkTextbox(frame, width = 680, height = 150, state = tk.NORMAL)
    history_textbox.place(x = firstx, y = firsty + 40)
    result_textbox = ctk.CTkTextbox(frame, width = 1460, height = 350, state = tk.NORMAL)
    result_textbox.place(x = firstx, y = firsty + 300)
    current_query_textbox = ctk.CTkTextbox(frame, width = 340, height = 20, state = tk.NORMAL)
    current_query_textbox.place(x = thirdx, y = firsty + 40)

    #entry
    query_in = ctk.CTkEntry(frame, placeholder_text = "Type in your query here", width = 350)
    query_in.place(x = secondx, y = firsty + 173)
    table_in = ctk.CTkEntry(frame, placeholder_text = "Type in the table name here", width = 350)
    table_in.place(x = secondx, y = firsty + 40)
    database_in = ctk.CTkEntry(frame, placeholder_text = "Type in the database name here", width = 350)
    database_in.place(x = thirdx, y = firsty + 173)

    #buttons
    show_table_button = ctk.CTkButton(frame, text = "Show table [ENTER]", command = run_table, width = 200, fg_color=button_color, hover_color="#494D54")
    show_table_button.place(x = secondx, y = firsty + 78)
    run_query_button = ctk.CTkButton(frame, text = "Run query [ENTER]", command = run_query, width = 200, fg_color=button_color, hover_color="#494D54")
    run_query_button.place(x = secondx, y = firsty + 210)
    clear_history_button = ctk.CTkButton(frame, text = "Clear history", command = clear_history, fg_color=button_color, hover_color="#494D54")
    clear_history_button.place(x = firstx, y = firsty + 210)
    clear_result_button = ctk.CTkButton(frame, text = "Clear result window", command = clear_result, fg_color=button_color, hover_color="#494D54")
    clear_result_button.place(x = firstx, y = firsty + 670)
    show_databases_button = ctk.CTkButton(frame, text = "Show databases", command = show_databases, fg_color=button_color, hover_color="#494D54")
    show_databases_button.place(x = firstx + 150, y = firsty + 670)
    show_tables_button = ctk.CTkButton(frame, text = "Show tables", command = show_tables, fg_color=button_color, hover_color="#494D54")
    show_tables_button.place(x = firstx + 301, y = firsty + 670)
    select_database_button = ctk.CTkButton(frame, text = "Select database", command = get_database, fg_color=button_color, hover_color="#494D54")
    select_database_button.place(x = thirdx, y = firsty + 210)

    #key bindings
    query_in.bind('<Return>', run_query)
    query_in.bind('<Up>', get_prev_query)
    query_in.bind('<Down>', clear_query_in)
    table_in.bind('<Return>', run_table)
    database_in.bind('<Return>', get_database)