URL = input("Please enter your URL:")
protocol = URL.split("://")[0]
domain_name = URL.split("://")[1].split("/")[0]
folder_structure = URL.split("://")[1].split("/")[1]
file_name = URL.split("://")[1].split("/")[2]
print(f"Protocol: {protocol}"
      f"\nDomain name: {domain_name}"
      f"\nFolder: {folder_structure}"
      f"\nFile: {file_name}")
