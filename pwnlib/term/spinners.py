# -*- coding: utf-8 -*-
__all__ = ['spinners']

def billboard(msg, window):
    return [msg[i: i + window].ljust(window, ' ') for i in range(len(msg))]

spinners = [
    ['/.......','./......','../.....','.../....','..../...','...../..','....../.',
     '.......\\','......\\.','.....\\..','....\\...','...\\....','..\\.....','.\\......'],
    billboard('   8=================D~~~   D:  ', 5),
    billboard('   trollololol lololol lololol     trollolololoooool      ', 5),
    ['|', '/', '-', '\\'],
    ['q', 'p', 'b', 'd'],
    ['.', 'o', 'O', '0', '*', ' ', ' ', ' '],
    ['▁', '▃', '▄', '▅', '▆', '▇', '█', '▇', '▆', '▅', '▄', '▃'],
    ['┤', '┘', '┴', '└', '├', '┌', '┬', '┐'],
    ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙'],
    ['◢', '◢', '◣', '◣', '◤', '◤', '◥', '◥'],
    ['◐', '◓', '◑', '◒'],
    ['▖', '▘', '▝', '▗'],
    ['.', 'o', 'O', '°', ' ', ' ', '°', 'O', 'o', '.', ' ', ' '],
    ['<', '<', '∧', '∧', '>', '>', 'v', 'v'],
]
