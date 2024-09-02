import tkinter as tk
from tkinter import scrolledtext, filedialog
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import threading
import queue

# Configuration of the model and prompt
template = """
Answer the question below. 
Here is the conversation history: {context}
Question : {question}
Answer:
"""

model = OllamaLLM(model="qwen2:0.5b")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Function to handle the conversation
def handle_conversation(user_input, context):
    try:
        result = chain.invoke({"context": context, "question": user_input})
        return result
    except Exception as e:
        return f"An error occurred: {str(e)}"

# User Interface with Tkinter
class ChatBotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI ChatBot")

        # Allow window resizing
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.context = ""

        # Text area for displaying the conversation
        self.conversation_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
        self.conversation_area.grid(column=0, row=0, padx=10, pady=10, columnspan=3, sticky="nsew")

        # Input field for the user
        self.user_input = tk.Entry(root)
        self.user_input.grid(column=0, row=1, padx=10, pady=10, sticky="ew")
        self.user_input.bind("<Return>", self.on_enter_pressed)

        # Button to send the request
        self.send_button = tk.Button(root, text="Send", command=self.on_send_button_clicked)
        self.send_button.grid(column=1, row=1, padx=10, pady=10, sticky="ew")

        # Button to download the conversation
        self.download_button = tk.Button(root, text="Download", command=self.download_conversation)
        self.download_button.grid(column=2, row=1, padx=10, pady=10, sticky="ew")

        # Configure columns to expand with the window
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=0)
        self.root.grid_columnconfigure(2, weight=0)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=0)

        # Queue to retrieve model results in the background
        self.response_queue = queue.Queue()

        # Asynchronous updating of messages
        self.root.after(100, self.check_queue)

        # Enable full-screen mode
        self.root.bind("<F11>", self.toggle_fullscreen)
        self.root.bind("<Escape>", self.end_fullscreen)
        self.fullscreen = False

    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.root.attributes("-fullscreen", self.fullscreen)
        return "break"

    def end_fullscreen(self, event=None):
        self.fullscreen = False
        self.root.attributes("-fullscreen", False)
        return "break"

    def on_enter_pressed(self, event):
        self.send_message()

    def on_send_button_clicked(self):
        self.send_message()

    def send_message(self):
        user_text = self.user_input.get()
        if user_text.strip() == "exit":
            self.root.quit()
        elif user_text.strip():
            self.display_message("You", user_text)
            self.user_input.delete(0, tk.END)
            
            # Start a thread to handle the conversation
            threading.Thread(target=self.get_ai_response, args=(user_text, self.context)).start()

    def get_ai_response(self, user_text, context):
        ai_response = handle_conversation(user_text, context)
        self.response_queue.put((user_text, ai_response))

    def check_queue(self):
        try:
            while True:
                user_text, ai_response = self.response_queue.get_nowait()
                self.context += f"\nUser: {user_text}\nAI: {ai_response}"
                self.display_message("AI", ai_response)
        except queue.Empty:
            pass
        # Recursive call to check the queue
        self.root.after(100, self.check_queue)

    def display_message(self, sender, message):
        self.conversation_area.configure(state='normal')
        self.conversation_area.insert(tk.END, f"{sender}: {message}\n")
        self.conversation_area.configure(state='disabled')
        self.conversation_area.yview(tk.END)

    def download_conversation(self):
        # Open a dialog to save the file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            # Save the conversation to the selected file
            with open(file_path, "w") as file:
                file.write(self.conversation_area.get("1.0", tk.END).strip())

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotUI(root)
    root.mainloop()
