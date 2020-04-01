#!/usr/bin/env python3
from time import sleep
import shlex
import configparser
from subprocess import Popen, PIPE
from dogtail.rawinput import typeText, pressKey, keyCombo
from dogtail.tree import root
from qecore.utility import run
from qecore.logger import QELogger

log = QELogger()

class Application:
    def __init__(self, component, a11y_app_name=None, desktop_file_exists=True,
                 desktop_file_name=None, app_process_name=None, shell=None,
                 session_type="", session_desktop="", logging=False):
        """
        .. note::

            Do **NOT** call this by yourself.
            This class is instanced by :py:meth:`sandbox.TestSandbox.get_application`.

        :type component: str
        :param component: Component name - usually the name of the application package.

        :type a11y_app_name: str
        :param a11y_app_name: Name of application as it appears in accessibility tree.

        :type desktop_file_exists: bool
        :param desktop_file_exists: States that desktop file of given application exists or not.

        :type desktop_file_name: str
        :param desktop_file_name: Name of desktop file if not same as component.

        :type app_process_name: str
        :param app_process_name: Name of application process if not same as component.

        :type logging: bool
        :param logging: Turn on logging of this submodule. Passed from sandbox.
        """

        self.logging = logging

        if self.logging:
            log.info(" ".join((
                f"__init__(self, component={component}, a11y_app_name={a11y_app_name},",
                f"desktop_file_exists={desktop_file_exists},",
                f"desktop_file_name={desktop_file_name},",
                f"app_process_name={app_process_name}, shell='shell',",
                f"session_type={session_type}, session_desktop={session_desktop},",
                f"logging={str(logging)})"
            )))

        self.shell = shell
        self.session_type = session_type
        self.session_desktop = session_desktop
        self.pid = None
        self.instance = None
        self.component = component
        self.a11y_app_name = a11y_app_name if a11y_app_name else component
        self.desktop_file_exists = desktop_file_exists
        self.exit_shortcut = "<Control_L><Q>"
        self.kill = True
        self.kill_command = None
        self.desktop_file_name = desktop_file_name if desktop_file_name else ""
        self.app_process_name = app_process_name if app_process_name else component
        self.get_desktop_file_data()

        self.preserve_old_api()


    def get_desktop_file_data(self):
        """
        Parse desktop file.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`__init__`.
        """

        if self.logging:
            log.info(f"{self.component} get_desktop_file_data(self)")

        if self.desktop_file_exists: # zenity/gnome-shell do not have desktop file
            desktop_run = run(" ".join((
                f"rpm -qlf $(which {self.component}) |",
                f"grep /usr/share/applications/ |",
                f"grep .desktop |",
                f"grep '{self.desktop_file_name}'"
            )), verbose=True)

            if desktop_run[1] != 0:
                raise Exception(f"Desktop file of application '{self.component}' was not found.")

            desktop_file = desktop_run[0].strip("\n")
            desktop_file_config = configparser.RawConfigParser()
            desktop_file_config.read(desktop_file)

            self.name = desktop_file_config.get("Desktop Entry", "name")
            self.exec = desktop_file_config.get("Desktop Entry", "exec").split(" ")[0]


    def start_via_command(self, command=None, **kwargs):
        """
        Start application via command.

        :type command: str
        :param command: Complete command that is to be used to start application.

        :type in_session: bool
        :param in_session: Start application via command in session.
        """

        kill = None
        in_session = None

        for key, val in kwargs.items():
            if "session" in str(key).lower():
                in_session = val

            if "kill" in str(key).lower():
                kill = val

        if self.logging:
            log.info("".join((
                f"{self.component} ",
                f"start_via_command(self, command={command}, in_session={in_session})"
            )))

        kill_override = kill if kill else self.kill

        if self.is_running() and kill_override:
            self.kill_application()

        if in_session:
            pressKey("Esc")
            keyCombo("<Alt><F2>")
            sleep(0.5)
            keyCombo("<Alt><F2>")
            sleep(0.5)
            enter_a_command = self.shell.findChild(lambda x: "activate" in x.actions and x.showing)
            enter_a_command.text = command if command else self.exec
            sleep(0.5)
            pressKey("Enter")
        else:
            self.process = Popen(shlex.split(command if command else self.exec),\
                 stdout=PIPE, stderr=PIPE)

        self.wait_before_app_starts(30)
        self.instance = self.get_root()


    def start_via_menu(self, kill=None):
        """
        Start application via menu.

        Starting the application by opening shell overview and typing the application
        name that is taken from the application's desktop file. This does no longer work
        in a new gnome-classic as it lost the search bar.
        """

        if self.logging:
            log.info(f"{self.component} start_via_menu(self)")

        if "classic" in self.session_desktop:
            assert False, f"Application cannot be started via menu in {self.session_desktop}."

        if not self.desktop_file_exists:
            raise Exception("".join((
                f"Testing target '{self.a11y_app_name}' does not have desktop file. ",
                f"Indication of user failure!"
            )))

        kill_override = kill if kill else self.kill

        if self.is_running() and kill_override:
            self.kill_application()

        run(" ".join((
            "dbus-send",
            "--session",
            "--type=method_call",
            "--dest=org.gnome.Shell",
            "/org/gnome/Shell",
            "org.gnome.Shell.FocusSearch"
        )))

        sleep(1)
        typeText(self.name)
        pressKey("Enter")

        self.wait_before_app_starts(30)
        self.instance = self.get_root()


    def close_via_shortcut(self):
        """
        Close application via shortcut.

        Closing application via shortcut Ctrl+Q.
        If for any reason the application does not have this shortcut you can define the shortcut
        to use in class attribute :py:attr:`exit_shortcut`

        .. note::

            Format of the shortcut is a string with each key character encapsuled in < >.
            Here are  a few examples: <Ctrl><Q> <Alt><F4> <Ctrl><Shift><Q>
        """

        if self.logging:
            log.info(f"{self.component} close_via_shortcut(self)")

        if not self.is_running():
            raise Exception("".join((
                f"Application '{self.a11y_app_name}' is no longer running. ",
                f"Indication of test failure!"
            )))

        keyCombo(self.exit_shortcut)

        self.wait_before_app_closes(30)
        self.instance = None


    def already_running(self):
        """
        If application is started by other means, other than methods from this class,
        this will retrieve the root of the application.
        """

        if self.logging:
            log.info(f"{self.component} already_running(self)")

        self.wait_before_app_starts(15)
        self.instance = self.get_root()


    def get_root(self):
        """
        Get accessibility root of appllication.

        :return: Return root object of application.
        :rtype: <dogtail.tree.root.application>

        This method is used upon application start to retrieve a11y object to use in the test.
        You do not need to use this by yourself, but can be useful in some situations.
        """

        if self.logging:
            log.info(f"{self.component} get_root(self) search by '{self.a11y_app_name}'")

        return root.application(self.a11y_app_name)


    def is_running(self):
        """
        Get accessibility root of appllication.

        :return: Return state of application. Running or not.
        :rtype: bool

        This method is used by various other methods in this class to ensure correct behaviour.
        You do not need to use this by yourself, but can be useful in some situations.
        """

        if self.logging:
            log.info(f"{self.component} is_running(self)")
        try:
            for _ in range(3):
                is_running = self.a11y_app_name in [x.name for x in root.applications()]
                if is_running:
                    break
            return is_running
        except Exception:
            return False


    def get_pid_list(self):
        """
        Get list of processes of running application.

        :return: Return all running processes of application, \
            seperated by new line character, not converting to list. \
            Return nothing if application is not running.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`get_all_kill_candidates`
            when stopping the application.
        """

        if self.logging:
            log.info(f"{self.component} get_pid_list(self)")

        if self.is_running():
            return run(f"pgrep -fla {self.app_process_name}").strip("\n")

        return None


    def get_all_kill_candidates(self):
        """
        Take result of :func:`get_pid_list` and return only processes of application.

        :rtype: list
        :return: Return all IDs of application processes.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`kill_application`\
            when stopping the application.

        If kill candidate happens to have ['runtest', 'behave', 'dogtail', '/usr/bin/gnome-shell']
        in its process name. Process will not be killed.
        Return empty list if no satisfactory process was found.
        This prevents testname colliding with found process so we will not kill the test itself.
        """

        if self.logging:
            log.info(f"{self.component} get_all_kill_candidates(self)")

        application_pid_string = self.get_pid_list()
        if application_pid_string:
            application_pid_list = application_pid_string.split("\n")
        else:
            return []

        final_pid_list = []
        for process in application_pid_list:
            if not (("runtest" in process) or \
                    ("behave" in process) or \
                    ("dogtail" in process) or \
                    (process == "/usr/bin/gnome-shell")):
                extracted_pid = process.split(" ", 1)[0]
                try:
                    final_pid_list.append(int(extracted_pid))
                except ValueError:
                    pass # skip non-digits
        return final_pid_list


    def kill_application(self):
        """
        Kill application.

        This method is used by :func:`start_via_command` and :func:`start_via_menu` to ensure
        the application is not running when starting the test. So we kill all application instances
        and open a new one to test on.
        You do not need to use this by yourself, but can be useful in some situations.
        """

        if self.logging:
            log.info(f"{self.component} kill(self)")

        if self.is_running() and self.kill:
            if not self.kill_command:
                for pid in self.get_all_kill_candidates():
                    run(f"sudo kill -9 {pid} > /dev/null")
            else:
                run(self.kill_command)


    # Following two could be merged, I could not think of a nice way of doing it though.
    def wait_before_app_starts(self, time_limit):
        """
        Wait before application starts.

        :type time_limit: int
        :param time_limit: Number which signifies time before the run is stopped.
        """

        if self.logging:
            log.info("".join((
                f"{self.component} ",
                f"wait_before_app_starts(self, time_limit={time_limit})"
            )))


        for _ in range(time_limit * 10):
            if not self.is_running():
                sleep(0.1)
            else:
                return

        assert False, "".join((
            f"Application '{self.a11y_app_name}' is not running. ",
            f"Indication of test failure!"
        ))

    def wait_before_app_closes(self, time_limit):
        """
        Wait before application stops.

        :type time_limit: int
        :param time_limit: Number which signifies time before the run is stopped.
        """

        if self.logging:
            log.info("".join((
                f"{self.component} ",
                f"wait_before_app_closes(self, time_limit={time_limit}"
            )))


        for _ in range(time_limit * 10):
            if self.is_running():
                sleep(0.1)
            else:
                return

        assert False, "".join((
            f"Application '{self.a11y_app_name}' is running. ",
            f"Indication of test failure!"
        ))


    def preserve_old_api(self):
        """
        Preserving old api as the new names of functions and attributes are snake_case complient.

        .. note::

            Do **NOT** call this by yourself. This method is called by :func:`application.Application.__init__`.
        """

        self.a11yAppName = self.a11y_app_name
        self.desktopFileExists = self.desktop_file_exists
        self.exitShortcut = self.exit_shortcut
        self.desktopFileName = self.desktop_file_name
        self.appProcessName = self.app_process_name
        self.getDesktopFileData = self.get_desktop_file_data
        self.getRoot = self.get_root
        self.isRunning = self.is_running
        self.getPidList = self.get_pid_list
        self.getAllKillCandidates = self.get_all_kill_candidates
