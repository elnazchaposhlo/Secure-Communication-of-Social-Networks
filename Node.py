#!/usr/bin/python3

import socket
import threading


class Node:
    def __init__(self, name, children=None, parent=None):
        self.name = name

        self.children = []
        if children is not None:
            if type(children) is not list: children = [children]
            for node in children:
                self.children.append(node)

        if parent is None:
            self.parent = None
        else:
            self.parent = parent

    def populate_children(self, node):
        self.children.append(node)

    def populate_parent(self, node):
        self.parent = node

    def get_rev_children(self):
        children = self.children[:]
        children.reverse()
        return children

    # Create Socket connection
    def create_socket(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:

            if self.children:
                # get host's name and then IP
                host_name = socket.gethostname()
                # host_ip = socket.gethostbyname(host_name)

                host_ip = '127.0.0.1'
                port = 49152 + int(self.name[-1])
                soc.bind((host_ip, port))
                soc.listen()
                conn, addr = soc.accept()
                print("Connected with " + str(addr[0]) + ":" + str(addr[1]))
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
