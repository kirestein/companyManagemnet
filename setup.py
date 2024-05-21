from cx_Freeze import setup, Executable

setup(
    name="EMPLOYEE REGISTRATION",
    version="0.1",
    description="",
    executables=[Executable("bmi.py", base="Win32GUI")]
)