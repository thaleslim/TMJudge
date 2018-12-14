# TMJudge

    TMJudge: A Code Judge Environment
    Copyright (C) 2018 Thales Menezes

    Philosophy:
        A Code Judge should be a tool to guide student's programmin' learning,
        a environment to correct and show errors as opportunities for growth;
        while also assisting teachers and tutors with class management, giving
        more time to address specific or theorical questions with the student.

        To achieve this, the judge can not be viewed by students as a foe
        to be defeated; or a buggy program to appologize for it's flaws
        in a attempt to keep the student motivated.
        
        The judge should be as independent, well polished and communicative as
        possible, it should be a arrow pointing in a direction, when necessary,
        instead of a riddle to be solved in every single feature.

    This program is free software: you can redistribute it and/or modify it under the terms
    of the GNU Affero General Public License as published by the Free Software Foundation,
    either version 3 of the License, or any later version.

    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
    without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License along with this
    program.  If not, see <https://www.gnu.org/licenses/>.

    Lead Developer:
        Thales Menezes - Undergraduated Computer Science student at University of Brasília
        source := https://github.com/thaleslim/TMJudge
        email  := thalesmenezes13@gmail.com

:innocent: Append and modify this list as you make changes to this repository

- [ ] unchecked example
- [x] checked example

:octocat: Thank you  

#### TODOs (always remember to prioritize the essentials):
- [ ] Use custom exceptions module:
    - Usage example:
    ```python
    import sys
    sys.path.append(__file__ + '\\..\\..\\..\\')
    from engine import InvalidArgument as custom_errors
    def func(*args):
        if not len(args):
            raise custom_errors.InvalidArgument("No parameters were assigned", args)
    ```
- [ ] Add a way to kill the program after time runs outs or infinite loop
    - Solution: use `trace` module instead of `exec()` and `eval()` directly
- [ ] Expand Tester.run() funcionalities
    - [ ] Store more details about the subject' code:
        - Examples: uses recursion? where?
    - [ ] If multiple inputs -> execute run multiple times -> return list(Program())
    - [ ] Add support to filename or code as input
    <!--
        Possible use to capture raised Exceptions from the students code
        caplog
        logging.LogRecord
        https://docs.pytest.org/en/latest/reference.html#caplog
      -->
- [ ] Optional: Make this prettier
    - [ ] pytest config `python -m pytest -s --maxfail=2 test_file.py --filename path\to\file.py`
    - [ ] Inside `conftest.py`, the global fixture file for pytest, this import is used
        ```python
        import sys
        sys.path.append(__file__ + '\\..\\..\\')
        from engine import Tester
        ```

#### Solved (Latest to Oldest):
- [x] Generate test log
    - Note: executin' the module will be a task to the web environment to query
    - Solution: basic logging implemented, appends to file the new message
    ```python
    # file: engine.Tester
    def log(error_message: str, expect: str, output: str, logfile: str = "log.txt", sep: str = "\r\n¤»Judge«¤\r\n"):
    ```
- [x] Filename argument is hardcoded
    - Solution: Added support to `-F` and `--filename` console args, watch for open() restrictions
- [x] Study the possibility to create a package for extra modules
    - Solution: Created package `engine` with essential modules to the Judge
- [x] Reorganize files structure
    - Solution: Current structure stands on 3 main folders:
        ```
        ├── alumni
        │   └── enrollment code
        │       └── challenge package number
        │           └── <challenge name>.py
        ├── engine
        │   ├── __init__.py
        |   ├── <exceptions_classes>.py
        │   └── Tester.py
        └── tests
            └── challenge package number
                └── test_<challenge name>.py
        ```
- [x] Add support to `input()`
    - Solution: using another `contextmanager`.
- [x] Create a function to run code passing arguments
    - Solution: `@pytest.fixture run` created.
- [x] Review the way to run the subject' code: I worry about it's safety and usability towards the server 
    ```python
    subprocess.run(args, shell=True)
    ```
    - Possibly worrying more than necessary, considerating it's most likely to be used with beginner programmers and the _`shell commands`_ are "hardcoded".
        - Solution: instead of using `subprocess` module we can use python' built-in `exec()` and `eval()` passing the subject' code. This provides more security to server (since we don't need to access the shell anymore) and flexibility (we can insert lines of code to extract usefull information about the code being tested) without the need to analyse the code for "malicious intent"(may be a feature on later versions); besides, less modules needed.

#### Remember where you began:
```python
# First ideia
import subprocess as console
def test_main():
    assert console.check_output('python src/main.py', timeout=1, shell=True).decode('utf-8') == 'hello'
```