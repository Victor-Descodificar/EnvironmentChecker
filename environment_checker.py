# This script checks if the required programs are avaiable in the machine.

import json
import os
import subprocess
from prettytable import PrettyTable
import re

class EnvChecker:

    def __init__(self):
        self.json_requirements = os.getcwd() + '/requirements.json'
        self.results = []

    def get_software_requirements(self):

        # Open json file
        data = ''
        with open(self.json_requirements) as f:
            data = json.load(f)

        # Get only the software that is required as 'true' as has some validation command to verify the version
        list_size = len(data["required_softwares"])
        for i in range(1,  list_size + 1):
            item = data["required_softwares"]["software_" + str(i)]
            if item["required"] == "true" and item["check_cmd"]:
                self.results.append(self.__get_software_versions(item))

    
    def __get_software_versions(self, _item):

        installed_versions = []
        not_found_versions = []
        error_found = False
        verification_command = ''

        try:
            # Get the verification command output
            command = _item["check_cmd"].split()
            out = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            stdout, stderr = out.communicate()
            if stdout is not None:
                # Validate versions
                for version in _item["version"]:
                    if re.search(version, str(stdout)):
                       installed_versions.append(version)
                    else:
                        not_found_versions.append(version)
            elif stderr is not None:
                error_found = True
                verification_command = _item["check_cmd"]
        except Exception:
            error_found = True
            verification_command = _item["check_cmd"]

        results = {
            'program_name': _item["name"],
            'required_versions': _item["version"],
            'installed_versions': installed_versions,
            'error_found': error_found,
            'command': verification_command
        }

        return results

    def report_software_requirements(self):
        table = PrettyTable()
        table.field_names = ['Required programs', 'Required version', 'Installed programs', 'Installed version', 'Error', 'Validation']
        for results in self.results:
            if results['error_found']:
                table.add_row([results['program_name'], results['required_versions'], 'Unkown', results['installed_versions'], 'Error running the command: ' + results['command'], 'FAILED'])
            elif results['required_versions'] != results['installed_versions']:
                table.add_row([results['program_name'], results['required_versions'], results['program_name'], results['installed_versions'], 'None', 'FAILED'])
            else:
                table.add_row([results['program_name'], results['required_versions'], results['program_name'], results['installed_versions'], 'None', 'PASSED'])

        print(table)

if __name__ == "__main__":
    ec = EnvChecker()
    ec.get_software_requirements()
    ec.report_software_requirements()
