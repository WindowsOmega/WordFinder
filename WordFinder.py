# To find
file = input("What file do we have here? ")

# Word Finder
query = input("What will you like me to find? ")
if "define" in query:
    import webbrowser
    url = "https://www.google.com/search?q="
    webbrowser.open_new_tab(url + query)

else:
    with open(file, 'r') as file_fr:
        for line_number, line in enumerate(file_fr, start=1): 
            if query in line:
                print(f"'{query}' found in line {line_number}: {line.strip()}")

import time
time.sleep(100)