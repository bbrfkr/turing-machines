from lib.turing_machines import SingleTapeTuringMachine

tm = SingleTapeTuringMachine(
    tape=">1101101010-",
    alphabets=[">", "1", "0", "-"],
    states=["qi", "q1", "q2", "q3", "q4", "qh"],
    initial_state="qi",
    halt_state="qh",
    program=[
        ("qi", ">", "q1", ">", 1),
        ("q1", "0", "q1", "0", 1),
        ("q1", "1", "q1", "1", 1),
        ("q1", "-", "q2", "-", -1),
        ("q2", "0", "q3", "-", 0),
        ("q2", "1", "q4", "-", 0),
        ("q3", "-", "q2", "1", -1),
        ("q4", "-", "q2", "0", -1),
        ("q2", ">", "qh", ">", 1),
    ],
)

tm.validate()
tm.execute()
