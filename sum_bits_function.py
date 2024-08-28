from lib.turing_machines import SingleTapeTuringMachine

tm = SingleTapeTuringMachine(
    tape=">0011-0011<",
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
        "q22",
        "q23",
        "q24",
        "q25",
        "q26",
        "q27",
        "q28",
        "q29",
        "q30",
        "q31",
        "q32",
        "q33",
        "q34",
        "q35",
        "q36",
        "q37",
        "q38",
        "q39",
        "q40",
        "q41",
        "q42",
        "q43",
        "q44",
        "q45",
        "q46",
        "qh",
    ],
    initial_state="qi",
    halt_state="qh",
    program=[
        ("qi", ">", "q1", ">", 1),
        # first bit
        ("q1", "0", "q2", "-", 1),
        ("q1", "1", "q3", "-", 1),
        ("q2", "0", "q2", "0", 1),
        ("q3", "0", "q3", "0", 1),
        ("q2", "1", "q2", "1", 1),
        ("q3", "1", "q3", "1", 1),
        ("q2", "-", "q4", "-", 1),
        ("q3", "-", "q5", "-", 1),
        ("q4", "0", "q6", "0", -1),
        ("q4", "1", "q6", "1", -1),
        ("q5", "0", "q6", "1", -1),
        ("q5", "1", "q6", "0", -1),
        ("q6", "-", "q7", "-", -1),
        ("q6", "-", "q7", "-", -1),
        ("q7", "0", "q7", "0", -1),
        ("q7", "1", "q7", "1", -1),
        ("q7", "-", "q8", "-", 1),
        # second bit
        ("q8", "0", "q9", "-", 1),
        ("q8", "1", "q10", "-", 1),
        ("q9", "0", "q9", "0", 1),
        ("q10", "0", "q10", "0", 1),
        ("q9", "1", "q9", "1", 1),
        ("q10", "1", "q10", "1", 1),
        ("q9", "-", "q11", "-", 1),
        ("q10", "-", "q12", "-", 1),
        ("q11", "0", "q13", "0", 1),
        ("q12", "0", "q14", "0", 1),
        ("q11", "1", "q13", "1", 1),
        ("q12", "1", "q14", "1", 1),
        ("q13", "0", "q15", "0", -1),
        ("q14", "0", "q15", "1", -1),
        ("q13", "1", "q15", "1", -1),
        ("q14", "1", "q16", "0", -1),
        ("q16", "0", "q15", "1", -1),
        ("q16", "1", "q15", "0", -1),
        ("q15", "0", "q15", "0", -1),
        ("q15", "1", "q15", "1", -1),
        ("q15", "-", "q17", "-", -1),
        ("q17", "0", "q17", "0", -1),
        ("q17", "1", "q17", "1", -1),
        ("q17", "-", "q18", "-", 1),
        # third bit
        ("q18", "0", "q19", "-", 1),
        ("q18", "1", "q20", "-", 1),
        ("q19", "0", "q19", "0", 1),
        ("q20", "0", "q20", "0", 1),
        ("q19", "1", "q19", "1", 1),
        ("q20", "1", "q20", "1", 1),
        ("q19", "-", "q21", "-", 1),
        ("q20", "-", "q22", "-", 1),
        ("q21", "0", "q23", "0", 1),
        ("q22", "0", "q24", "0", 1),
        ("q21", "1", "q23", "1", 1),
        ("q22", "1", "q24", "1", 1),
        ("q23", "0", "q25", "0", 1),
        ("q24", "0", "q26", "0", 1),
        ("q23", "1", "q25", "1", 1),
        ("q24", "1", "q26", "1", 1),
        ("q25", "0", "q27", "0", -1),
        ("q26", "0", "q27", "1", -1),
        ("q25", "1", "q27", "1", -1),
        ("q26", "1", "q28", "0", -1),
        ("q28", "0", "q27", "1", -1),
        ("q28", "1", "q28", "0", -1),
        ("q28", "-", "q29", "-", -1),
        ("q27", "0", "q27", "0", -1),
        ("q27", "1", "q27", "1", -1),
        ("q27", "-", "q29", "-", -1),
        ("q29", "0", "q29", "0", -1),
        ("q29", "1", "q29", "1", -1),
        ("q29", "-", "q30", "-", 1),
        # forth bit
        ("q30", "0", "q31", "-", 1),
        ("q30", "1", "q32", "-", 1),
        ("q31", "-", "q31", "-", 1),
        ("q32", "-", "q32", "-", 1),
        ("q31", "0", "q33", "0", 1),
        ("q32", "0", "q34", "0", 1),
        ("q31", "1", "q33", "1", 1),
        ("q32", "1", "q34", "1", 1),
        ("q33", "0", "q35", "0", 1),
        ("q34", "0", "q36", "0", 1),
        ("q33", "1", "q35", "1", 1),
        ("q34", "1", "q36", "1", 1),
        ("q35", "0", "q37", "0", 1),
        ("q36", "0", "q38", "0", 1),
        ("q35", "1", "q37", "1", 1),
        ("q36", "1", "q38", "1", 1),
        ("q37", "0", "q39", "0", -1),
        ("q38", "0", "q39", "1", -1),
        ("q37", "1", "q39", "1", -1),
        ("q38", "1", "q40", "0", -1),
        ("q40", "0", "q39", "1", -1),
        ("q40", "1", "q40", "0", -1),
        ("q39", "0", "q39", "0", -1),
        ("q39", "1", "q39", "1", -1),
        ("q39", "-", "q41", "-", 1),
        ("q40", "-", "q41", "-", 1),
        # move
        ("q41", "0", "q42", "-", -1),
        ("q41", "1", "q43", "-", -1),
        ("q42", "-", "q42", "-", -1),
        ("q43", "-", "q43", "-", -1),
        ("q42", "0", "q42", "0", -1),
        ("q43", "0", "q43", "0", -1),
        ("q42", "1", "q42", "1", -1),
        ("q43", "1", "q43", "1", -1),
        ("q42", ">", "q44", ">", 1),
        ("q43", ">", "q45", ">", 1),
        ("q44", "0", "q44", "0", 1),
        ("q45", "0", "q45", "0", 1),
        ("q44", "1", "q44", "1", 1),
        ("q45", "1", "q45", "1", 1),
        ("q44", "-", "q41", "0", 1),
        ("q45", "-", "q41", "1", 1),
        ("q41", "-", "q41", "-", 1),
        ("q41", "<", "q46", "<", -1),
        ("q46", "-", "q46", "-", -1),
        ("q46", "0", "q46", "0", -1),
        ("q46", "1", "q46", "1", -1),
        ("q46", ">", "qh", ">", 1),
    ],
)

tm.validate()
tm.execute()
