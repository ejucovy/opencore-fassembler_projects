from fassembler import tasks
from fassembler.project import Project, Setting

class FrontendProject(Project):
    """
    Install the libopencore frontend that proxies over http to opencore,
    tasktracker and wordpress, with a Deliverance theme applied to the
    tasktracker and wordpress responses.
    """

    name = 'frontend'
    title = "Install frontend"

    settings = [
        Setting('port',
                default='{{env.base_port}}',
                help='Port the frontend should listen on'),
        Setting('opencore_remote_uri',
                default='http://localhost:{{env.base_port+1}}',
                help="Base domain and port that opencore's Zope instance is listening on"),
        Setting('tasktracker_remote_uri',
                default='http://localhost:{{env.base_port+4}}',
                help="Base domain and port that TaskTracker is listening on"),
        Setting('wordpress_remote_uri',
                default='http://localhost:{{env.base_port+3}}',
                help="Base domain and port that WordPress is listening on"),
        Setting('zine_remote_uri',
                default='http://localhost:{{env.base_port+3}}',
                help="Base domain and port that Zine is listening on"),
        Setting('use_tasktracker',
                default='1',
                help="Set to 0 if you don't have tasktracker enabled"),
        Setting('use_wordpress',
                default='1',
                help="Set to 0 if you don't have wordpress enabled"),
        Setting('use_zine',
                default='0',
                help="Set to 1 if you have zine enabled"),
        Setting('spec',
                default='requirements/frontend-req.txt',
                help='Specification of packages to install'),
        Setting('only_local_connections',
                default='0',
                help="Set to 1 if you want to restrict access to localhost (for example if you are using a proxy server as your frontmost component)"),
        Setting('static_file_root',
                default='None',
                help="(Optional) Full path to a directory on the filesystem where static files will be served from. If set, a Paste#static fileserver will be mounted on the path prefix `/++static++/`"),
        Setting('config_tmpl_location',
                default='http://socialplanning-opencore.googlecode.com/svn/fassembler/templates/frontend',
                help="SVN location of config template file(s)"),
        Setting('use_twirlip',
                default='1',
                help="Set to 0 if you don't have twirlip enabled"),
        Setting('shared_secret_filename',
                default='{{env.var}}/secret.txt',
                help='Path to the file containing the shared secret used to encrypt and decrypt the auth cookie'),
        Setting('twirlip_remote_uri',
                default='http://localhost:{{env.base_port+7}}',
                help="Base domain and port that Twirlip is listening on"),
        ]

    actions = [
        tasks.VirtualEnv(),
        tasks.InstallSpec('Install frontend', '{{config.spec}}'),
        tasks.SvnCheckout('Checkout paste configuration template',
                          '{{config.config_tmpl_location}}',
                          'frontend/src/paste_template'),
        tasks.InstallPasteConfig(path='frontend/src/paste_template/paste.ini_tmpl'),
        tasks.InstallPasteStartup(),
        tasks.InstallSupervisorConfig(),
        ]
