import customtkinter

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("600x400")
app.title("Skully")

label = customtkinter.CTkLabel(
    app,
    text="💀 Welcome to Skully",
    font=("Arial", 28)
)
label.pack(pady=30)

textbox = customtkinter.CTkTextbox(
    app,
    width=400,
    height=150
)
textbox.pack(pady=20)

button = customtkinter.CTkButton(
    app,
    text="Click Me",
    command=lambda: textbox.insert("end", "Skully says hello!\n")
)
button.pack()

app.mainloop()