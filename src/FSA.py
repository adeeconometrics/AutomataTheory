from typing import Set, List, Dict, Callable, Union
from dataclasses import dataclass

from tabulate import tabulate


@dataclass(frozen=True, eq=True)
class State:
    m_state: str
    m_symbol:str = 'State'

    def __str__(self) -> str:
        return f'{self.m_symbol}({self.m_state})'

@dataclass(frozen=True, eq=True)
class States:
    m_states:Set[State]
        
    def __str__(self) -> str:
        return f"{{{','.join(str(i) for i in self.m_states)}}}"

@dataclass
class DFA:
    finite_states: Set[State]
    start_state: State
    final_state: State
    input_symbols: List[str]
    transition_table: Dict[Union[Set[State], State], Union[Set[State], State]]

    def __post_init__(self) -> None:
        if self.start_state not in self.finite_states:
            raise ValueError(
                f'start state: {self.start_state} is not defined in finite states {self.finite_states}')
        if self.final_state not in self.finite_states:
            raise ValueError(
                f'start state: {self.final_state} is not defined in finite states {self.finite_states}')

    def __str__(self) -> str:
        return tabulate(self.transition_table, headers = self.input_symbols, tablefmt='github')

    def to_nfa(self):
        pass


@dataclass
class NFA:
    finite_states: Set[State]
    input_symbols: List[str]
    start_state: State
    final_state: State
    transition_table: Dict[Union[Set[State],
                                    State], Union[Set[State], State]]

    def __post_init__(self) -> None:
        if self.start_state not in self.finite_states:
            raise ValueError(
                f'start state: {self.start_state} is not defined in finite states {self.finite_states}')
        if self.final_state not in self.finite_states:
            raise ValueError(
                f'start state: {self.final_state} is not defined in finite states {self.finite_states}')

    def __str__(self) -> str:
        return tabulate(self.transition_table, headers=self.input_symbols, tablefmt='github')

    def to_dfa(self):
        pass

if __name__ == '__main__':
    states = [State(i) for i in range(4)]
    start_state = State(0)
    final_state = State(3)
    input_symbols = [0, 1]
    transition_table = {
        State(0):[State(1), State(2)],
        State(1):[States({State(2), State(1)}), State(3)]
    }

    dfa = DFA(states, start_state, final_state,
              input_symbols, transition_table)
    print(dfa)
