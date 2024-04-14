from tkinter import PhotoImage, Label, StringVar
import customtkinter


customtkinter.set_appearance_mode("light")
root = customtkinter.CTk()
root.title("MythosAI")
root.geometry("900x700")
root.resizable(False, False)
background_image = PhotoImage(file='mythosAiBckg.png')
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

user_input = StringVar(root)

def get_user_input():
    outputToScreen.insert("end-1c", user_input.get())



outputToScreen = customtkinter.CTkTextbox(root,
                                   width=520,
                                   height=550,
                                   corner_radius=1,
                                   border_width=0,
                                   fg_color="transparent",
                                   text_color="black",
                                   font=("Helvetica", 18),
                                   wrap="word",  # Char default, word, none
                                   activate_scrollbars=True,
                                   scrollbar_button_color="orange",
                                   scrollbar_button_hover_color="red",
                                   state="disabled",).pack(pady=20)

entry = customtkinter.CTkEntry(root,
                               placeholder_text="Type your question here...",
                               width=300,
                               height=50,
                               justify="center",
                               font=("Arial", 18),
                               fg_color="transparent",
                               border_width=0).place(x=250, y=600)
button = customtkinter.CTkButton(root,
                                 width=70,
                                 height=50,
                                 corner_radius=0,
                                 border_width=0,
                                 fg_color="orange",
                                 hover_color="red",
                                 text="Click me!",
                                 command=get_user_input()).place(x=580,y=600)

root.mainloop()
