import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter root window (hidden)
root = tk.Tk()
root.withdraw()

# Ask the user to select an Excel file using a file dialog
file_path = filedialog.askopenfilename(title="Select Excel File", filetypes=[("Excel Files", "*.xlsx")])

# Check if the user canceled the dialog
if not file_path:
    print("No Excel file selected. Exiting.")
else:
    try:
        # Ask the user to enter the sheet name
        selected_sheet = input("Enter the sheet name: ")

        # Read the Excel file using pandas with the specified sheet name
        df = pd.read_excel(file_path, sheet_name=selected_sheet)

        # List the available column names in the selected sheet
        column_names = df.columns
        print(f"Available columns in the sheet '{selected_sheet}':")
        for idx, column in enumerate(column_names):
            print(f"{idx + 1}. {column}")

        # Ask the user to choose a column
        selected_column_index = int(input("Enter the column number (e.g., 1): ")) - 1

        if 0 <= selected_column_index < len(column_names):
            selected_column = column_names[selected_column_index]

            # Ask the user for the save location using a file dialog
            output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

            # Check if the user canceled the dialog
            if not output_file:
                print("No file selected for saving. Exiting.")
            else:
                # Extract the selected column data and write it to the selected text file
                with open(output_file, "w") as file:
                    for item in df[selected_column]:
                        file.write(str(item) + "\n")

                print(f"Contents of column '{selected_column}' from '{file_path}' (sheet '{selected_sheet}') have been extracted and saved to '{output_file}'.")
        else:
            print("Invalid column number selected.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Close the Tkinter root window
root.destroy()
