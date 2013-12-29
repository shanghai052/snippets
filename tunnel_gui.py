import Tkinter as tk
from generate_tunnels import SshThread
from time import sleep
import tkMessageBox as tkm

class TunnelGUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.hops = []
        self.entries = {}
        self.fields = ('ssh_ip', 'ssh_port', 'username', 'password',
                       'end_ip', 'end_port', 'forwarding_port')
        self.initialize()

    def initialize(self):
        self.parent.title('Tunnel Generator')

        label_frame = tk.LabelFrame(self.parent, bd=2)
        for i, label in enumerate(self.fields):
            field_label = tk.Label(label_frame, text=label, pady=3)
            field_entry = tk.Entry(self.parent, bd=2)
            field_label.grid(row=i, column=0, sticky='w')
            field_entry.grid(row=i, column=1)
            self.entries[label] = field_entry

        label_frame.grid(row=0, column=0, rowspan=7, sticky='ns')

        tk.Button(self.parent, text='Tunnels GO', width=7,
                                 command=self.go).grid(row=7, column=1, sticky='w')
        tk.Button(self.parent, text='Save', width=7,
                                  command=self.save).grid(row=7, column=1, sticky='e')
        tk.Button(self.parent, text='Report', command='').grid(row=7, column=0, sticky='we')


    def save(self):
        hop = {}
        for field in self.entries:
            if field.endswith('port'):
                hop[field] = int(self.entries[field].get())
            else:
                hop[field] = self.entries[field].get()
            self.entries[field].delete(0, tk.END)
        for k, v in hop.items():
            print k, 'is', v
        print '---------------------------'
        self.hops.append(hop)

    def go(self):
        threads = {}
        if self.hops:
            for i, hop in enumerate(self.hops):
                i += 1
                threads[i] = SshThread(**hop)
                threads[i].start()
                sleep(2)
                while not threads[i].is_authenticated():
                    sleep(0.25)
                    pass
            tkm.showinfo("Done", 'All tunnels complete.')

if __name__ == '__main__':
    root = tk.Tk()
    TunnelGUI(root).mainloop()
