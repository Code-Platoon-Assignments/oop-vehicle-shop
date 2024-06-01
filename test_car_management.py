import pytest
from car_management import run_the_manager
    
def test_add_a_car(monkeypatch, capsys):
    inputs = iter(['1', 'Toyota', 'Camry', '2020', "7"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    run_the_manager()
    out,err = capsys.readouterr()
    assert out.startswith("Car added successfully!")
    
def test_all_cars(monkeypatch, capsys):
        inputs = iter(['2', "7"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        run_the_manager()
        out,err = capsys.readouterr()
        assert "All Cars:" in out
        assert "2020 Toyota Camry" in out
        
def test_total_number_of_cars(monkeypatch, capsys):
        inputs = iter(['3', "7"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        run_the_manager()
        out,err = capsys.readouterr()
        assert out.split("\n")[0] == "Total number of cars: 1"
        
def test_what_is_car_id(monkeypatch, capsys):
        inputs = iter(['4','1',"7"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        run_the_manager()
        out,err = capsys.readouterr()
        assert out == """ID: 1
Make: Toyota
Model: Camry
Year: 2020
Mileage: 0
Services: 
Goodbye
"""


def test_enter_service(monkeypatch, capsys):
        inputs = iter(['5','1', "Oil Change", "4", '1', "7"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        run_the_manager()
        out,err = capsys.readouterr()
        assert out == """ID: 1
Make: Toyota
Model: Camry
Year: 2020
Mileage: 0
Services: Oil Change
Goodbye
"""

def test_enter_new_mileage(monkeypatch, capsys):
        inputs = iter(['6','1', "5000", "4", '1', '7'])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        run_the_manager()
        out,err = capsys.readouterr()
        assert out == """ID: 1
Make: Toyota
Model: Camry
Year: 2020
Mileage: 5000
Services: Oil Change
Goodbye
"""

def test_quit(monkeypatch, capsys):
        inputs = iter(['7'])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        run_the_manager()
        out,err = capsys.readouterr()
        assert out == """Goodbye
"""

def test_invalid_input(monkeypatch, capsys):
        inputs = iter(['17', "7"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        run_the_manager()
        out,err = capsys.readouterr()
        assert out == """Invalid input
Goodbye
"""