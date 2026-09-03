"""
Обёртка над пулом TCP-соединений к внутреннему сервису (самописный клиент).
Берём коннект из пула, шлём запрос, возвращаем. Дёргается из горячего пути.
"""

import socket
import threading

POOL = []
MAX_SIZE = 10


def get_connection(host, port):
    if POOL:
        return POOL.pop()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    return sock


def release_connection(sock):
    if len(POOL) < MAX_SIZE:
        POOL.append(sock)


def send_request(host, port, data):
    sock = get_connection(host, port)
    sock.sendall(data)
    response = sock.recv(1024)
    release_connection(sock)
    return response


def send_many(host, port, messages):
    responses = []
    for msg in messages:
        responses.append(send_request(host, port, msg))
    return responses
