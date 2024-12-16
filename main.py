#importing libraries
import tkinter as tk
import customtkinter as ctk

#importing modules
from DMLExecutor import dml
from DQLExecutor import dql
from TableDescription import table

#creating main window
window = ctk.CTk()

#configure window settings & appearance
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}+0+0")
window.overrideredirect(True)
ctk.set_appearance_mode("dark")

#fixed parameters
exitx, exity = 1491, 0
returnx, returny, return_text = 1360, 740, "Back [Escape]"
firstx, firsty = 400, 100

#colors
title_bar_color = "#1e1f1c"
main_color = "#272822"
button_color = "#313338"
return_color = "#3c3d3a"

#functions  
def showframe(frame):
    for f in [main_frame, dev_tools, dql_executor, dml_executor, table_description]:
        f.place_forget()
    frame.place(relx = 0, rely = 0.08 if frame != navigation_frame else 0, relwidth = 1, relheight = 0.92 if frame != navigation_frame else 0.08)

    global current_frame
    current_frame = frame
    frame.focus_set()
    
def close_window(event = None):
    window.destroy()

def return_main(event = None):
    showframe(main_frame)

def return_dev_tool_frame(event = None):
    showframe(dev_tools)

def handle_escape(event):
    if current_frame == main_frame:
        close_window()
    elif current_frame == dev_tools:
        return_main()
    elif current_frame == dql_executor or dml_executor or table_description:
        return_dev_tool_frame()

#frames
navigation_frame = ctk.CTkFrame(window, fg_color = title_bar_color)
navigation_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.08)

main_frame = ctk.CTkFrame(window, fg_color = main_color)
main_frame.place(relx = 0, rely = 0.08, relwidth = 1, relheight = 0.92)

dev_tools = ctk.CTkFrame(window)
dql_executor = ctk.CTkFrame(window)
dml_executor = ctk.CTkFrame(window)
table_description = ctk.CTkFrame(window)

#buttons
#navigation - main buttons
dev_tool_button = ctk.CTkButton(navigation_frame, text = "Dev tools", command = lambda:showframe(dev_tools), fg_color=button_color, hover_color = return_color)
dev_tool_button.place(x = 500, y = 35)

#navigation - exit button
exit_button = ctk.CTkButton(navigation_frame, text = "✖", command = close_window, fg_color = title_bar_color, hover_color = "#FF0000", width = 45, height = 33)
exit_button.place(x = exitx, y = exity)

#dev tools - main buttons
dml_executor_button = ctk.CTkButton(dev_tools, text = "DML Executor", command = lambda:showframe(dml_executor), fg_color=button_color, hover_color = return_color)
dql_executor_button = ctk.CTkButton(dev_tools, text = "DQL Executor", command = lambda:showframe(dql_executor), fg_color=button_color, hover_color = return_color)
table_description_button = ctk.CTkButton(dev_tools, text = "Table Description", command = lambda:showframe(table_description), fg_color=button_color, hover_color = return_color)

dml_executor_button.place(x = firstx, y = firsty)
dql_executor_button.place(x = firstx + 300, y = firsty)
table_description_button.place(x = firstx + 600, y = firsty)

#dev tools - back buttons
back_dev_tool_button = ctk.CTkButton(dev_tools, text = return_text, command = lambda:showframe(main_frame), fg_color=button_color, hover_color = return_color)
back_dql_executor_button = ctk.CTkButton(dql_executor, text = return_text, command = lambda:showframe(dev_tools), fg_color=button_color, hover_color = return_color)
back_dml_exectuor_button = ctk.CTkButton(dml_executor, text = return_text, command = lambda:showframe(dev_tools), fg_color=button_color, hover_color = return_color)
back_table_description_button = ctk.CTkButton(table_description, text = return_text, command = lambda:showframe(dev_tools), fg_color=button_color, hover_color = return_color)

back_dev_tool_button.place(x = returnx, y = returny)
back_dql_executor_button.place(x = returnx, y = returny)
back_dml_exectuor_button.place(x = returnx, y = returny)
back_table_description_button.place(x = returnx, y = returny)

#calling module file
dml(dml_executor)
dql(dql_executor)
table(table_description)

#set current frame
current_frame = main_frame

#key bindings
window.bind('<Escape>', handle_escape)

#run event controller
window.mainloop()