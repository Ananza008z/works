import sys
import os
from cx_Freeze import setup, Executable

executables = [Executable(
    "main.py",
    icon="Rank.ico",
    shortcut_name="Ranking Program",
    shortcut_dir="DesktopFolder",
    base="Win32GUI")]

setup(
    name="Ranking Program",
    version="2.0",
    description="Ranking Program",
    author="Anansit Chaiwaree",
    py_modules=["ranking_module", "scoring_module", "config"],
    executables=executables
)
