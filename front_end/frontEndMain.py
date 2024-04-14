import customtkinter

root = customtkinter.CTk()

root.title("MythosAI")
root.geometry("700x500")

entry = customtkinter.CTkEntry(root, placeholder_text="CTkEntry", width=250, height=50).place(relx=.3, rely=.85)

root.mainloop()