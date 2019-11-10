   Flask with sign up twitter and facebook
=======================================

1. Sign up with facebook
2. Sign up with twitter

How to run server
=======================================
1. Access folder that contain run.py file
2. Custom config
    > export APP_SETTINGS=config.DevelopmentConfig
3. Install virtual env
    > virtualenv -p (address python3) venv <br>
    pip install requirements.txt
4. Start mysql
    > mysql.server start          
5. Run server
    > python run.py <br>

How to run tdd test
=======================================
1. Access folder that contain run.py file
2. Run command
    > python manage.py test
    
How to run bdd test
=======================================
1. Access folder that contain run.py file
2. Run command
    > behave features/checkform.feature <br>
     behave features/checkfb.feature <br>
     behave features/checktw.feature