import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
from langdetect import detect

# Constants for colors and fonts
BG_COLOR = "#f0f0f0"  # Light gray background
BUTTON_COLOR = "#0078d7"  # Blue for buttons
TEXT_COLOR = "#000000"  # Black text
FONT = ("Consolas", 12)  # Monospaced font (like terminal)

def translate_text():
    """
    Translates text automatically based on the detected language.
    """
    text = text_input.get("1.0", "end-1c").strip()  # Get text from the input text box
    if not text:
        messagebox.showwarning("Input Error", "Please enter some text to translate.")
        return

    try:
        # Detect the language of the input text
        detected_lang = detect(text)

        # Translate based on detected language
        if detected_lang == 'en':
            translated_text = GoogleTranslator(source='en', target='de').translate(text)
        elif detected_lang == 'de':
            translated_text = GoogleTranslator(source='de', target='en').translate(text)
        else:
            messagebox.showwarning("Language Error", "Only English and German are supported.")
            return
        
        text_output.delete("1.0", "end")  # Clear the output text box
        text_output.insert("1.0", translated_text)  # Insert translated text
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")

def clear_fields():
    """
    Clears both the input and output text boxes.
    """
    text_input.delete("1.0", "end")
    text_output.delete("1.0", "end")

def exit_app():
    """
    Exits the application.
    """
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Professional Translator Bot | Ziad Tamer")
root.geometry("600x500+435+170")
root.resizable(True, True)  # Allow window resizing
root.configure(bg=BG_COLOR)

# Input text box
input_label = ttk.Label(root, text="Enter text to translate:", font=FONT, background=BG_COLOR)
input_label.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 0))

text_input = tk.Text(root, height=5, width=50, font=FONT, wrap="word", bg="white", fg=TEXT_COLOR)
text_input.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))

# Output text box
output_label = ttk.Label(root, text="Translated text:", font=FONT, background=BG_COLOR)
output_label.grid(row=2, column=0, sticky="w", padx=10, pady=(10, 0))

text_output = tk.Text(root, height=5, width=50, font=FONT, wrap="word", bg="white", fg=TEXT_COLOR)
text_output.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))

# Buttons frame at the bottom
button_frame = ttk.Frame(root)
button_frame.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

translate_button = ttk.Button(
    button_frame,
    text="Translate",
    command=translate_text,
    style="Blue.TButton"
)
translate_button.pack(side="left", padx=5, expand=True)

clear_button = ttk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    style="Blue.TButton"
)
clear_button.pack(side="left", padx=5, expand=True)

exit_button = ttk.Button(
    button_frame,
    text="Exit",
    command=exit_app,
    style="Blue.TButton"
)
exit_button.pack(side="left", padx=5, expand=True)

# Configure grid weights for resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(3, weight=1)

# Custom button style
style = ttk.Style()
style.configure("Blue.TButton", font=FONT, background=BUTTON_COLOR, foreground=TEXT_COLOR, borderwidth=0)
style.map("Blue.TButton", background=[("active", "#005bb5")])  # Darker blue on hover

# Run the application
root.mainloop()