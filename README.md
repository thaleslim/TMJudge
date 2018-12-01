# TMJudge
Projeto de construção de uma interface de correção de códigos online

:octocat: Append and modify this list as you make changes to this repository :innocent:
- [ ] unchecked example
- [x] checked example

TODOs:

 - [ ] Rever forma de execução do código: pouco seguro usar 
     ```python
     subprocess.run(*args, shell=True)
     ```
     - Possível paranoia com segurança, considerando que os comandos do _`cmd`_ são imbutidos no código
