## 📌 Python Packages
- Python Standard Library - putem face import fara sa instalam
librarii. Exemple: math, random
- Python Packages - este necesar sa facem instalarea pachetului
inainte sa il utilizam si astfel putem folosi functiile/metodele
astfel incat sa ne optimizam codul. Exemple: behave, SQLAlchemy etc.
- Pentru pachete extra, facute de alti developeri, avem PYPI:
https://pypi.org si folosim comanda pip pentru instalarea lor.
- Link-uri de studiat:
1. https://packaging.python.org/tutorials/installing-packages/
2. https://packaging.python.org/tutorials/packaging-projects/


## 📌 Virtual environments
- Este folosit pentru a gestiona python packages pentru diferite
proiecte.
- Avantaje:
  - putem descarca pachete in proiectul nostru fara privilegii de administrator
  - putem crea un pachet cu aplicatia noastra si ulterior o putem partaja cu alti programatori
  - putem crea cu usurinta o lista de dependinte si subdependinte intr-un fisier
, ceea ce face mai usor pentru alti programatori sa reproduca/dezvolte
si sa instaleze toate dependintele utilizate de noi in virtual environment
- Instalare virtualenv (adica programul care ne ajuta sa cream si sa folosim un virtual env)
  - putem folosi comanda: ```pip install virtualenv```
- Avem 3 parti importante in folosirea lui:
1. CREARE: ```python -m venv nume_folder_venv``` - aici de obicei
folosim env/venv/myenv pentru acel nume de folder, sa zicem de exemplu
ca il numim myenv. Crearea se face o singura data!
2. ACTIVARE: trebuie sa il activam ori de cate ori avem nevoie
sa rulam proiectul, sa instalam o librarie; comanda de activare e diferita in functie
de sistemul de operare:
- OSX: ```source myenv/bin/activate```
- Windows Powershell: ```myenv/Scripts/Activate.ps1```
- Windows cmd/Pycharm Terminal: ```myenv/Scripts/activate.bat```
3. DEZACTIVARE: asta o putem face cand vrem in acelasi terminal sa trecem
sa lucram la un alt proiect, comanda e: ```deactivate```

#### pip comands

```python
"""
Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  inspect                     Inspect the python environment.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  index                       Inspect information available from package indexes.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --debug                     Let unhandled exceptions propagate outside the main subroutine, instead of logging them to stderr.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  --require-virtualenv        Allow pip to only run in a virtual environment; exit with an error otherwise.
  --python <python>           Run pip with the specified Python interpreter.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --no-input                  Disable prompting for input.
  --keyring-provider <keyring_provider>
                              Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled, import, subprocess]. (default: disabled)        
  --proxy <proxy>             Specify a proxy in the form scheme://[user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.
  --cert <path>               Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL Certificate Verification' in pip documentation for more information.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index.
  --no-color                  Suppress colored output.
  --no-python-version-warning
                              Silence deprecation warnings for upcoming unsupported Pythons.
  --use-feature <feature>     Enable new functionality, that may be backward incompatible.
  --use-deprecated <feature>  Enable deprecated functionality, that will be removed in the future.
PS D:\NEW_Python_projects\PYTA_14\sesiunea_13_Exercitii_OOP_(mini-proiect)\proiecte_individuale\proiect_calculator> 

"""
```