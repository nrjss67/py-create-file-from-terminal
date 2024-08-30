import sys
import os
import datetime


def content_writer(path: str) -> None:
    with open(path, "w") as new_file:
        content_line = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line_counter = 1
        while "stop" not in content_line:
            new_file.write(content_line + "\n")
            content_line = (f"{str(line_counter)} "
                            f"{input("Enter content line: ")}")
            line_counter += 1


def create_app() -> None:
    command = sys.argv
    if "-d" in command and "-f" in command:
        file_name = None
        part_of_dir = []
        for part in sys.argv[2:]:
            if ("." not in part
                    and "-" not in part):
                part_of_dir.append(part)
            if "." in part:
                file_name = part

        joined_path = os.path.join(*part_of_dir)
        os.makedirs(joined_path, exist_ok=True)

        content_writer(joined_path + "/" + file_name)
        return

    flag = command[1]
    if flag == "-d":
        path = os.path.join(*command[2:])
        os.makedirs(path, exist_ok=True)
    if flag == "-f":
        content_writer(f"./{command[2]}")


if __name__ == "__main__":
    create_app()
