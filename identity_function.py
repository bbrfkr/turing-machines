from lib.turing_machines import SingleTapeTuringMachine

tm = SingleTapeTuringMachine(
    tape=">10110--",
    alphabets=[">", "1", "0", "-"],
    states=["qi", "q1", "q2", "q3", "qh"],
    initial_state="qi",
    halt_state="qh",
    program=[
        ("qi", ">", "q1", ">", 1),
        ("q1", "0", "q1", "-", 1),
        ("q1", "1", "q1", "-", 1),
        ("q1", "-", "q2", "-", -1),
        ("q2", "-", "q2", "-", -1),
        ("q2", ">", "q3", ">", 1),
        ("q3", "-", "qh", "1", 0),
    ],
)

tm.validate()
tm.execute()
