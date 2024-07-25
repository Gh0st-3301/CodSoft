import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        self.expression = ""
        
        self.input_text = tk.StringVar()
        
        # Create the display
        self.input_field = tk.Entry(root, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=4, width=14, borderwidth=4)
        self.input_field.grid(row=0, column=0, columnspan=4)
        
        # Create the buttons
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+', 
            'C'
        ]
        
        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(root, text=button, padx=20, pady=20, command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
    
    def on_button_click(self, char):
        if char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        elif char == 'C':
            self.expression = ""
        else:
            self.expression += str(char)
        self.input_text.set(self.expression)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()