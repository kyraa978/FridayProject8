import sqlite3
import tkinter as tk

def create_database():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            feedback TEXT
        )
    ''')
    conn.commit()
    conn.close()

def submit_feedback():
    name = name_entry.get()
    email = email_entry.get()
    feedback = feedback_text.get("1.0", "end-1c")

    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)", (name, email, feedback))
    conn.commit()
    conn.close()

    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    feedback_text.delete("1.0", tk.END)

    message_label.config(text="Feedback submitted successfully!")

def view_feedback():
    password = input("Enter password: ")
    if password == "your_password":  # Replace "your_password" with your desired password
        conn = sqlite3.connect('feedback.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM feedback")
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            print(f"ID: {row[0]}\nName: {row[1]}\nEmail: {row[2]}\nFeedback: {row[3]}\n\n")
    else:
        print("Incorrect password.")

window = tk.Tk()
window.title("Customer Feedback")


name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

email_label = tk.Label(window, text="Email:")
email_label.pack()
email_entry = tk.Entry(window)
email_entry.pack()

feedback_label = tk.Label(window, text="Feedback:")
feedback_label.pack()
feedback_text = tk.Text(window, height=5)
feedback_text.pack()


submit_button = tk.Button(window, text="Submit", command=submit_feedback)
submit_button.pack()


view_button = tk.Button(window, text="View Feedback", command=view_feedback)
view_button.pack()


message_label = tk.Label(window, text="")
message_label.pack()


create_database()

window.mainloop()