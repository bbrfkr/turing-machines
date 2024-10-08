from lib.turing_machines import SingleTapeTuringMachine

tm = SingleTapeTuringMachine(
    tape=">11010110--------<",
    alphabets=[">", "1", "0", "-", "<"],
    states=[
        "qi",
        "q1",
        "q2",
        "q3",
        "q4",
        "q5",
        "q6",
        "q7",
        "q8",
        "q9",
        "q10",
        "q11",
        "q12",
        "q13",
        "q14",
        "q15",
        "q16",
        "q17",
        "q18",
        "q19",
        "q20",
        "q21",
        "qh",
    ],
    initial_state="qi",
    halt_state="qh",
    program=[
        ("qi", ">", "q1", ">", 1),
        ("q1", "0", "q1", "0", 1),
        ("q1", "1", "q1", "1", 1),
        ("q1", "-", "q2", "-", -1),
        ("q2", "0", "q3", "-", 1),
        ("q2", "1", "q4", "-", 1),
        ("q3", "-", "q5", "0", -1),
        ("q4", "-", "q5", "1", -1),
        ("q5", "-", "q5", "-", -1),
        ("q5", "0", "q6", "-", 1),
        ("q5", "1", "q7", "-", 1),
        ("q6", "-", "q6", "-", 1),
        ("q7", "-", "q7", "-", 1),
        ("q6", "0", "q8", "0", 1),
        ("q7", "0", "q9", "0", 1),
        ("q6", "1", "q8", "1", 1),
        ("q7", "1", "q9", "1", 1),
        ("q8", "0", "q8", "0", 1),
        ("q9", "0", "q9", "0", 1),
        ("q8", "1", "q8", "1", 1),
        ("q9", "1", "q9", "1", 1),
        ("q8", "-", "q10", "0", -1),
        ("q9", "-", "q10", "1", -1),
        ("q10", "0", "q10", "0", -1),
        ("q10", "1", "q10", "1", -1),
        ("q10", "-", "q5", "-", -1),
        ("q5", ">", "q11", ">", 1),
        ("q11", "-", "q11", "-", 1),
        ("q11", "0", "q12", "-", -1),
        ("q11", "1", "q13", "-", -1),
        ("q12", "-", "q12", "-", -1),
        ("q13", "-", "q13", "-", -1),
        ("q12", "0", "q12", "0", 1),
        ("q12", "1", "q12", "1", 1),
        ("q13", "0", "q13", "0", 1),
        ("q13", "1", "q13", "1", 1),
        ("q12", ">", "q14", ">", 1),
        ("q13", ">", "q15", ">", 1),
        ("q14", "-", "q16", "0", 1),
        ("q15", "-", "q16", "1", 1),
        ("q16", "-", "q16", "-", 1),
        ("q16", "<", "q21", "<", -1),
        ("q21", "0", "q21", "0", -1),
        ("q21", "1", "q21", "1", -1),
        ("q21", "-", "q21", "-", -1),
        ("q21", ">", "qh", ">", 1),
        ("q16", "0", "q17", "-", -1),
        ("q16", "1", "q18", "-", -1),
        ("q17", "-", "q17", "-", -1),
        ("q18", "-", "q18", "-", -1),
        ("q17", "0", "q19", "0", 1),
        ("q18", "0", "q20", "0", 1),
        ("q17", "1", "q19", "1", 1),
        ("q18", "1", "q20", "1", 1),
        ("q19", "-", "q16", "0", 1),
        ("q20", "-", "q16", "1", 1),
    ],
)

tm.validate()
tm.execute()
