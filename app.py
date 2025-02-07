# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети
"""
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
"""


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)  # Отправка кода ответа
        self.send_header(
            "Content-type", "text/html"
        )  # Отправка типа данных, который будет передаваться
        self.end_headers()
        with open("catalog/templates/catalog/contact.html", "r", encoding="utf-8") as file:
            app = file.read()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(app, "utf-8"))  # Тело ответа


"""
            Метод для обработки входящих GET-запросов
"""
if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
