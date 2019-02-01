from pathlib import Path
from loguru import logger
import re

path = Path('w:/qgis/temavaelgere')

substitutions = {}

def replace(string, substitutions):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], string)

with open(qlr_fil.absolute()) as qlr_f:
    logger.debug(f'Åbner: {qlr_fil.name}')
    lines = qlr_f.readlines()

with open(qlr_fil.absolute(), 'w') as ny_qlr:
    logger.debug(f'Overskriver: {qlr_fil.name}')
    for line in lines:
        if '<datasource>' in line:
            new_line = replace(line, substitutions)
            ny_qlr.write(new_line)
        else:
            ny_qlr.write(line)    