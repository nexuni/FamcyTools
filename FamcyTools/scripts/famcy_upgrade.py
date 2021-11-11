import subprocess
import pkg_resources
import FamcyTools

def main(args):
	famcy_id = args[0]
	script_output = subprocess.check_output(["bash", FamcyTools.FAMCY_DIR % (USERNAME, args[0])+"/scripts/bash/"+"upgrade.sh", FamcyTools.FAMCY_DIR % (USERNAME, args[0]), famcy_id]) 
	print("[Famcy Upgrade] ", script_output.decode())
	print("Famcy version after upgrade: ", pkg_resources.require("Famcy")[0].version)