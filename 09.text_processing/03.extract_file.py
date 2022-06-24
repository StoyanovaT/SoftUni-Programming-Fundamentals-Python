# file_path = input().split(chr(92))
#
# for i in file_path:
#     if "." in i:
#         (file_name, file_extension) = i.split(".")
#
#         print(f"File name: {file_name}")
#         print(f"File extension: {file_extension}")

# решение на Марио:

def extract_file(data):
    needed_information = data[-1].split('.')
    file_name = needed_information[0]
    extension = needed_information[1]

    print(f"File name: {file_name}")
    print(f"File extension: {extension}")


d = input().split("\\")
extract_file(d)