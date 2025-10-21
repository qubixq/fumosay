#!/usr/bin/env python3


import argparse
import sys
import textwrap
from pathlib import Path
from typing import List, Tuple

FUMO_STYLE1 = r"""
⠀⠀⠀⣠⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀
⠀⠀⡜⠁⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⠷⠶⠱⡄
⠀⢸⣸⣿⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠫⢀⣖⡃⢀⣸⢹
⠀⡇⣿⣿⣶⣤⡀⠀⠀⠙⢆⠀⠀⠀⠀⠀⣠⡪⢀⣤⣾⣿⣿⣿⣿⣸
⠀⡇⠛⠛⠛⢿⣿⣷⣦⣀⠀⣳⣄⠀⢠⣾⠇⣠⣾⣿⣿⣿⣿⣿⣿⣽
⠀⠯⣠⣠⣤⣤⣤⣭⣭⡽⠿⠾⠞⠛⠷⠧⣾⣿⣿⣯⣿⡛⣽⣿⡿⡼
⠀⡇⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣮⡛⢿⠃
⠀⣧⣛⣭⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣷⣎⡇
⠀⡸⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣷⣟⡇
⣜⣿⣿⡧⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⣸⣿⡜⡄
⠉⠉⢹⡇⠀⠀⠀⢀⣞⠡⠀⠀⠀⠀⠀⠀⡝⣦⠀⠀⠀⠀⢿⣿⣿⣹
⠀⠀⢸⠁⠀⠀⢠⣏⣨⣉⡃⠀⠀⠀⢀⣜⡉⢉⣇⠀⠀⠀⢹⡄⠀⠀
⠀⠀⡾⠄⠀⠀⢸⣾⢏⡍⡏⠑⠆⠀⢿⣻⣿⣿⣿⠀⠀⢰⠈⡇⠀⠀
⠀⢰⢇⢀⣆⠀⢸⠙⠾⠽⠃⠀⠀⠀⠘⠿⡿⠟⢹⠀⢀⡎⠀⡇⠀⠀
⠀⠘⢺⣻⡺⣦⣫⡀⠀⠀⠀⣄⣀⣀⠀⠀⠀⠀⢜⣠⣾⡙⣆⡇⠀⠀
⠀⠀⠀⠙⢿⡿⡝⠿⢧⡢⣠⣤⣍⣀⣤⡄⢀⣞⣿⡿⣻⣿⠞⠀⠀⠀
⠀⠀⠀⢠⠏⠄⠐⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠳⢤⣉⢳⠀⠀⠀
⢀⡠⠖⠉⠀⠀⣠⠇⣿⡿⣿⡿⢹⣿⣿⣿⣿⣧⣠⡀⠀⠈⠉⢢⡀⠀
⢿⠀⠀⣠⠴⣋⡤⠚⠛⠛⠛⠛⠛⠛⠛⠛⠙⠛⠛⢿⣦⣄⠀⢈⡇⠀
⠈⢓⣤⣵⣾⠁⣀⣀⠤⣤⣀⠀⠀⠀⠀⢀⡤⠶⠤⢌⡹⠿⠷⠻⢤⡀
⢰⠋⠈⠉⠘⠋⠁⠀⠀⠈⠙⠳⢄⣀⡴⠉⠀⠀⠀⠀⠙⠂⠀⠀⢀⡇
⢸⡠⡀⠀⠒⠂⠐⠢⠀⣀⠀⠀⠀⠀⠀⢀⠤⠚⠀⠀⢸⣔⢄⠀⢾⠀
⠀⠑⠸⢿⠀⠀⠀⠀⢈⡗⠭⣖⡒⠒⢊⣱⠀⠀⠀⠀⢨⠟⠂⠚⠋⠀
⠀⠀⠀⠘⠦⣄⣀⣠⠞⠀⠀⠀⠈⠉⠉⠀⠳⠤⠤⡤⠞⠀⠀⠀⠀⠀
"""

FUMO_STYLE2 = r"""
⠀⢀⣒⠒⠆⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡛⠛⠻⣷⣶⣦⣬⣕⡒⠤⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡿⢿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣳⠖⢋⣩⣭⣿⣶⡤⠶⠶⢶⣒⣲⢶⣉⣐⣒⣒⣒⢤⡀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠉⣩⣭⣽⣶⣾⣿⢿⡏⢁⣴⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠉⠙⠲⢭⣯⣟⡿⣷⣘⠢⡀⠀⠀⠀⠀⠀
⠹⣷⣿⣿⣿⣿⣿⢟⣵⠋⢠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣾⣦⣾⣢⠀⠀⠀⠀
⠀⠹⣿⣿⣿⡿⣳⣿⠃⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⠟⠀⠀⠀⠀
⠀⠀⠹⣿⣿⣵⣿⠃⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠛⣯⡇⠛⣽⣦⣿⠀⠀⠀⠀⢀⠔⠙⣄⠀⠀⠀⠀⠀⠀⣠⠳⡀⠀⠀⠀⠀⢿⡵⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣸⣿⣿⣿⠿⢿⠟⠀⠀⠀⢀⡏⠀⠀⠘⡄⠀⠀⠀⠀⢠⠃⠀⠹⡄⠀⠀⠀⠸⣿⣷⡀⠀⠀⠀
⠀⠀⠀⢰⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⢸⠒⠤⢤⣀⣘⣆⠀⠀⠀⡏⢀⣀⡠⢷⠀⠀⠀⠀⣿⡿⠃⠀⠀⠀
⠀⠀⠀⠸⣿⣿⠟⢹⣥⠀⠀⠀⠀⠀⣸⣀⣀⣤⣀⣀⠈⠳⢤⡀⡇⣀⣠⣄⣸⡆⠀⠀⠀⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠁⠁⠀⢸⢟⡄⠀⠀⠀⠀⣿⣾⣿⣿⣿⣿⠁⠀⠈⠙⠙⣯⣿⣿⣿⡇⠀⠀⢠⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠇⢨⢞⢆⠀⠀⠀⡿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⣿⣿⣿⡿⡇⠀⣠⢟⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡼⠀⢈⡏⢎⠳⣄⠀⡇⠙⠛⠟⠛⠀⠀⠀⠀⠀⠀⠘⠻⠛⢱⢃⡜⡝⠈⠚⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣅⠁⢸⣋⠈⢣⡈⢷⠇⠀⠀⠀⠀⠀⣄⠀⠀⢀⡄⠀⠀⣠⣼⢯⣴⠇⣀⡀⢸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠳⡌⠛⣶⣆⣷⣿⣦⣄⣀⠀⠀⠀⠈⠉⠉⢉⣀⣤⡞⢛⣄⡀⢀⡨⢗⡦⠎⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠪⣿⠁⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠉⠁⢸⠀⠀⠀⠄⠙⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠚⡉⢳⡄⠡⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠁⣠⣧⣤⣄⣀⡀⡰⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠔⠉⠀⠀⠀⠀⢀⣧⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣅⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠆⠀⠀⠀⣀⣼⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⣠⠖⠒⠒⠛⢿⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠑⠤⠴⠞⢋⣵⣿⢿⣿⣿⣿⣿⣿⣿⠗⣀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⢀⡼⣶⣤⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠟⢛⣿⠀⠙⠲⠽⠛⠛⠵⠞⠉⠙⠳⢦⣀⣀⡞⠀⠀⠀⠀⡠⠋⠐⠣⠮⡁⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣎⡀⢀⣾⠇⢀⣠⡶⢶⠞⠋⠉⠉⠒⢄⡀⠉⠈⠉⠀⠀⠀⣠⣾⠀⠀⠀⠀⠀⢸⡀
⠀⠀⠀⠀⠀⠀⠀⠘⣦⡀⠘⢁⡴⢟⣯⣞⢉⠀⠀⠀⠀⠀⠀⢹⠶⠤⠤⡤⢖⣿⡋⢇⠀⠀⠀⠀⠀⢸⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠵⠗⠺⠟⠖⢈⡣⡄⠀⠀⠀⠀⢀⣼⡤⣬⣽⠾⠋⠉⠑⠺⠧⣀⣤⣤⡠⠟⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠷⠶⠦⠶⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

FUMO_STYLE3 = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠚⡙⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠈⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠞⠁⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠚⠉⠉⡩⠉⠉⠉⠉⠉⠉⠙⠒⠒⠲⠤⢤⣀⡤⠚⠉⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠊⠁⢠⠄⠀⠀⠀⠐⠁⠀⠁⠀⠀⢀⠈⠀⠤⠀⠀⡈⠙⠢⣄⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠁⠀⠀⠀⠰⠎⠀⠀⠀⠈⢷⡀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠃⠀⠀⠱⣄⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⢀⣀⣀⣠⠤⠤⠤⠤⠤⠤⠤⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡄⡔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠓⢢⠖⠚⠉⢉⣵⣿⣄⣀⣀⣀⡤⠔⠚⠉⠉⠙⠓⠦⣍⠓⠲⢤⡀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡴⠃⢀⡠⠞⠉⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠯⠤⠤⠤⠤⠵⠦⢤⣀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠐⠶⠶⢎⣩⣤⣾⠋⠀⠀⣠⠞⠉⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⡰⠛⢦⡀⠀⠀⠀⠀⠀⠀⣏⠻⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⢀⣞⣑⣆⣐⣒⣚⣆⠀⠀⠀⠀⠀⢀⠾⠅⠀⣀⡉⠲⣄⡀⠀⠀⠀⢸⣿⠛⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣀⣠⠤⠤⠒⢦⡀⢸⠀⡼⡇⠀⠀⠀⠘⢲⡏⠱⣄⠀⣀⡔⠉⠉⠉⠙⣖⠢⡄⢸⠉⠀⠀⠀⢀⣿⠀⠀⠉⢀⡠⠔⠒⠢⠤⣀⡀⠀
⠈⠙⠒⠤⢄⣀⢀⡽⠚⣷⠁⢇⡀⠀⠀⢠⠞⠀⠀⠀⠉⠁⣇⠀⠀⠀⠀⠈⡿⢠⠋⠀⠀⠀⠀⣼⡟⠠⣤⠚⠁⠀⠀⠀⠀⠀⣀⠬⠛
⠀⢀⣀⠤⠤⠚⢥⣄⡤⢾⡀⠀⠉⠑⠊⠁⠀⠀⠀⢀⠀⠀⠘⠦⣀⣀⣀⠴⡱⠋⣀⣴⣂⡠⠞⢻⣦⠀⣈⣉⠑⠒⠤⠤⠒⠉⠀⠀⠀
⠀⠈⠉⠑⠒⠦⠏⠈⡶⢀⠱⢄⣀⠀⠀⠀⠀⠘⠖⠉⠀⠀⠀⠀⣀⣀⡠⠞⠓⠉⢁⡉⠁⢰⠒⣾⠟⠀⠈⠪⡉⠑⠲⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠏⡇⢾⣿⣆⣀⣈⠉⠉⠰⠶⠶⠈⠉⠉⢉⠉⠉⠁⡀⠀⠀⠈⢷⠀⠁⣰⠇⢸⡿⠀⠀⣷⣆⠹⠆⣀⠹⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠓⠈⠁⠈⣏⠉⠉⠉⠉⠒⠲⠤⠤⠤⣀⣀⣀⣙⣀⣀⣈⡥⠤⠤⠶⠒⠉⠁⢠⣿⣅⣀⠀⠸⣈⠇⠀⠀⠉⠙⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣶⣿⣿⣧⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣿⣿⣿⣿⡷⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠻⠿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿
"""

def create_bubble(text: str, width: int = 40) -> str:
    lines = []

    wrapped = textwrap.wrap(text, width=width)

    if not wrapped:
        wrapped = ['']

    max_len = max(len(line) for line in wrapped) if wrapped else 0

    lines.append(' ' + '_' * (max_len + 2))

    if len(wrapped) == 1:
        lines.append(f'< {wrapped[0].ljust(max_len)} >')
    else:
        for i, line in enumerate(wrapped):
            if i == 0:
                lines.append(f'/ {line.ljust(max_len)} \\')
            elif i == len(wrapped) - 1:
                lines.append(f'\\ {line.ljust(max_len)} /')
            else:
                lines.append(f'| {line.ljust(max_len)} |')

    lines.append(' ' + '-' * (max_len + 2))

    return '\n'.join(lines)

def create_thought_bubble(text: str, width: int = 40) -> str:
    lines = []

    wrapped = textwrap.wrap(text, width=width)

    if not wrapped:
        wrapped = ['']

    max_len = max(len(line) for line in wrapped) if wrapped else 0

    lines.append(' ' + '_' * (max_len + 2))

    for line in wrapped:
        lines.append(f'( {line.ljust(max_len)} )')

    lines.append(' ' + '-' * (max_len + 2))

    return '\n'.join(lines)

def add_bubble_tail(bubble: str, character: str, thought: bool = False) -> str:
    tail = '  o\n   o' if thought else '  \\\n   \\'
    return bubble + '\n' + tail + '\n' + character

def get_fumo_art(style: str = 'style1') -> str:
    styles = {
        'style1': FUMO_STYLE1,
        'style2': FUMO_STYLE2,
        'style3': FUMO_STYLE3,
        'default': FUMO_STYLE1,
        '1': FUMO_STYLE1,
        '2': FUMO_STYLE2,
        '3': FUMO_STYLE3
    }
    return styles.get(style, FUMO_STYLE1)

def fumosay(message: str,
             width: int = 40,
             thought: bool = False,
             style: str = 'style1',
             no_bubble: bool = False) -> str:

    fumo = get_fumo_art(style)

    if no_bubble:
        return message + '\n' + fumo

    if thought:
        bubble = create_thought_bubble(message, width)
    else:
        bubble = create_bubble(message, width)

    return add_bubble_tail(bubble, fumo, thought)

def read_stdin() -> str:
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    return ""

def main():
    parser = argparse.ArgumentParser(
        description='fumosay - Let Fumo say something',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  fumosay.py "I'm the Strongest!"
  echo "Baka baka!" | fumosay.py
  fumosay.py -t "What should I do?"
  fumosay.py -s style2 "⑨ is the best!"
  fumosay.py -s 3 "Nice Braille art!"
  fumosay.py -w 60 "Long message with custom width"
        '''
    )

    parser.add_argument(
        'message',
        nargs='*',
        help='Message for Fumo to say'
    )

    parser.add_argument(
        '-w', '--width',
        type=int,
        default=40,
        help='Maximum width of speech bubble (default: 40)'
    )

    parser.add_argument(
        '-t', '--think',
        action='store_true',
        help='Make Fumo think instead of speak'
    )

    parser.add_argument(
        '-s', '--style',
        choices=['style1', 'style2', 'style3', '1', '2', '3', 'default'],
        default='style1',
        help='Fumo ASCII art style (style1/1, style2/2, style3/3)'
    )

    parser.add_argument(
        '-n', '--no-bubble',
        action='store_true',
        help='Print message without bubble'
    )

    parser.add_argument(
        '-f', '--file',
        type=str,
        help='Read message from file'
    )

    args = parser.parse_args()

    message = ''

    if args.file:
        try:
            message = Path(args.file).read_text().strip()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.message:
        message = ' '.join(args.message)
    else:
        message = read_stdin()

    if not message:
        message = "I'm the Strongest! ⑨"

    output = fumosay(
        message,
        width=args.width,
        thought=args.think,
        style=args.style,
        no_bubble=args.no_bubble
    )

    print(output)

if __name__ == '__main__':
    main()
