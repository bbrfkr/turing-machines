from enum import Enum
from .errors import ValidationError
from .utils import (
    check_alphabets,
    check_states,
    check_tape,
)

class SingleTapeTuringMachine:
    is_valid = False
    
    class Index(Enum):
        NOW_STATE = 0
        READ_ALPHABET = 1
        NEXT_STATE = 2
        WRITTEN_ALPHABET = 3
        DIRECTION_HEAD = 4

    def __init__(
        self,
        tape: str,
        alphabets: list[str],
        states: list[str],
        initial_state: str,
        halt_state: str,
        program: list[tuple[str, str, str, str, int]]
    ):
        self.tape = tape
        self.alphabets = alphabets
        self.states = states
        self.initial_state = initial_state
        self.halt_state = halt_state
        self.program = program

    def validate(self):
        if not check_alphabets(alphabets=self.alphabets):
            raise ValidationError("alphabets list is not valid.")
        if not check_tape(tape=self.tape, alphabets=self.alphabets):
            raise ValidationError("tape is not valid.")
        if not check_states(
            states=self.states,
            initial_state=self.initial_state,
            halt_state=self.halt_state
        ):
            raise ValidationError("states list is not valid.")
        if not self._check_program():
            raise ValidationError("program is not valid.")
        self.is_valid = True

    def execute(self):
        if not self.is_valid:
            raise ValidationError("validation is not executed.")
        step = 0
        state = self.initial_state
        head = 0
        while(state != self.halt_state):
            print(f"===== step {step} =====")
            self.print_tape_and_head(head)
            alphabet = self.tape[head]
            for row in self.program:
                if row[self.Index.READ_ALPHABET.value] == alphabet and row[self.Index.NOW_STATE.value] == state:
                    self.tape = self.tape[:head] + row[self.Index.WRITTEN_ALPHABET.value] + self.tape[head+1:]
                    state = row[self.Index.NEXT_STATE.value]
                    if head != 0 or row[self.Index.DIRECTION_HEAD.value] != -1:
                        head = head + row[self.Index.DIRECTION_HEAD.value]
                    step = step + 1
                    break
        print(f"===== step {step} =====")
        self.print_tape_and_head(head)
        return True


    def print_tape_and_head(self, head):
        print(self.tape)
        print(''.join([' ' for _ in range(head)]) + '↑') 

    def _check_program(self):
        for row in self.program:
            if (
                (row[self.Index.READ_ALPHABET.value] not in self.alphabets) or
                (row[self.Index.WRITTEN_ALPHABET.value] not in self.alphabets) or 
                (row[self.Index.NOW_STATE.value] not in self.states) or 
                (row[self.Index.NEXT_STATE.value] not in self.states) or 
                (row[self.Index.DIRECTION_HEAD.value] not in [0,1,-1])
            ):
                return False
        return True