import tkinter as tk
from tkinter import messagebox, scrolledtext
from hyphenation import hyphenate_text

def process_text():
    """
    Обробка введеного тексту і додавання переносів.
    """
    input_text = text_input.get("1.0", tk.END).strip()
    
    if not input_text:
        messagebox.showwarning("Попередження", "Введіть текст для переносу!")
        return
    
    try:
        result = hyphenate_text(input_text)
        result_output.config(state=tk.NORMAL)  
        result_output.delete("1.0", tk.END)   
        result_output.insert(tk.END, result)  
        result_output.config(state=tk.DISABLED)  
    except Exception as e:
        messagebox.showerror("Помилка", f"Сталася помилка: {str(e)}")

root = tk.Tk()
root.title("Перенос слів та речень")
root.geometry("800x600")
root.configure(bg="#30336b")  

def create_gradient_button(parent, text, command):
    button = tk.Button(parent, text=text, command=command, font=("Arial", 14, "bold"),
                       fg="white", bg="#e17055", activebackground="#d63031",
                       relief=tk.RAISED, bd=4, padx=20, pady=10)
    return button

title_label = tk.Label(
    root, text="✨ Перенос слів та речень ✨", 
    font=("Comic Sans MS", 24, "bold"), 
    bg="#30336b", fg="#f5f6fa"
)
title_label.pack(pady=20)

text_input_label = tk.Label(root, text="📝 Введіть текст:", font=("Arial", 14, "italic"), bg="#30336b", fg="#f5f6fa")
text_input_label.pack()

text_input = scrolledtext.ScrolledText(root, height=7, width=80, font=("Arial", 14), wrap=tk.WORD, bg="#f8a5c2", fg="#2d3436")
text_input.pack(pady=10)

process_button = create_gradient_button(root, "🔄 Обробити", process_text)
process_button.pack(pady=20)

result_label = tk.Label(root, text="📋 Результат з переносами:", font=("Arial", 14, "italic"), bg="#30336b", fg="#f5f6fa")
result_label.pack()

result_output = scrolledtext.ScrolledText(root, height=7, width=80, font=("Arial", 14), wrap=tk.WORD, state=tk.DISABLED, bg="#74b9ff", fg="#2d3436")
result_output.pack(pady=10)

footer_label = tk.Label(
    root, text="🔧 Розроблено з ❤️ на Python та Tkinter", 
    font=("Arial", 12, "italic"), bg="#30336b", fg="#f5f6fa"
)
footer_label.pack(side=tk.BOTTOM, pady=20)

root.mainloop()
