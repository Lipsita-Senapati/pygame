import cx_Freeze

executables = [cx_Freeze.Executable("pg1.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["racecar1.png"]}},
    executables = executables

    )
