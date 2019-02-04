from pathlib import Path
from loguru import logger
import re

class QlrReplace:

    def __init__(self, path, substitutions):
        self.path = Path(path)
        self.substitutions = substitutions
    
    def replace_substitutions(self, string):
        substrings = sorted(self.substitutions, key=len, reverse=True)
        regex = re.compile('|'.join(map(re.escape, substrings)))
        return regex.sub(lambda match: self.substitutions[match.group(0)], string)

    def erstat_datasource(self, qlr_path):
        with open(qlr_path.absolute()) as qlr_f:
            logger.debug(f'Åbner: {qlr_path.name}')
            lines = qlr_f.readlines()

        with open(qlr_path.absolute(), 'w') as ny_qlr:
            for line in lines:
                if '<datasource>' in line:
                    new_line = self.replace_substitutions(line)
                    ny_qlr.write(new_line)
                else:
                    ny_qlr.write(line)    
    
    def get_files(self):
        qlr_files = self.path.rglob('*.qlr')
        return qlr_files