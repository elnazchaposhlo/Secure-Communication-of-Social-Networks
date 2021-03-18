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

        # self.create_socket()



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
                port = 55555 + int(self.name[-1])
                soc.bind((host_ip, port))
                soc.listen()
                print(self.name + " is listening...")
                conn, addr = soc.accept()
                print(self.name + " says >>> Connected with " + str(addr[0]) + ":" + str(addr[1]))
                while True:
                    try:
                        data = conn.recv(1024)
                        msg = data.decode('utf-8')
                        print(self.name + " says >>> data received: " + msg)
                        break
                    except:
                        break

            if (not self.children) and self.parent:
                host_ip = '127.0.0.1'
                port = 55555 + int(self.parent.name[-1])
                try:
                    soc.connect((host_ip, port))
                    print(self.name + " says >>> Connected to: " + self.parent.name)
                    # send own secret key
                    msg = "Greetings! I am " + self.name + ". Good to connect with you!"
                    soc.send(msg.encode('utf-8'))
                except:
                    print("Connection Error")
