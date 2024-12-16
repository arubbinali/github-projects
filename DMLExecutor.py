#importing libraries
import tkinter as tk
import customtkinter as ctk
import mysql.connector as sql

#importing password
from passwords import password as key

def dml(frame):
    
    #fixed parameters
    firstx, firsty = 40, 70
    secondx = 770
    thirdx = 1160
    gap = '*' * 256
    password = key()
    button_color = "#313338"

    #functions
    def run_query():
        global query
        result_textbox.delete(1.0, tk.END)
        query = query_in.get().strip()
        if query:
            history_textbox.insert(tk.END, query + "\n")
            output(query)
        else:
            result_textbox.insert(tk.END, f"{gap}\nConnected to MySQL Server\n{gap}\n\nError: No query given, enter a query")
        query_in.delete(0, tk.END)

    def execute(event = None):
        run_query()

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

    def output(query):
        try:
            connection = sql.connect(
                host = "localhost",
                user = "root",
                password = password
            )
            
            if connection.is_connected():
                result_textbox.insert(tk.END, f"{gap}\nConnected to MySQL Server\n{gap}\n\n")
            
            cursor = connection.cursor()
            cursor.execute(query)

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
        show_current_query(valid_query)

    #title
    dml_title = ctk.CTkLabel(frame, text = "Data Manipulation Language Executor", font = ("Roboto", 24), text_color = "#FFD700")
    dml_title.place(x = 580, y = 20)

    #headings
    history_text = ctk.CTkLabel(frame, text = "Query history")
    query_text = ctk.CTkLabel(frame, text = "Enter a select query")
    current_query_text = ctk.CTkLabel(frame, text = "Current query")
    result_text = ctk.CTkLabel(frame, text = "Result")
    
    current_query_text.place(x = thirdx, y = firsty)
    query_text.place(x = secondx, y = firsty)
    history_text.place(x = firstx, y = firsty)
    result_text.place(x = firstx, y = firsty + 260)

    #output
    history_textbox = ctk.CTkTextbox(frame, width = 680, height = 150, state = tk.NORMAL)
    result_textbox = ctk.CTkTextbox(frame, width = 1460, height = 350, state = tk.NORMAL)
    current_query_textbox = ctk.CTkTextbox(frame, width = 340, height = 20, state = tk.NORMAL)
    
    history_textbox.place(x = firstx, y = firsty + 40)
    result_textbox.place(x = firstx, y = firsty + 300)
    current_query_textbox.place(x = thirdx, y = firsty + 50)

    #entry
    query_in = ctk.CTkEntry(frame, placeholder_text = "Type in your query here", width = 350)
    query_in.place(x = secondx, y = firsty + 50)

    #buttons
    run_query_button = ctk.CTkButton(frame, text = "Run query [ENTER]", command = run_query, width = 200, fg_color=button_color, hover_color="#494D54")
    clear_history_button = ctk.CTkButton(frame, text = "Clear history", command = clear_history, fg_color=button_color, hover_color="#494D54")
    clear_result_button = ctk.CTkButton(frame, text = "Clear result window", command = clear_result, fg_color=button_color, hover_color="#494D54")
    
    run_query_button.place(x = secondx, y = firsty + 100)
    clear_history_button.place(x = firstx, y = firsty + 210)
    clear_result_button.place(x = firstx, y = firsty + 670)

    #key bindings
    query_in.bind('<Return>', execute)
    query_in.bind('<Up>', get_prev_query)
    query_in.bind('<Down>', clear_query_in)