from for_serv import forward_tunnel
from paramiko import MissingHostKeyPolicy, SSHClient
from threading import Thread


class AllowAnythingPolicy(MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return


class SshThread(Thread):
    def __init__(self, **kwargs):
        Thread.__init__(self)
        self.ssh_ip = kwargs.get('ssh_ip')
        self.ssh_port = kwargs.get('ssh_port')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.forwarding_port = kwargs.get('forwarding_port')
        self.end_ip = kwargs.get('end_ip')
        self.end_port = kwargs.get('end_port')
        self.client = SSHClient()

    def run(self):
        self.client.set_missing_host_key_policy(AllowAnythingPolicy())
        self.client.connect(self.ssh_ip, port=self.ssh_port, username=self.username, password=self.password,
                            look_for_keys=False)
        transport = self.client.get_transport()
        forward_tunnel(self.forwarding_port, self.end_ip, self.end_port, transport)

    def is_authenticated(self):
        transport = self.client.get_transport()
        return transport.is_authenticated()


def main(hops):
    from time import sleep
    threads = {}
    for i, hop in enumerate(hops):
        i += 1
        threads[i] = SshThread(**hop)
        threads[i].start()
        sleep(2)
        while not threads[i].is_authenticated():
            sleep(0.25)
            pass
    print 'All tunnels complete.'

if __name__ == '__main__':
    pass
    '''
    to have a more permanent solution, build hops as a list of dictionaries here such as:
        hops = []
        hop_one = {
            'ssh_ip': ip,
            'ssh_port': port,
            'username': username,
            'password': password,
            'forwarding_port': forwarding_port,
            'end_ip': end_ip,
            'end_port': end_port
        }
        hops.append(hop_one)
        ...
        main(hops)
    '''
