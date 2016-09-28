#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os

__author__ = 'Marco Bartel'


# import time
# import socket
# import optparse
# import textwrap
#
# import paramiko
#
# HOST, PORT = 'localhost', 22
# BACKLOG = 10
#
# def start_server(host, port):
#     paramiko.common.logging.basicConfig(level=logging.DEBUG)
#
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
#     server_socket.bind((host, port))
#     server_socket.listen(BACKLOG)
#
#     while True:
#         conn, addr = server_socket.accept()
#
#         host_key = paramiko.RSAKey.from_private_key_file(keyfile)
#         transport = paramiko.Transport(conn)
#         transport.add_server_key(host_key)
#         transport.set_subsystem_handler(
#             'sftp', paramiko.SFTPServer, SFTPServer)
#
#         server = SFTPServerInterface()
#         transport.start_server(server=server)
#
#         channel = transport.accept()
#         while transport.is_active():
#             time.sleep(1)
#
#
# def main():
#     usage = """\
#     usage: sftpserver [options]
#     -k/--keyfile should be specified
#     """
#     parser = optparse.OptionParser(usage=textwrap.dedent(usage))
#     parser.add_option(
#         '--host', dest='host', default=HOST,
#         help='listen on HOST [default: %default]')
#     parser.add_option(
#         '-p', '--port', dest='port', type='int', default=PORT,
#         help='listen on PORT [default: %default]'
#         )
#     parser.add_option(
#         '-l', '--level', dest='level', default='INFO',
#         help='Debug level: WARNING, INFO, DEBUG [default: %default]'
#         )
#     parser.add_option(
#         '-k', '--keyfile', dest='keyfile', metavar='FILE',
#         help='Path to private key, for example /tmp/test_rsa.key'
#         )
#
#     options, args = parser.parse_args()
#
#     # if options.keyfile is None:
#     #     parser.print_help()
#     #     sys.exit(-1)
#
#     start_server(options.host, options.port, options.keyfile, options.level)


