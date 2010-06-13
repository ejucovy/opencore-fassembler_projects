from fassembler import tasks
from fassembler.project import Project, Setting

class ZineProject(Project):
    """
    Install Zine
    """

    name = 'zine'
    title = 'Install Zine'
    settings = [
        Setting('db_sqlobject',
                default='mysql://{{config.db_username}}:{{config.db_password}}@{{config.db_host}}/{{config.db_name}}?charset=utf8',
                help='Full SQLObject connection string for database'),
        Setting('db_username',
                default='tasktracker',
                help='Database connection username'),
        Setting('db_password',
                default='tasktracker',
                help='Database connection password'),
        Setting('db_host',
                default='localhost',
                help='Host where database is running'),
        Setting('db_name',
                default='{{env.config.getdefault("general", "db_prefix", "")}}tasktracker',
                help='Name of database'),
        Setting('db_test_sqlobject',
                default='mysql://{{config.db_username}}:{{config.db_password}}@{{config.db_host}}/{{config.db_test_name}}',
                help='Full SQLObject connection string for test database'),
        Setting('db_test_name',
                default='tasktracker_test',
                help='Name of the test database'),
        Setting('db_root_password',
                default='{{env.db_root_password}}',
                help='Database root password'),
        #Setting('tasktracker_repo',
        #        default='https://svn.openplans.org/svn/TaskTracker/trunk',
        #        help='svn location to install TaskTracker from'),
        Setting('zine_instances_directory',
                default='{{env.base_path}}/var/{{project.name}}/instances',
                help="Directory that will house all projects' Zine instances (config files and sqlite databases)",
                ),
        Setting('port',
                default='{{env.base_port+4}}',
                help='Port to install Zine on'),
        Setting('host',
                default='localhost',
                help='Host to serve on'),
        Setting('spec',
                default='requirements/zine-req.txt',
                help='Specification of packages to install'),
        Setting('config_tmpl_location',
                default='http://socialplanning-opencore.googlecode.com/svn/fassembler/templates/zine',
                help="SVN location of config template file(s)"),
        ]

    actions = [
        tasks.VirtualEnv(),
        tasks.InstallSpec('Install Zine',
                          '{{config.spec}}'),
        tasks.SvnCheckout('Checkout paste configuration template',
                          '{{config.config_tmpl_location}}',
                          'zine/src/paste_template'),
        tasks.InstallPasteConfig(path='zine/src/paste_template/paste.ini_tmpl'),
        tasks.InstallPasteStartup(),
        tasks.InstallSupervisorConfig(),
        ]


