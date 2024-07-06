import nmap

def hostScan(host, ports, arguments, run_as_root):
  nm = nmap.PortScanner()
  ports = ",".join(ports)
  
  if run_as_root:
    nm.scan(hosts=host, ports=ports, arguments=arguments + ' -O -sV --script=default', sudo=True)
  else:
    nm.scan(hosts=host, ports=ports, arguments=arguments + ' -O -sV --script=default')

  for host in nm.all_hosts():
    for host_key, host_value in nm[host].items():
      print(f"{host_key} : {host_value}")
    for osmatch in nm[host]['osmatch']:
      for osmatch_key, osmatch_value in osmatch.items():
        print(f"{osmatch_key} : {osmatch_value}")
      for osclass in osmatch['osclass']:
        for osclass_key, osclass_value in osclass.items():
          print(f"{osclass_key} : {osclass_value}")
    for proto in nm[host].all_protocols():
      print(f"Protocol : {proto}")

      lport = nm[host][proto].keys()
      for port in lport:
        for port_key, port_value in nm[host][proto][port].items():
          print(f"{port_key} : {port_value}")

host = input("Host: ")
ports = input("Puertos: ").split(",")
arguments = input("Argumentos: ")
run_as_root = input("Correr como super usuario? (s/n): ").lower() == "s"

hostScan(host, ports, arguments, run_as_root)