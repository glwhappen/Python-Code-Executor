import tkinter as tk
import threading
import sys
import io

def execute_code():
    code = code_entry.get('1.0', tk.END)
    output_entry.delete('1.0', tk.END)
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    try:
        exec(code)
    except Exception as e:
        output_entry.insert(tk.END, f"An error occurred: {e}")
    else:
        sys.stdout = old_stdout
        output = redirected_output.getvalue()
        output_entry.insert(tk.END, output)

def thread_it(func, *args):
    '''创建一个线程'''
    t = threading.Thread(target=func, args=args, daemon=True)
    # t.setDaemon(True)
    t.start()

root = tk.Tk()
root.title('Python Code Executor')

code_entry = tk.Text(root, height=10)
code_entry.pack(padx=10, pady=10)

execute_button = tk.Button(root, text='Execute', command=lambda: thread_it(execute_code))
execute_button.pack(padx=10, pady=10)

output_entry = tk.Text(root, height=20)
output_entry.pack(padx=10, pady=10)

root.mainloop()
