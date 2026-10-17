import os
from http.server import BaseHTTPRequestHandler, HTTPServer


def get_student_info():
    name = os.getenv("STUDENT_NAME", "Baimurat")
    surname = os.getenv("STUDENT_SURNAME", "Akbiyev")
    group = os.getenv("STUDENT_GROUP", "IT2-2306")
    student_id = os.getenv("STUDENT_ID", "38150")

    return (
        "================================\n"
        "DevOps Student Application\n"
        "================================\n"
        f"Name: {name}\n"
        f"Surname: {surname}\n"
        f"Group: {group}\n"
        f"Student ID: {student_id}\n"
        "\nApplication is running successfully!\n"
    )


class StudentHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = get_student_info()
        data = message.encode("utf-8")

        self.send_response(200)
        self.send_header(
            "Content-Type",
            "text/plain; charset=utf-8"
        )
        self.send_header(
            "Content-Length",
            str(len(data))
        )
        self.end_headers()

        self.wfile.write(data)


if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", "8000"))

    print(get_student_info(), flush=True)
    print(f"Server started on port {port}", flush=True)

    server = HTTPServer(
        ("0.0.0.0", port),
        StudentHandler
    )

    server.serve_forever()
