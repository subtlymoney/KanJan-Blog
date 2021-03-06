# from flask.ext.script import Manager, Server
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from KanJanBlog import __init__
from KanJanBlog import models

# Init manager object via app object
manager = Manager(__init__.app)

# Init migrate object via app adn db object
migrate = Migrate(__init__.app, models.db)

# Create some new commands
# This command will be run the Flask development_env server
manager.add_command('server', Server())
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    '''
    Create a python CLI.

    :return: Default import object
    type: 'Dict'
    '''
    return dict(app=__init__.app,
                db=models.db,
                User=models.User,
                Post=models.Post,
                Comment=models.Comment,
                Tag=models.Tag
                )

if __name__ == '__main__':
    manager.run()