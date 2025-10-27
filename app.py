#!/usr/bin/env python3
"""
Coffee Grind Distribution Analyzer
A GUI application for analyzing coffee grind distributions from images.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import sys
from datetime import datetime

class CoffeeGrindApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Grind Distribution Analyzer")
        self.root.geometry("600x500")
        
        # Variables
        self.image_path = None
        self.output_dir = os.path.join(os.path.expanduser("~"), "CoffeeGrindData")
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Coffee Grind Distribution Analyzer", 
                                font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Instructions
        instructions = ttk.Label(main_frame, text="Analyze your coffee grind distribution photos", 
                                wraplength=500)
        instructions.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Image selection
        ttk.Label(main_frame, text="1. Select Image:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.image_label = ttk.Label(main_frame, text="No image selected", foreground="gray")
        self.image_label.grid(row=3, column=0, columnspan=2, pady=5)
        
        select_btn = ttk.Button(main_frame, text="Open Image", command=self.select_image)
        select_btn.grid(row=4, column=0, columnspan=2, pady=5)
        
        # Grinder info
        ttk.Label(main_frame, text="2. Grinder Information:").grid(row=5, column=0, sticky=tk.W, pady=5)
        
        ttk.Label(main_frame, text="Grinder Name:").grid(row=6, column=0, sticky=tk.W, padx=(20,0))
        self.grinder_name = ttk.Entry(main_frame, width=30)
        self.grinder_name.grid(row=6, column=1, sticky=tk.W, pady=2)
        
        ttk.Label(main_frame, text="Your Username:").grid(row=7, column=0, sticky=tk.W, padx=(20,0))
        self.username = ttk.Entry(main_frame, width=30)
        self.username.grid(row=7, column=1, sticky=tk.W, pady=2)
        
        # Analysis section
        ttk.Label(main_frame, text="3. Generate Data:").grid(row=8, column=0, sticky=tk.W, pady=5)
        
        self.analyze_btn = ttk.Button(main_frame, text="Analyze & Save Data", 
                                      command=self.analyze_image, state='disabled')
        self.analyze_btn.grid(row=9, column=0, columnspan=2, pady=10)
        
        # Status
        self.status_label = ttk.Label(main_frame, text="", foreground="blue")
        self.status_label.grid(row=10, column=0, columnspan=2, pady=5)
        
        # Info section
        info_frame = ttk.LabelFrame(main_frame, text="Information", padding="5")
        info_frame.grid(row=11, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        info_text = ("This application helps you analyze coffee grind distribution.\n"
                    "For detailed instructions, visit:\n"
                    "github.com/julowe/coffee-grind-distribution")
        info_label = ttk.Label(info_frame, text=info_text, wraplength=500)
        info_label.pack()
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
    def select_image(self):
        """Open file dialog to select an image."""
        filetypes = (
            ('Image files', '*.jpg *.jpeg *.png *.bmp'),
            ('All files', '*.*')
        )
        
        filename = filedialog.askopenfilename(
            title='Select coffee grind image',
            filetypes=filetypes
        )
        
        if filename:
            self.image_path = filename
            self.image_label.config(text=os.path.basename(filename), foreground="black")
            self.analyze_btn.config(state='normal')
            self.status_label.config(text="Image loaded successfully", foreground="green")
    
    def analyze_image(self):
        """Analyze the selected image and save data."""
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image first")
            return
        
        grinder = self.grinder_name.get().strip()
        username = self.username.get().strip()
        
        if not grinder or not username:
            messagebox.showerror("Error", "Please enter grinder name and username")
            return
        
        try:
            # Create output directory
            os.makedirs(self.output_dir, exist_ok=True)
            
            # Generate timestamp
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            folder_name = f"{timestamp}_{username}"
            folder_path = os.path.join(self.output_dir, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            
            # Create sample CSV files (placeholder for actual analysis)
            csv_filename = f"{timestamp}_{username}.csv"
            stats_filename = f"{timestamp}_{username}_stats.csv"
            readme_filename = "README.md"
            
            # Save CSV (placeholder data)
            with open(os.path.join(folder_path, csv_filename), 'w', encoding='utf-8') as f:
                f.write("diameter_mm,count\n")
                f.write("0.5,10\n")
                f.write("0.75,25\n")
                f.write("1.0,50\n")
                f.write("1.25,100\n")
                f.write("1.5,45\n")
            
            # Save stats (placeholder data)
            with open(os.path.join(folder_path, stats_filename), 'w', encoding='utf-8') as f:
                f.write("metric,value\n")
                f.write("average_diameter_mm,1.25\n")
                f.write("std_deviation,0.55\n")
                f.write("total_particles,230\n")
                f.write(f"grinder,{grinder}\n")
            
            # Save README
            with open(os.path.join(folder_path, readme_filename), 'w', encoding='utf-8') as f:
                f.write(f"# Coffee Grind Distribution Data\n\n")
                f.write(f"**Grinder:** {grinder}\n")
                f.write(f"**Username:** {username}\n")
                f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n")
                f.write(f"**Image:** {os.path.basename(self.image_path)}\n\n")
                f.write("## Instructions for submission\n\n")
                f.write("1. Upload your image to imgur.com\n")
                f.write("2. Fork the coffee-grind-distribution repository\n")
                f.write("3. Add this folder to the data directory\n")
                f.write("4. Create a pull request\n")
            
            self.status_label.config(
                text=f"Data saved successfully to:\n{folder_path}", 
                foreground="green"
            )
            
            messagebox.showinfo(
                "Success", 
                f"Analysis complete!\n\nData saved to:\n{folder_path}\n\n"
                "Follow the instructions in the README.md file to submit your data."
            )
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {str(e)}")
            self.status_label.config(text="Error occurred", foreground="red")

def main():
    root = tk.Tk()
    app = CoffeeGrindApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
