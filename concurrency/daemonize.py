import sys
import os
from signal import signal
import getopt
import logging

class Daemon:
    """
    A generic daemon class.

    Usage: subclass the Daemon class and override the run() method
    """

    SIG_STOP = 10

    def __init__(self, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        pid_dir = '/tmp/ml'
        if not os.path.isdir(pid_dir):
            os.mkdir(pid_dir)
        self.pidfile = "{0}/{1}.pid".format(pid_dir, self.__class__.__name__)
        self.working_dir = os.getcwd()
        self.server = None
        self.DEV_MODE = False

    def setup_server(self):
        raise NotImplementedError("server must be set to run!")

    def daemonize(self):
        """
        do the UNIX double-fork magic, see Stevens' "Advanced
        Programming in the UNIX Environment" for details (ISBN 0201563177)
        http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
        """
        print("daemonize started ...")
        try:
            pid = os.fork()
            if pid > 0:
                # exit first parent
                sys.exit(0)
        except OSError as e:
            logging.error("fork #1 failed: %d (%s)" % (e.errno, e.strerror))
            sys.exit(1)

        # decouple from parent environment
        os.chdir("/")
        os.setsid()
        os.umask(0)

        # do second fork
        try:
            pid = os.fork()
            if pid > 0:
                # exit from second parent
                sys.exit(0)
        except OSError as e:
            logging.error("fork #2 failed: %d (%s)" % (e.errno, e.strerror))
            sys.exit(1)

        # redirect stdin stdout stderr
        logging.info("input/output redirect...")
        logging.info("please read log for furthermore information!")
        sys.stdout.flush()
        sys.stderr.flush()

        with open('/dev/null') as read_null, open('/dev/null', 'w') as write_null:
            # method dup2() duplicates file descriptor fd to fd2
            os.dup2(read_null.fileno(), sys.stdin.fileno())
            os.dup2(write_null.fileno(), sys.stdout.fileno())
            os.dup2(write_null.fileno(), sys.stderr.fileno())

        # write pidfile
        pid = str(os.getpid())
        with open(self.pidfile, 'w+') as f:
            f.write(pid)

        # set working_dir
        os.chdir(self.working_dir)
        logging.info("daemonize finished")

    def delpid(self):
        try:
            os.remove(self.pidfile)
            print("PID file removed. file: {}".format(self.pidfile))
        except IOError as e:
            print(e)

    def start(self):
        """
        Start the daemon
        """
        # Check for a pidfile to see if the daemon already runs
        try:
            with open(self.pidfile, 'r') as pf:
                pid = int(pf.read().strip())
        except IOError:
            pid = None

        #make certain that pid is not None and process is running.
        if pid:
            print("pidfile {} already exist.")
            if os.path.exists("/proc/{}" .format(pid)):
                print("Daemon already running.".format(self.pidfile))
            else:
                print("Deamon is already killed, please stop() first for deleting pid file.")
            sys.exit(1)

        # Start the daemon, run the server
        self.setup_log()
        logging.info("=============start/restart server=============")
        self.setup_config()
        # don't deamonize in dev mode
        if not self.DEV_MODE:
            # just use print() to show info in console before redirection happening in self.daemonize().
            # just use logging.info() after setup_log().
            # use logging module as soon as possible.
            self.daemonize()
        self.setup_server()  # only set server before run
        self.setup_signal_handler()
        self.server.run()

    def stop(self):
        """
        Stop the daemon
        """
        # Get the pid from the pidfile
        try:
            with open(self.pidfile, 'r') as pf:
                pid = int(pf.read().strip())
        except IOError:
            pid = None

        if not pid:
            print("pidfile {} does not exist. Daemon not running?".format(self.pidfile))
            return  # not an error in a restart

        # Try killing the daemon process and deleting pid file
        try:
            os.kill(pid, self.SIG_STOP)
        except:
            print("try killing process failed!")
            print("Unexpected error: {}".format(sys.exc_info()[0]))
        finally:
            self.delpid()

    def restart(self):
        """
        Restart the daemon
        """
        self.stop()
        self.start()

    def setup_log(self):
        #lc.setup_logging()
        logging.info("log setup finished")

    def setup_config(self):
        #cm.setup_config()
        logging.info("config setup finished")

    def setup_signal_handler(self):
        signal(self.SIG_STOP, self.signal_handler)

    def signal_handler(self, signum, frame):
        logging.info("signal received: {}".format(signum))
        if signum == self.SIG_STOP:
            logging.info("termination process is started. pls wait ...")
            self.server.stop()

    def main(self):
        """
        all server based classes should start/stop/restart with method 'main()'
        """
        try:
            opts, args = getopt.getopt(sys.argv[1:], 'h', ['help'])
        except getopt.error as e:
            print(e)
            print('for help use --help')
            print("usage: {} start|stop|restart".format(sys.argv[0]))
            sys.exit(2)

        # set dev mode
        if len(args) == 2 and 'dev' == args[1]:
            self.DEV_MODE = True
            print("in dev mode...")

        if len(args) >= 1:
            if 'start' == args[0]:
                self.start()
            elif 'stop' == args[0]:
                self.stop()
            elif 'restart' == args[0]:
                self.restart()
            else:
                print("unknown command: {}".format(args[0]))
                sys.exit(2)
            sys.exit(0)
