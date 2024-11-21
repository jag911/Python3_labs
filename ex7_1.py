import sys
import re
def main():
    if sys.platform == 'win32' or sys.platform == 'win64':
        pass # no one cares
    else:
        svc_file = r"/etc/services"
    used_ports = {'tcp': set(), 'udp': set()}
    pre_reg = re.compile(r"(\d{1,5})/(tcp|udp)")
    with open(svc_file,"rt") as fh_in:
        for line in fh_in:
            line = line.strip()
            if line[0] != "#" and not line.isspace():
                m = pre_reg.search(line)
                if m:
                    num, proto = m.group(0).split('/')
                    if int(num) < 1024:
                        used_ports[proto].add(num)
    print(1024-len(used_ports['udp']))
    print(1024-len(used_ports['tcp']))

    print(set(range(1,1024)) - used_ports['tcp'])
    print(set(range(1,1024)) - used_ports['udp'])
    return None

if __name__ == "__main__":
    import cProfile
    cProfile.run("main()", "stats.prof")
    import sys
    sys.exit(0)