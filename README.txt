#Required Python Module
socket
subprocess
os
base64
json

**NOTE:
Before Use Edit line 66 (listner.py) and line 70 (backdoor.py) with ur IP address and listening port no.

(X.XX.XX.XX, xxxx) => (192.168.1.10, 4444)

**Both Attacker and victim machine must be in same network.

Deploy the backdoor.py file in the Victim machine and use listener.py from your machine.

NOTE: The Victim machine must hv required modules and python interpreter.

However if your Deploying the backdoor as .exe package then no need of python interpreter in Victim machine