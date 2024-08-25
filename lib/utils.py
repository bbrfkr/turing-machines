def check_alphabets(alphabets: list[str]):
    # check uniqueness
    original_size = len(alphabets)
    unique_size = len(list(set(alphabets)))
    if original_size != unique_size:
        return False

    # check length
    for alphabet in alphabets:
        if len(alphabet) != 1:
            return False
    return True

def check_tape(tape: str, alphabets: list[str]):
    for alphabet in tape:
        if alphabet in alphabets:
            return True
    return False

def check_states(states: list[str], initial_state: str, halt_state: str):
    # check uniqueness
    original_size = len(states)
    unique_size = len(list(set(states)))
    if original_size != unique_size:
        return False

    # check initial_state
    if (initial_state in states) and (halt_state in states) and (initial_state != halt_state):
        return True
    return False
