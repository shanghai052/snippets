import select
import SocketServer


class ForwardServer(SocketServer.ThreadingTCPServer):
    daemon_threads = True
    allow_reuse_address = True


class Handler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            channel = self.ssh_transport.open_channel('direct-tcpip',
                                                      (self.chain_host, self.chain_port),
                                                      self.request.getpeername())
        except Exception, e:
            print 'Incoming request to %s:%d failed: %s' % (self.chain_host,
                                                            self.chain_port, repr(e))
            return

        if channel is None:
            print 'Incoming request to %s:%d was rejected by the SSH server.' % \
                  (self.chain_host, self.chain_port)
            return

        print 'Connected!  Tunnel open %r -> %r -> %r' % (self.request.getpeername(),
                                                          channel.getpeername(),
                                                          (self.chain_host,
                                                           self.chain_port))

        while True:
            r, w, x = select.select([self.request, channel], [], [])
            if self.request in r:
                data = self.request.recv(1024)
                if len(data) == 0:
                    break
                channel.send(data)
            if channel in r:
                data = channel.recv(1024)
                if len(data) == 0:
                    break
                self.request.send(data)

        peername = self.request.getpeername()
        channel.close()
        self.request.close()
        print 'Tunnel closed from %r' % (peername,)


def forward_tunnel(local_port, remote_host, remote_port, transport):
    class SubHandler(Handler):
        chain_host = remote_host
        chain_port = remote_port
        ssh_transport = transport

    ForwardServer(('', local_port), SubHandler).serve_forever()


if __name__ == '__main__':
    pass
