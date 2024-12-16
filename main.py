def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)  #  с помощью END вставляем полученное слово в конец списка
        task_entry.delete(0, tk.END)  #  очищаем поле для ввода, от нулевого индекса и до конца

def delete_task():
    selected_task = task_listbox.curselection() # с помощью функции **curselection** элемент, на который мы нажмём, будет передавать свой ID, индекс, в переменную  selected_task
    if selected_task:
        task_listbox.delete(selected_task) # удаляем выбранный элемент из списка

def mark_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.itemconfig(selected_task, bg = "HotPink3") # с помощью функции **itemconfig** выполненная задача изменит цвет заливки


import tkinter as tk

root=tk.Tk()

root.title("Трекер задач")

root.configure(background="DarkBlue")

text1 = tk.Label(root, text ="Введите вашу задачу", bg = "DarkBlue", fg="WhiteSmoke")
text1.pack (pady=5)

task_entry = tk.Entry(root, width=30, bg = "MediumVioletRed", fg="WhiteSmoke")
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text = "Добавить задачу", command=add_task)
add_task_button.pack(pady= 5)

delete_task_button = tk.Button(root, text = "Удалить задачу", command= delete_task)
delete_task_button.pack(pady=5)

mark_task_button = tk.Button(root, text = "Задача выполнена", command=mark_task)
mark_task_button.pack(pady=5)

text2 = tk.Label (root, text = "Список задач", bg = "DarkBlue", fg="WhiteSmoke")
text2.pack(pady=10)

task_listbox = tk.Listbox(root, height=10, width=60, bg = "SlateBlue", fg="WhiteSmoke")
task_listbox.pack(pady = 10)

root.mainloop()