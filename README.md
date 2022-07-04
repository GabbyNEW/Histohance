# Histohance
## Instructions
1. If you don't have ``virtuanenv`` installed on your machine, run ``pip install virtualenv`` in your terminal to install it first.
2. Navigate to the project's root directory in your terminal and run ``python -m venv venv``. This creates a Python virtual environment named ``venv`` in the root directory.
3. Next, navgiate to the ``venv/Scripts`` directory. If you're on a Mac, you can skip this step and just run ``source env/bin/activate``.
   * For **cmd**, run ``activate.bat``.
   * For **powershell**, run ``activate.psl``.
4. In the virtual environment, navigate back to the root directory and install the required pip dependencies by running ``pip install -r requirements.txt``.
5. Launch the local flask app by running ``flask run``.