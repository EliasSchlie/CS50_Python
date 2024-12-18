def main():
    name = input("File name: ")
    name = name.strip()
    name = name.split(".")
    extension = name[-1]
    extension = extension.lower()
    output_ftype(extension)

def output_ftype(e):
    match e:
        case "py":
            print("text/x-python")
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

main()